#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <numeric>
#include <functional>
#include <algorithm>
#include <cmath>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)
#define dforn(i,n) for(int i=(n)-1;i>=0;i--)
#define dforsn(i,s,n) for(int i=(n)-1;i>=(int)(s);i--)

#define forall(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define dforall(i,c) for(typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)
#define all(c) (c).begin(),(c).end()

#define esta(x,c) ((c).find(x) != (c).end())
#define zMem(c) memset((c),0,sizeof(c))

typedef long long tint;
typedef long double tdbl;

typedef pair<int,int> pint;
typedef pair<tint,tint> ptint;

typedef vector<int> vint;
typedef vector<vint> vvint;
typedef vector<string> vstr;

const tdbl phi = (tdbl(1.0) + tdbl(sqrt(5.0))) / tdbl(2.0);

int main()
{
	stdin = freopen("c.in","r",stdin);
	stdout = freopen("c.out","w",stdout);
	int totalCasos;
	cin >> totalCasos;
	forn(caso,totalCasos)
	{
		tint a1,a2,b1,b2;
		cin >> a1 >> a2 >> b1 >> b2;
		tint res = 0;		
		for(tint a = a1; a<=a2;a++)
		{
			tint cuenta = 0;
			tint maxb = phi * tdbl(a);
			maxb = min(maxb,b2);
			tint minb = max(a+1,b1);
			if (maxb >= minb)
			{
				//cerr << "a->" << maxb - minb+1 << endl;
				cuenta += maxb - minb+1;
			}
			minb = tint(tdbl(a) / phi + tdbl(1.0));
			minb = max(minb,b1);
			maxb = min(a,b2);
			if (maxb >= minb)
			{
				//cerr << "b->" << maxb - minb+1 << endl;
				cuenta += maxb - minb+1;
				
			}
			res += (b2-b1+1) - cuenta;
			//cerr << (b2-b1+1) - cuenta << endl;
		}
		//cerr << "*" << endl;
		cout << "Case #" << caso + 1 << ": " << res << endl;
		//cerr << "Case #" << caso + 1 << ": " << res << endl;
	}
	return 0;
}


