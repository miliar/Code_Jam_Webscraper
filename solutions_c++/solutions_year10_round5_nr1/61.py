#include <stdio.h>
#include <string.h>

#define MAX 100000

int primes[MAX];
int cnt;

inline bool IsPrime(int n) {
	for(int r=2;r*r<=n;++r)
		if(!(n%r))
			return false;
	return true;
}

void GenPrimes() {
	for(int i=2;i<1000000;++i) {
		if(IsPrime(i))
			primes[cnt++]=i;
	}
}

void euclid(int a,int b,int &x,int &y) {
	if(!b) {
		x=1, y=0;
		return;
	}
	int xx,yy;
	euclid(b,a%b,xx,yy);
	x=yy, y=xx-(a/b)*yy;
}

inline int inv(int a,int p) {
	int x,y;
	a%=p;
	if(a<0) a+=p;
	euclid(a,p,x,y);
	return x;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	GenPrimes();
	int tests;
	scanf("%d",&tests);
	for(int test=1;test<=tests;++test) {
		int d,n;
		int x[20];
		scanf("%d%d",&d,&n);
		for(int i=0;i<n;++i)
			scanf("%d",&x[i]);
		printf("Case #%d: ",test);
		if(n==1) {
			printf("I don't know.\n");
			continue;
		}
		if(n==2) {
			if(x[0]==x[1])
				printf("%d\n",x[0]);
			else
				printf("I don't know.\n");
			continue;
		}
		if(x[0]==x[1]) {
			for(int i=2;i<n;++i)
				if(x[i]!=x[0])
					printf("BUG\n");
			printf("%d\n",x[0]);
			continue;
		}
		int m=1,ans=-1;
		for(int i=0;i<d;++i,m*=10);
		bool found=false;
		bool ambiguous=false;
		for(int i=0;i<cnt;++i) {
			int p=primes[i];
			if(p>m) break;
			bool ok=true;
			for(int i=0;i<n;++i)
				if(x[i]>=p) {
					ok=false;
					break;
				}
			if(!ok) continue;
			int a=((long long)(x[2]-x[1])*inv(x[1]-x[0],p))%p;
			int b=(x[1]-(long long)a*x[0])%p;
			for(int i=3;i<n;++i) {
				int t=((long long)a*x[i-1]+b)%p;
				if((x[i]-t)%p) {
					ok=false;
					break;
				}
			}
			if(ok) {
				int t=((long long)a*x[n-1]+b)%p;
				if(t<0) t+=p;
				if(found) {
					if(ans!=t) {
						ambiguous=true;
						break;
					}
				}
				found=true;
				ans=t;
			}
		}
		if(found && !ambiguous)
			printf("%d\n",ans);
		else
			printf("I don't know.\n");
	}
	return 0;
}
