#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;
typedef pair<int,int> IP;
ll ns[1024];
ll D,K;

ll test(ll a, ll b, ll p)
{
	ll s = ns[0];
	for(int i=1; i<K; ++i) {
		s = (s*a+b)%p;
		if (s!=ns[i]) return -1;
	}
	return (s*a+b)%p;
}

vector<bool> primeVec;
vector<int> primes;

void genIsP(int n)
{
	primeVec.clear(); primeVec.resize(n+1, 1);

	primeVec[0]=primeVec[1]=0;
	int i;
	for(i=2; i*i<=n; ++i) {
		if (!primeVec[i]) continue;
		for(int j=i*i; j<=n; j+=i)
			primeVec[j] = 0;
	}
}

void genPrimes(int n)
{
	genIsP(n);
	primes.clear();
	primes.push_back(2);
	for(int i=3; i<=n; ++i) if (primeVec[i]) primes.push_back(i);
}
template<class T>
T mod(T a, T b)
{
	T r=a%b;
	if (r<0) r+=b;
	return r;
}
template<class T>
pair<T,T> egcd(T a, T b)
{
	if (a%b==0) return IP(0,1);
	pair<T,T> x=egcd(b,a%b);
	return make_pair(x.second, x.first-x.second*(a/b));
}
template<class T>
T modinv(T x, T p)
{
	return mod(egcd(x,p).first,p);
}

int main()
{
	genPrimes(1e7);

	int t;cin>>t;
	for(int a=1; a<=t ;++a) {
		cin>>D>>K;
		ll big=0;
		for(int i=0; i<K; ++i) cin>>ns[i], big=max(big, ns[i]);

		int cnt=0;
		ll get=-1;
		if (K<3) {
			if (K==2 && ns[0]==ns[1]) cnt=1, get=ns[0];
			else cnt=2;
		} else {
			ll x=ns[0], y=ns[1], z=ns[2];
			int dd=1;
			for(int i=0; i<D; ++i) dd*=10;
			for(int i=0; primes[i]<dd; ++i) {
				ll p = primes[i];
				if (p<=big) continue;

//				cout<<"modinv "<<y-x<<' '<<p<<' '<<modinv(y-x+p,p)<<'\n';
				ll a = mod((z-y)*modinv(y-x+p,p), p);
				ll b = mod(z-a*y, p);

//				cout<<"lol "<<a<<' '<<b<<'\n';

				ll q = test(a,b,p);
				if (q<0) continue;
				else if (q==get) continue;
				else {
//					cout<<"get "<<p<<' '<<q<<'\n';
					get = q;
					++cnt;
				}
			}
		}
		cout<<"Case #"<<a<<": ";
		if (cnt==1) {
			cout<<get;
		} else {
			cout<<"I don't know.";
		}
		cout<<'\n';
	}
}
