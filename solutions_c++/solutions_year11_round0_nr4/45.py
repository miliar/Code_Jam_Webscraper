#include<cstdio>

#define NMAX 1000

int work() {
	static int a[NMAX];
	int n,i,now,cnt,nxt,ret=0;
	scanf("%d",&n);
	for(i=0;i<n;i++) {
		scanf("%d",a+i);
		a[i]--;
	}
	for(i=0;i<n;i++) {
		now=i;
		cnt=0;
		while((nxt=a[now])>=0) {
			a[now]=-1;
			cnt++;
			now=nxt;
		}
		if(cnt>=2)ret+=cnt;
	}
	return ret;
}

int main() {
	int T,S;
	scanf("%d",&T);
	for(S=1;S<=T;S++)printf("Case #%d: %d.000000\n",S,work());
	return 0;
}
