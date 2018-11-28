#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <cmath>
#include <numeric>
#include <algorithm>
#include <functional>
#include <cctype>
#include <sstream>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <gmp.h>
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
    TR(s);
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

const int INF = 999999999;
const int MAX_N = 1024;
int N, W, H;
pair<int, int> pp[MAX_N];
int rr[MAX_N];
double xx[MAX_N], yy[MAX_N];
double rxx[MAX_N], ryy[MAX_N];

static const double EPS = 1e-8;

double best_x, best_y;

void check(int i, double x, double y)
{
    TR(i|x|y);
    if ( x > best_x*(1+EPS) ) return;
    if ( x >= best_x*(1-EPS) && y >= best_y ) return;
    if ( x < 0 || x > W ) return;
    if ( y < 0 || y > H ) return;
    forN ( j, i ) {
        double d = hypot(x-xx[j], y-yy[j]);
        if ( d < (rr[i]+rr[j])*(1+EPS*.1) ) return;
    }
    best_x = x;
    best_y = y;
}

void place_clx(int i, int j, int lx)
{
    double bx = xx[j], by = yy[j];
    double br = rr[j]+rr[i];
    double dl = lx-bx;
    if ( abs(dl) > br ) return;
    br *= (1+EPS);
    double h = sqrt(br*br-dl*dl);
    check(i, lx, by-h);
    check(i, lx, by+h);
}

void place_cly(int i, int j, int ly)
{
    double bx = xx[j], by = yy[j];
    double br = rr[j]+rr[i];
    double dl = ly-by;
    if ( abs(dl) > br ) return;
    br *= (1+EPS);
    double w = sqrt(br*br-dl*dl);
    check(i, bx-w, ly);
    check(i, bx+w, ly);
}

void place_cc(int i, int j, int k)
{
    double bx = xx[j], by = yy[j];
    double br = rr[j]+rr[i];
    double cx = xx[k], cy = yy[k];
    double cr = rr[k]+rr[i];
    double dx = cx-bx, dy = cy-by;
    double dc = hypot(dx, dy);
    if ( dc > br+cr ) return;
    br *= (1+EPS);
    cr *= (1+EPS);
    double x = .5*(1+(br*br-cr*cr)/(dc*dc));
    assert(x >= 0 && x <= 1);
    double y = sqrt(1-(br/dc)*(br/dc));
    assert(y >= 0);
    check(i, bx+x*dx+y*dy, by+x*dy-y*dx);
    check(i, bx+x*dx-y*dy, by+x*dy+y*dx);
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
        cin >> N >> W >> H >> skip_endl;
        forN ( i, N ) { cin >> pp[i].first; pp[i].second = i; }
        cin >> skip_endl;

        // error check
        if ( !cin ) {
            cout << "Error parsing input" << endl;
            return 1;
        }
        // main code

        sort(pp, pp+N, greater<pair<int, int> >());
        forN ( i, N ) rr[i] = pp[i].first;
        TR(W|H|A(rr,N));
        forN ( i, N ) {
            best_x = W+1;
            best_y = H+1;
            check(i, 0, 0);
            check(i, 0, H);
            check(i, W, 0);
            check(i, W, H);
            forN ( j, i ) {
                place_clx(i, j, 0);
                place_clx(i, j, W);
                place_cly(i, j, 0);
                place_cly(i, j, H);
                forN ( k, j ) {
                    place_cc(i, j, k);
                }
            }
            TR(i|best_x|best_y);
            assert(best_x <= W);
            xx[i] = best_x;
            yy[i] = best_y;
        }

        forN ( i, N ) {
            rxx[pp[i].second] = xx[i];
            ryy[pp[i].second] = yy[i];
        }

        // output
        cout << "Case #"<<nc+1<<": ";
        forN ( i, N ) {
            cout << ' ' << setprecision(11) << rxx[i];
            cout << ' ' << setprecision(11) << ryy[i];
        }
        cout << endl;
    }
}
