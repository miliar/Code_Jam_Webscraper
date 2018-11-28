
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <set>
#include <map>
#include <iomanip>
#include <cmath>
#include <string>
#include <vector>
#include <complex>
#include <stack>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

#define all(v)     ((v).begin()), ((v).end())
#define sz(v)      ((int)((v).size()))
#define clr(v, d)     memset(v, d, sizeof(v))
#define repa(v)   for(int i=0;i<(sz(v));++i) for(int j=0;j<(sz(v[i]));++j)
#define rep(i, v)      for(int i=0;i<(sz(v));++i)
#define lp(i, cnt)     for(int i=0;i<(cnt);++i)
#define lpi(i, s, cnt) for(int i=(s);i<(cnt);++i)
#define P(x)     cout<<#x<<" = { "<<x<<" }\n"
#define MP make_pair

typedef long long ll;
const int OO = (int)1e8;        // Note: Small->WRONG, Large->OVERFLOW

const double PI  = acos(-1);
const double EPS = (1e-8);


int dcmp(double a, double b) {
        return fabs(a-b) <= EPS ? 0 : a < b ? -1 : 1;   }

typedef complex<double> point;
#define X real()
#define Y imag()
#define angle(a)                (atan2((a).imag(), (a).real()))
#define vec(a,b)                ((b)-(a))
#define same(p1,p2)             (dp(vec(p1,p2),vec(p1,p2)) < EPS)
#define dp(a,b)                 ( (conj(a)*(b)).real() )
#define cp(a,b)                 ( (conj(a)*(b)).imag() )
#define length(a)               (hypot((a).imag(), (a).real()))
#define normalize(a)            (a)/length(a)
#define polar(r,ang)            ((r)*exp(point(0,ang)))
#define rotateO(p,ang)          ((p)*exp(point(0,ang)))
#define rotateA(p,angle,about)  (rotateO(vec(about,p),ang)+about)

int ccw( point p0, point p1, point p2 ) {
        point v1(p1-p0), v2(p2-p0);
        if ( cp(v1, v2) > +EPS)                         return +1;
        if ( cp(v1, v2) < -EPS)                         return -1;
        if (v1.X*v2.X < -EPS || v1.Y*v2.Y < -EPS)
                return -1;
        if ( norm(v1) < norm(v2)-EPS )  return +1;
        return  0;
}


bool intersect(point p1, point p2, point p3, point p4) {
        bool x = (p1 == p2), y = (p3==p4);
        if(x && y)      return p1 == p3;
        if(x)           return ccw(p3, p4, p1) == 0;
        if(y)           return ccw(p1, p2, p3) == 0;

        return  ccw(p1, p2, p3) * ccw(p1, p2, p4) <= 0  &&
                        ccw(p3, p4, p1) * ccw(p3, p4, p2) <= 0;
}

int main()
{

#ifndef ONLINE_JUDGE
freopen("a.txt", "rt", stdin);
freopen("b.txt", "wt", stdout);
#endif

	int t;scanf("%d",&t);
	for(int ii = 0 ; ii < t; ii ++)
	{
		cout<<"Case #"<<ii+1<<": ";
		vector<pair<point ,point> >vpp;
		int n;scanf("%d",&n);
//		point p1,p2;
		for (int i = 0; i < n; ++i) {
			int y1,y2;
			//p1.x = 1 , p2.x = 10;
			scanf("%d%d",&y1,&y2);
			point p1(1,y1),p2(10,y2);
			vpp.push_back(make_pair(p1,p2));

		}
	int res = 0 ;
		for (int i = 0; i < vpp.size(); ++i) {
			for (int j = i+1; j < vpp.size(); ++j) {
				if(intersect(vpp[i].first , vpp[i].second , vpp[j].first,vpp[j].second))
					res++;
			}
		}
		cout<<res<<endl;
	}

	return 0;
}
