#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <cmath>
#include <numeric>
#include <complex>
#include <algorithm>
#include <functional>
#include <cctype>
#include <sstream>
#include <iostream>
#include <iomanip>
#ifdef HOME_RUN
# include <debug.hpp>
# include <dump.hpp>
# include <cassert>
#else
# define TR(x) do{}while(0)
# ifdef assert
#  indef assert
# endif
# define assert(x) do{}while(0)
#endif
using namespace std;

#define ALL(C) (C).begin(), (C).end()
#define forIter(I,C) for(typeof((C).end()) I=(C).begin(); I!=(C).end(); ++I)
#define forNF(I,S,C) for(int I=(S); I<int(C); ++I)
#define forN(I,C) forNF(I,0,C)
#define forEach(I,C) forN(I,(C).size())
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef long long i64;
typedef unsigned long long u64;

inline istream& skip_endl(istream& in)
{
    string s;
    getline(in, s);
    forIter( i, s ) assert(isspace(*i));
    return in;
}

inline string get_str()
{
    string ret;
    getline(cin, ret);
    return ret;
}

map<string, int> str_index;
int get_index(const string& s)
{
    return str_index.insert(make_pair(s, str_index.size())).first->second;
}
int get_str_index()
{
    return get_index(get_str());
}

/////////////////////////////////////////////////////////////////////////////
typedef long double Coord;
typedef pair<Coord, Coord> Point;
typedef vector<Point> VP;
int _;
#define x first
#define y second

// Point operators
inline Point operator+(Point p1, Point p2)
{
    return Point(p1.x+p2.x, p1.y+p2.y);
}
inline Point operator-(Point p1, Point p2)
{
    return Point(p1.x-p2.x, p1.y-p2.y);
}
inline Point operator-(Point p)
{
    return Point(-p.x, -p.y);
}
inline Point operator*(Point p, Coord n)
{
    return Point(p.x*n, p.y*n);
}
inline Point operator/(Point p, Coord n)
{
    return Point(p.x/n, p.y/n);
}
inline Coord operator*(Point v1, Point v2)
{
    return v1.x*v2.x+v1.y*v2.y;
}
inline Coord operator/(Point v1, Point v2)
{
    return v1.x*v2.y-v1.y*v2.x;
}

// polygon area
Coord doubleArea(const VP& p)
{
     Coord area = 0;
     forEach ( i, p )
         area += p[i]/p[(i+1)%p.size()];
     return abs(area);
}
inline double area(const VP& pp)
{
    return doubleArea(pp)*.5;
}

// fast convex hull
struct ByArg // sort by angle around center point o
{
    ByArg(Point o_) : o(o_) {}
    Point o;
    inline bool operator()(Point a, Point b) const
    {
        a = a-o; b = b-o;
        if ( a/b ) return a/b < 0;
        return a*a < b*b;
    }
};
VP convexhull(VP p)
{
     VP ret;
     if ( !p.empty() ) {
         swap(p[0], *min_element(ALL(p)));
         sort(ALL(p), ByArg(p[0]));
         for ( size_t i = 0; i < p.size(); ++i ) {
             while ( ret.size() > 1 ) {
                 const Point& r = *(ret.end()-2);
                 if ( (ret.back()-r)/(p[i]-r) < 0 )
                     break;
                 ret.pop_back();
             }
             ret.push_back(p[i]);
         }
     }
     return ret;
}

/////////////////////////////////////////////////////////////////////////////

int N, M;
int xx[5000], yy[5000];
int bxx[1000], byy[1000];

double calc(int bx, int by)
{
    VP pp;
    Point bp(bx, by);
    pp.push_back(bp);
    map<Point, set<int> > pii;
    forN ( i, N ) {
        pii[bp].insert(i);
        Coord cx = bx-xx[i];
        Coord cy = by-yy[i];
        forN ( j, i ) {
            Coord dx = xx[j]-xx[i];
            Coord dy = yy[j]-yy[i];
            Coord a = (cx*dx+cy*dy)/(dx*dx+dy*dy);
            Coord mx = xx[i]+dx*a;
            Coord my = yy[i]+dy*a;
            Coord vx = mx*2-bx;
            Coord vy = my*2-by;
            bool inside = 1;
            forN ( k, N ) {
                if ( k == i || k == j ) continue;
                Coord rx = bx-xx[k];
                Coord ry = by-yy[k];
                Coord dx = vx-xx[k];
                Coord dy = vy-yy[k];
                if ( dx*dx+dy*dy > rx*rx+ry*ry ) {
                    inside = 0;
                    break;
                }
            }
            if ( inside ) {
                Point p(vx, vy);
                pp.push_back(p);
                pii[p].insert(i);
                pii[p].insert(j);
            }
        }
    }
    VP cp = convexhull(pp);
    if ( cp.size() <= 1 ) return 0;
    double a = area(cp);
    TR(cp|a);
    forEach ( i, cp ) {
        Point p1 = cp[i], p2 = cp[(i+1)%cp.size()];
        Point d = p2-p1;
        const set<int>& ii1 = pii[p1];
        const set<int>& ii2 = pii[p2];
        int best_j = -1;
        Coord best_p = 1e99;
        forIter ( k, ii1 ) {
            int j = *k;
            if ( !ii2.count(j) ) continue;
            Coord p = d/(Point(xx[j], yy[j])-p1);
            TR(j|d|p);
            if ( p < best_p ) {
                best_p = p;
                best_j = j;
            }
        }
        assert(best_j >= 0);
        int j = best_j;
        Point d1 = p1-Point(xx[j], yy[j]);
        Point d2 = p2-Point(xx[j], yy[j]);
        Coord r2 = d1*d1;
        TR(j|p1|p2|Point(xx[j],yy[j]));
        double alpha = acos((d1*d2)/r2);
        if ( best_p >= 0 ) alpha = 2*M_PI-alpha;
        TR(alpha|sqrt(r2)|r2*.5*(alpha-sin(alpha)));
        a += r2*.5*(alpha-sin(alpha));
    }
    TR(a);
    return a;
}

int main(int argc, const char** argv)
{
    int num_cases = 1;
    cin >> num_cases >> skip_endl;
    int part_cases = 0;
    if ( argc == 2 ) {
        part_cases = atoi(argv[1]);
    }
    
    forN ( nc, num_cases ) {
        // parse input
        cin >> N >> M >> skip_endl;
        
        forN ( i, N ) {
            cin >> xx[i] >> yy[i] >> skip_endl;
        }

        forN ( i, M ) {
            cin >> bxx[i] >> byy[i] >> skip_endl;
        }

        // error check
        if ( !cin ) cout << "Error parsing input" << endl;
        // main code

        // output
        cout << "Case #"<<nc+1<<":";

        forN ( i, M ) {
            cout << ' ' << fixed << setprecision(7) << calc(bxx[i], byy[i]);
        }

        cout << endl;
    }
}
