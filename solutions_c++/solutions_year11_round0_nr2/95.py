#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstring>
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
#include <queue>
#include <tr1/unordered_map>
#include <tr1/unordered_set>

using namespace std;
using namespace tr1;

#define fori(i, n) for ( int i = 0; i < (n); ++i )
#define forr(i, a, b) for ( int i = (a); i <= (b); ++i )
#define ford(i, a, b) for ( int i = (a); i >= (b); --i )
#define tr(T, i) for (typeof(T.begin()) i = T.begin(); i != T.end(); ++i )
#define sz size()
#define all(x) (x).begin(),(x).end()
#define _sort(x) sort(all(x))
#define pb push_back

#define TRACE(x...) x
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x" = " << x << "\n")

template<class T> string a2s(T x) { ostringstream o; o << x; return o.str(); }
template<class T> T s2a(string s) { istringstream i(s); T x; i >> x; return x; }

const double EPS = 1e-9;
const int INF = 0x3F3F3F3F;

int cmpD(double x, double y = 0, double tol = EPS)
{
    return ( x <= y + tol ) ? ( x + tol < y ) ? -1 : 0 : 1;
}

int main()
{
	int t, c, d, n;
	char ch;
	string s, asw;
	cin >> t;
	forr(cas,1,t)
	{
		cin >> c;
		map< set< char >, char > sub;
		map< set< char >, char >::iterator it1;
		fori(i,c)
		{
			cin >> s;
			set< char > S;
			S.insert(s[0]);
			S.insert(s[1]);
			sub[S] = s[2];
		}
		
		cin >> d;
		set< set< char > > opp;
		set< set< char > >::iterator it2;
		fori(i,d)
		{
			cin >> s;
			set< char > S;
			S.insert(s[0]);
			S.insert(s[1]);
			opp.insert( S );
		}
		
		cin >> n;
		asw = "";
		fori(i,n)
		{
			cin >> ch;
			if ( asw.sz == 0 )
			{
				asw.append(1,ch);
			}
			else
			{
				set< char > S;
				S.insert(asw[asw.sz-1]);
				S.insert(ch);
				it1 = sub.find( S );
				if ( it1 != sub.end() )
				{
					asw = asw.substr(0, asw.sz-1);
					asw.append(1,it1->second);
				}
				else
				{
					bool limpou = false;
					fori(j,asw.sz)
					{
						set< char > S;
						S.insert(ch);
						S.insert(asw[j]);
						it2 = opp.find( S );
						if ( it2 != opp.end() )
						{
							asw = "";
							limpou = true;
							break;
						}
					}
					if ( !limpou ) asw.append(1,ch);
				}
			}
		}
		
		cout << "Case #" << cas << ": [";
		if ( asw.sz != 0 ) cout << asw[0];
		forr(i,1,(int)asw.sz-1) cout << ", " << asw[i];
		cout << "]" << endl;
	}
	return 0;
}

