#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
template<class T> void maz(T &a,T b) {if(b>a)a=b;}

const int NMAX=10000;

int N;
int d[NMAX+1],l[NMAX+1];
int z[NMAX+1];

bool solve() {
	int i,j;
	z[0]=d[0];
	for(i=0;i<N;i++) {
		//printf("z[%d]=%d\n",i,z[i]);
		if(i==N-1)break;
		for(j=i+1;j<N;j++) {
			if(d[j]>d[i]+z[i])break;
			maz(z[j],min(l[j],d[j]-d[i]));
		}
	}
	return z[i]>=0;
}

void input() {
	scanf("%d",&N);
	for(int i=0;i<N;i++)scanf("%d%d",d+i,l+i);
	l[N]=0;
	scanf("%d",d+N++);
	memset(z,0xff,N*sizeof(int));
}

int main() {
	int t,i;
	scanf("%d",&t);
	for(i=1;i<=t;i++) {
		input();
		printf("Case #%d: ",i);
		puts(solve()?"YES":"NO");
	}
	return 0;
}
