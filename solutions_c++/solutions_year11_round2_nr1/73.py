#include<cstdio>

#define NMAX 100

int n; char table[NMAX][NMAX];
double wp[NMAX],owp[NMAX],oowp[NMAX];

double _wp(int a,int b) {
	int i,win=0,cnt=0;
	for(i=0;i<n;i++) {
		if(i==b)continue;
		if(table[a][i]!='.') {
			cnt++;
			if(table[a][i]=='1')win++;
		}
	}
	double ret=(double)win/cnt;
	return ret;
}

void solve() {
	int i,j,a,b; double sum; int cnt;
	for(i=0;i<n;i++) {
		wp[i]=0;
		a=0;
		b=0;
		for(j=0;j<n;j++) {
			if(table[i][j]!='.') {
				b++;
				if(table[i][j]=='1')a++;
			}
		}
		wp[i]=(double)a/b;
	}
	for(i=0;i<n;i++) {
		owp[i]=0;
		sum=0;
		cnt=0;
		for(j=0;j<n;j++) {
			if(table[i][j]!='.') {
				sum+=_wp(j,i);
				cnt++;
			}
		}
		owp[i]=sum/cnt;
	}
	for(i=0;i<n;i++) {
		oowp[i]=0;
		sum=0;
		cnt=0;
		for(j=0;j<n;j++) {
			if(table[i][j]!='.') {
				sum+=owp[j];
				cnt++;
			}
		}
		oowp[i]=sum/cnt;
	}
}

void input() {
	int i,j;
	scanf("%d",&n);
	for(i=0;i<n;i++) {
		for(j=0;j<n;j++) {
			scanf(" %c",&table[i][j]);
		}
	}
}

int main() {
	int T,S;
	scanf("%d",&T);
	for(S=1;S<=T;S++) {
		input();
		solve();
		printf("Case #%d:\n",S);
		for(int i=0;i<n;i++) {
			double x=wp[i]+owp[i]*2+oowp[i];
			x/=4;
			printf("%.8f\n",x);
		}
	}
	return 0;
}
