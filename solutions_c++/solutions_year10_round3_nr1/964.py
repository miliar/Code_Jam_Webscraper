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

class Point
{
	public:
		double x, y;
		Point(double xx = -1,double yy = -1)
		{
			x = xx; y = yy;
		}
};

// check whether segments intersect or not

// [(sx,sy), (ex,ey)] - segment, (pointx,pointy) - point

// on what side of the segment does the point lie on?

int side(double sx, double sy, double ex, double ey, double pointx, double pointy)

 { /* determine the side that the points lie on */
 double dx, dy;
 double px, py;
 double t;

 dx = ex - sx;
 dy = ey - sy;

 px = pointx - sx;
 py = pointy - sy;

 /* take cross-product */
 t = dx * py - dy * px;

 if (t > 0.00001) return 0; /* "left" side */
 if (t < -0.00001) return 1; /* "right" side */
 return 2; /* on the line */
 }

// if the one segment is inside the other or the intersection point lies on one
// of the segments like T, the function returns 1
int check_intersect(Point p1, Point p2, Point q1, Point q2)
 { /* do (p1,p2) and (q1,q2) intersect? */
 double sx, sy;
 double ex, ey;

 sx = p1.x;
 sy = p1.y;
 ex = p2.x;
 ey = p2.y;

 if (side(sx, sy, ex, ey, q1.x, q1.y) == side(sx, sy, ex, ey, q2.x, q2.y))
 /* are the q1 and q2 on the same side of (p1,p2)? */
 return 0; /* if so, the segments don't intersect */

 sx = q1.x;
 sy = q1.y;
 ex = q2.x;
 ey = q2.y;

 if (side(sx, sy, ex, ey, p1.x, p1.y) == side(sx, sy, ex, ey, p2.x, p2.y))
 /* are p1 and p2 on the same side of (q1,q2) */
 return 0; /* if so, the segments don't intersect */
 /* the endpoints of each segment are on opposite sides of
 the other segment. Therefore, they intersect */
 return 1;
 }
 
class S
{
	public:
		Point a, b;
		S()
		{
			a = Point();
			b = Point();
		}
};

int main ()
{
	freopen("A-large(2).in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int T;
	cin >> T;
	For(tests, T)
	{
		int n, a, b;
		cin >> n;
		vector<S> v(n);
		For(i, n)
		{
			cin >> a >> b;
			v[i].a = Point(0, a);
			v[i].b = Point(100, b);
		}
		int res = 0;
		For(i, n)
		{
			Fori(j, i + 1, n)
			{
				if(check_intersect(v[i].a, v[i].b, v[j].a, v[j].b))
				{
					++res;
				}
			}
		}
		printf("Case #%d: %d\n", tests + 1, res);
	}
	return 0;
}
