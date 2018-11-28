#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <list>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <cstdio>
#include <ctime>
using namespace std;

#define fori(i, n) for ( typeof(n) i = 0; i < (n); ++i )
#define forr(i, a, b) for ( typeof(a) i = (a); i <= (b); ++i )
#define ford(i, a, b) for ( typeof(a) i = (a); i >= (b); --i )
#define tr(T, i) for ( typeof(T.begin()) i = T.begin(); i != T.end(); ++i )
#define sz size()
#define all(x) (x).begin(),(x).end()
#define _sort(x) sort(all(x))

template<class T> string a2s(T x) { ostringstream o; o << x; return o.str(); }
template<class T> T s2a(string s) { istringstream i(s); T x; i >> x; return x; }

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;

const double EPS = 1e-9;

#define TRACE(x...)
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x" = " << x << "\n")

int cmp( double x, double y = 0, double tol = EPS )
{
    return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

long long base(long long a, int base)
{
	if ( base == 10 ) return a;
	long long asw = 0;
	string s = "";
	
	while ( a != 0 )
	{
		s += a2s(a%base);
		a /= base;
	}

	reverse(all(s));
	asw = s2a<int>(s);
	
	return asw;
}

ll base10(ll a, int base)
{
	ll asw = 0;
	string s = a2s(a);
	
	for(int i = s.sz-1; i >= 0; --i)
	{
		asw += (s[i]-'0') * (ll) pow( (double)(base), (int)(s.sz-1-i) );
	}

	return asw;
}

int main()
{
    int N;
    cin >> N;

    fori(cas, N)
    {
        string s;
        cin >> s;

		ll asw = numeric_limits<ll>::max();

		set<char> S;

		fori(i,s.sz) S.insert(s[i]);
		int n = S.sz;

		vector<int> v(10, 0);
		for( int i = 10-n; i < 10; ++i )
		{
			v[i] = 1;
		}

 		map<char, char> M;

		set<char>::iterator it;
		do
		{
			vector<int> vv;
			int minbase = 2;
			fori(i,v.sz)
			{
				if(v[i] == 1)
				{
					vv.push_back(i);
					minbase = max(minbase, (int)(i+1));
				}
			}
				
			do
			{
				it = S.begin();
				fori(i,vv.sz)
				{
					M[*it] = vv[i] + '0';
					++it;
				}
			
				string s1 = s;
				fori(i,s.sz)
				{
					s1[i] = M[s[i]];
				}
				if(s1[0] == '0') continue;

				ll num = s2a<ll>(s1);

// 				tr(M, itt)
// 				{
// 					cout << itt->first << " " << itt->second << endl;
// 				}
				WATCH(s);
				WATCH(s1);
				
				forr(i, minbase, 10)
				{
					ll calc = base10(num, i);

					if ( calc < asw )
					{
						asw = calc;
					}
				}

			} while(next_permutation(all(vv)));
					
		} while(next_permutation(all(v)));

        cout << "Case #" << cas+1 << ": ";
        cout << asw << endl;
    }

    return 0;
}
