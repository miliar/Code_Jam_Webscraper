#include<stdio.h>
#include<string.h>

char mp[10][16];
int win[10], lose[10];
double res[10], owp[10];
void solve() {
	int N;
	scanf("%d", &N);
	memset(win, 0, sizeof(win));
	memset(lose, 0, sizeof(lose));
	for(int i=0;i<N;i++) {
		scanf("%s", mp[i]);
		for(int j=0;j<N;j++) {
			if(mp[i][j]=='1') win[i]++;
			else if(mp[i][j]=='0') lose[i]++;
		}
		res[i]=0.25*win[i]/(lose[i]+win[i]);
	}
	for(int i=0;i<N;i++) {
		double o=0;
		int cnt=0;
		for(int j=0;j<N;j++) {
			if(mp[i][j]=='1') {
				o+=(double)win[j]/(win[j]+lose[j]-1);
				cnt++;
			} else if(mp[i][j]=='0') {
				o+=(double)(win[j]-1)/(win[j]+lose[j]-1);
				cnt++;
			}
		}
		owp[i]=o/cnt;
		res[i]+=0.5*owp[i];
	}
	for(int i=0;i<N;i++) {
		double o=0;
		int cnt=0;
		for(int j=0;j<N;j++) {
			if(mp[i][j]!='.') {
				o+=owp[j];
				cnt++;
			}
		}
		res[i]+=0.25*o/cnt;
	}
	for(int i=0;i<N;i++) {
		printf("%.12lf\n", res[i]);
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for(int c=1;c<=T;c++) {
		printf("Case #%d:\n", c);
		solve();
	}
}