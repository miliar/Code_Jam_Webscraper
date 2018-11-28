#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
template<class T> void maz(T &a,T b) {if(b>a)a=b;}

const int NMAX=1000;

int N,W,H,r[NMAX],ansx[NMAX],ansy[NMAX];

bool cmp(int a,int b) {
	return r[a]>r[b];
}

void solve() {
	static int a[NMAX];
	int i,j,k,u; bool f=false;
	if(W<H){f=true;swap(W,H);}
	for(i=0;i<N;i++)a[i]=i;
	sort(a,a+N,cmp);
	int Y=0,up=0;
	for(i=0;i<N;i=j) {
		int X=0,R=0;
		for(j=i;j<N;j++) {
			u=a[j];
			if(j!=i)X+=r[u];
			if(X>W)break;
			ansx[u]=X;
			X+=r[u];
			maz(R,r[u]);
		}
		if(i)Y+=up+R;
		up=R;
		for(k=i;k<j;k++)ansy[a[k]]=Y;
	}
	for(i=0;i<N;i++) {
		if(ansx[i]>W||ansy[i]>H) {
			fprintf(stderr,"\n@_@ %d>%d || %d>%d\n",ansx[i],W,ansy[i],H);
			exit(1);
		}
		if(f)swap(ansx[i],ansy[i]);
		printf(" %d %d",ansx[i],ansy[i]);
	}
}

void input() {
	int i;
	scanf("%d%d%d",&N,&W,&H);
	for(i=0;i<N;i++)scanf("%d",r+i);
}

int main() {
	int t,i;
	scanf("%d",&t);
	for(i=1;i<=t;i++) {
		input();
		printf("Case #%d:",i);
		solve();
		puts("");
	}
	return 0;
}
