#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define For(i,b) for(int i = 0; i < (int)b; ++i)
#define Fori(i,a,b) for(int i = a; i < (int)b; ++i)
#define All(t) t.begin(),t.end()
#define Fill(a,b) memset(a,b,sizeof(a))
#define Forstl(it,x) for(typeof(x.begin()) it=x.begin(); it!=x.end(); ++it)
#define db(x) cout << #x << " = " << x << endl
#define mod(A, B) ((((A) % (B)) + (B)) % (B))
#define Exist(container, element) (container.find(element) != container.end())
#define sz(a) int((a).size())
#define ARRSIZE(x) (sizeof(x)/sizeof(x[0]))
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<string> vs;

string itos (int i) {stringstream s; s << i; return s.str();}
int stoi (string s) {istringstream in(s); int ret; in >> ret; return ret;}

template <class T>
void out(vector<T> v)
{
  cout << "{";
  For(_i,v.size()) {if(_i) cout<<","; cout<<v[_i];}
  cout<<"}"<<endl;
}

ll extendedEuclid(ll a, ll b, ll & x, ll &  y)
{
    if(a == 0)
    {
        x = 0;
        y = 1;
        return b;
    }
    ll x1, y1;
    ll res = extendedEuclid(b % a, a, x1, y1);
    x = y1 - (b / a) * x1;
    y = x1;
    return res;
}

ll gcd(ll x, ll y)
{
    return x ? gcd(y%x, x) : y;
}

ll f(ll x, ll n)
{
	return n * ((x + n - 1LL) / n);
}
int main ()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int T, N;
	ll a, b, c, x, y, res;
	cin >> T;
	For(tests, T)
	{
		cin >> N;
		vector<ll>a(N);
		For(i, N) cin >> a[i];
		sort(All(a));
		vector<ll> dif;
		For(i, N - 1) dif.push_back(a[i + 1] - a[i]);
		ll d = 0;
		For(i, N - 1) d = gcd(d, dif[i]);
		ll t = f(a[N - 1], d);
		ll res = t - a[N - 1];
		printf("Case #%d: %lld\n", tests + 1, res);
	}
	return 0;
}
