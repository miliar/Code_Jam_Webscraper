#include<stdio.h>
#include<string.h>

int data[1000], next[1000], flag[1000];
long long val[1000], steps[1000];
long long solve() {
	int R, k, N;
	scanf("%d%d%d", &R, &k, &N);
	for(int i=0;i<N;i++) scanf("%d", &data[i]);

	long long sm=0;
	int end=0, len=0;
	for(int i=0;i<N;i++) {
		while(len<N && sm+data[end]<=k) {
			sm+=data[end];
			end=(end+1)%N;
			len++;
		}
		next[i]=end;
		val[i]=sm;
		sm-=data[i];
		len--;
	}

	memset(flag, -1, sizeof(flag));
	int p=0, l, s;
	sm=0;
	for(int i=0;;i++) {
		if(flag[p]!=-1) {
			l=i-flag[p];
			s=flag[p];
			sm-=steps[s];
			break;
		}
		steps[i]=sm;
		flag[p]=i;
		sm+=val[p];
		p=next[p];
	}

	sm*=(R-s)/l;
	R=(R-s)%l+s;
	sm+=steps[R];
	return sm;
}

int main() {
	int T;
	scanf("%d", &T);
	for(int c=1;c<=T;c++) {
		printf("Case #%d: %lld\n", c, solve());
	}
}