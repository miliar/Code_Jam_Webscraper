#include <cstdio>
#include <cstring>
#include <set>

typedef long long ll;

const int LARGENUMBER=1000000+100;
int p[LARGENUMBER], rank[LARGENUMBER];

void make_set() {
	for(int i=0;i<LARGENUMBER;++i)
		p[i]=i, rank[i]=0;
}

void link(int x, int y) {
	if(rank[x]>rank[y]) {
		p[y]=x;
	} else {
		p[x]=y;
		if(rank[x]==rank[y])
			rank[y]++;
	}
}

int findset(int x) {
	if(x!=p[x])
		p[x]=findset(p[x]);
	return p[x];
}

void setunion(int x, int y) {
	link(findset(x),findset(y));
}

bool prime[LARGENUMBER];

typedef std::set<int> si;
typedef si::iterator siter;

int main() {
	// Prime sieve
	memset(prime, true, sizeof(prime));
	prime[0]=prime[1]=false;
	for(int i=2;i<LARGENUMBER;++i)
		if(prime[i])
			for(int j=2*i;j<LARGENUMBER;j+=i)
				prime[j]=false;
	int C;
	ll A,B,P;
	scanf("%d",&C);
	for(int c=0;c<C;++c) {
		scanf("%lld%lld%lld",&A,&B,&P);
		make_set();
		for(int p=P;p<=B-A;++p) {
			if(prime[p]) {
				for(ll a=A+(A%p==0?0:p-A%p);a+p<=B;a+=p)
					setunion(a-A, a+p-A);
			}
		}
		si sets;
		for(ll i=0;i<=B-A;++i)
			sets.insert(findset(i));
		printf("Case #%d: %d\n",c+1, (int)sets.size());
	}
}