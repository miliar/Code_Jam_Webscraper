#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

typedef long long int64;

vector<pair<int,int> > factorize(int x) {
	vector<pair<int,int> > f;
	if (x==1) { f.push_back(make_pair(1,1)); }
	for (int d=2;d*d<=x;d++) {
		if (x%d==0) {
			int k=0;
			while (x%d==0) { x/=d; k++; }
			f.push_back(make_pair(d,k));
		}
	}
	if (x!=1) f.push_back(make_pair(x,1));
	return f;
}

long long phi(int x) {
	if (x==1) return 1;
	vector<pair<int,int> > f = factorize(x);
	long long r = 1;
	for (int i=0;i<f.size();i++) {
		r*=(f[i].first-1);
		for (int j=0;j<f[i].second-1;j++) r*=f[i].first;
	}
	return r;
}

int modPow(int a, int k, int m) { // a^k (mod m)
	if (k==0) return 1;
	if (k%2==0) {
		int64 b=modPow(a,k/2,m);
		return (b*b)%m;
	} else {
		int64 b=modPow(a,k-1,m);
		return (a*b)%m;
	}
}

int modInv(int a, int m) { // 1/a = a^-1 = a^(phi(m)-1) (mod m)
	return modPow(a,phi(m)-1,m);
}


int gcd(int a, int b) {
	int c;
	if (a<b) swap(a,b);
	while (b!=0) { c=a%b; a=b; b=c; }
	return a;
}

int isPrime[1000001];
vector<int> primes;

void sieve(int n, bool getPrimeList) {
	long long i,f;
	primes.clear();
	isPrime[0]=0; isPrime[1]=0;
	for (i=2;i<=n;i++) isPrime[i]=1;

	for (i=2; (getPrimeList ? (i<=n) : (i*i<=n)); i++) {
		if (isPrime[i]==1) {
			primes.push_back(i);
			f=i;
			while (i*f<=n) { isPrime[i*f]=0; f++; }
		}
	}
}

int s[10];

int main() {
	//freopen("random.in","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	sieve(1000000,1);

	int tests;
	scanf("%d",&tests);
	for (int test=1;test<=tests;test++) {
		cerr << test << endl;
		printf("Case #%d: ",test);
		int d,k;
		scanf("%d %d",&d,&k);
		for (int i=0;i<k;i++) scanf("%d",&s[i]);
		if (k==1) {
			printf("I don't know.\n");
			continue;
		}
		if (k==2) {
			if (s[0]==s[1]) printf("%d\n",s[0]);
			else printf("I don't know.\n");
			continue;
		}
		int sol=-1;
		int64 a,b;
		for (int ip=0;ip<primes.size();ip++) {
			int p=primes[ip];
			if (p>pow(10,d)) break;

			int ok=1;
			for (int i=0;i<k;i++) {
				if (s[i]>=p) { ok=0; break; }
			}
			if (!ok) continue;

			int x=(s[2]-s[1]+p)%p, y=(s[1]-s[0]+p)%p;

			if (y==0) {
				if (x!=0) continue;
				else a=0;
			} else {
				if (gcd(y,p)!=1) continue;
				a=((int64)x*modInv(y,p))%p;
			}
			b=((s[1]-a*s[0])%p+p)%p;

			ok=1;
			for (int i=3;i<k;i++) {
				if (s[i]!=(s[i-1]*a+b)%p) { ok=0; break; }
			}
			if (ok) {
				//cout << p << " " << a << " " << b << endl;
				int sol2=(s[k-1]*a+b)%p;
				if (sol==-1 || sol==sol2) sol=sol2;
				else sol=-2;
			}
		}
		if (sol>=0) printf("%d\n",sol);
		else printf("I don't know.\n");
	}
    return 0;
}
