#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <numeric>
using namespace std;
#define forn(i,n) for(int i=0; i<int(n); i++)
#define forsn(i,s,n) for(int i=(s); i<int(n); i++)
#define dforn(i,n) for(int i = int(n) - 1; i >= 0; i--)
#define forall(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define dforall(i,c) for(__typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)
#define all(c) (c).begin(), (c).end()
#define esta(v,c) ((c).find(v) != (c).end())
#define zMem(c) memset((c), 0, sizeof(c))
#define pb push_back
#define x first
#define y second
#define INF 1000000000
typedef long long tint;
typedef long double tdbl;
typedef vector<int> vint;
typedef vector<vint> vvint;
typedef pair<int,int> pint;
typedef pair<tdbl,tdbl> pdbl;

tdbl sqr(tdbl x)
{
	return x*x;
}

tdbl f(tdbl r, tdbl d)
{
	return r*r*(asin(1.0) - asin(d/r) - sqrt(1-sqr(d/r))*d/r);
}

/*tdbl max(tdbl x, tdbl y)
{
	return (x<y) ? y : x;
}
tdbl min(tdbl x, ydbl y)
{
	return (x<y) ? x : y;
}*/

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D.out","w",stdout);
	int TT; cin >> TT;
	forn(tt,TT)
	{
		int N, M; cin >> N >> M;
		pdbl p,q,d;
		cin >> p.x >> p.y >> q.x >> q.y; if(p.x > q.x) swap(p,q);
		d.x = q.x-p.x, d.y = q.y-p.y;
		cout << "Case #" << tt+1 << ":";
		forn(rep,M)
		{
			pdbl pto;
			cin >> pto.x >> pto.y; //cout << pto.x << " " << pto.y << endl;
			tdbl a = d.y/d.x, b = p.y - a*p.x;
			tdbl c = -d.x/d.y, d = pto.y - c*pto.x;
			pdbl pete ( (d-b)/(a-c), a*(d-b)/(a-c) + b );
			tdbl r1 = sqrt(sqr(p.x - pto.x) + sqr(p.y - pto.y));
			tdbl dis1 = sqrt(sqr(p.x - pete.x) + sqr(p.y - pete.y)); //cout << endl << r1 << " " << dis1 << endl;
			tdbl r2 = sqrt(sqr(q.x - pto.x) + sqr(q.y - pto.y));
			tdbl dis2 = sqrt(sqr(q.x - pete.x) + sqr(q.y - pete.y));
			if(pete.x < p.x) printf(" %.7lf", double(r1*r1*4*atan(1.0)-f(r1,dis1)+f(r2,dis2)));
			else if(q.x < pete.x) printf(" %.7lf", double(f(r1,dis1)+r2*r2*4*atan(1.0)-f(r2,dis2)));
			else printf(" %.7lf", (double)f(r1,dis1)+(double)f(r2,dis2));
		}
		cout << endl;
	}
	
	return 0;
}
