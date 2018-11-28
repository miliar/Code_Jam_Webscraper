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

const int MAX_W = 1024;
const int MAX_G = 1000;
double yy[2][MAX_W];
double cut[MAX_G];

inline double get_dy(int x)
{
    return yy[1][x]-yy[0][x];
}

inline double trap_area(double dx, double dy1, double dy2)
{
    return dx*.5*(dy1+dy2);
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
        int W, L, U, G;
        cin >> W >> L >> U >> G >> skip_endl;
        assert(W <= MAX_W);
        assert(W >= 1);
        assert(L >= 2);
        assert(U >= 2);
        assert(G >= 2);
        forN ( s, 2 ) {
            int N = s? U: L;
            int ppx, ppy;
            cin >> ppx >> ppy >> skip_endl;
            assert(ppx == 0);
            forN ( i, N-1 ) {
                int px, py;
                cin >> px >> py >> skip_endl;
                forNF ( x, ppx, px ) {
                    double y = ppy + (py-ppy)/double(px-ppx)*(x-ppx);
                    yy[s][x] = y;
                }
                ppx = px;
                ppy = py;
            }
            assert(ppx == W);
            yy[s][W] = ppy;
        }
        
        // error check
        if ( !cin ) { cout << "Error parsing input" << endl; return 1; }
        // main code

        double area = 0;
        forN ( x, W ) area += trap_area(1, get_dy(x), get_dy(x+1));

        double x = 0, dy = get_dy(0);
        forN ( i, G ) {
            double more_a = area/G;
            while ( more_a > 0 ) {
                int px = int(x), nx = px+1;
                double ndy = get_dy(nx);
                double w = nx-x;
                double ra = trap_area(w, dy, ndy);
                if ( ra > more_a ) {
                    double dx;
                    if ( abs(ndy-dy) < 1e-9 ) {
                        dx = w*more_a/ra;
                    }
                    else {
                        double a = (ndy-dy)/(2*w);
                        double b = dy;
                        double c = -more_a;
                        double D = b*b-4*a*c;
                        if ( D <= 0 ) D = 0;
                        dx = (-b+sqrt(D))/(2*a);
                        //TR(a|b|c);
                    }
                    x = x+dx;
                    //TR(px|x|nx);
                    assert(x >= px && x <= nx);
                    dy = dy+dx/w*(ndy-dy);
                    break;
                }
                more_a -= ra;
                x = nx;
                dy = ndy;
            }
            cut[i] = x;
        }
        //TR(cut[G-1]|W);
        assert(abs(cut[G-1]-W)<1e-7);

        // output
        cout << "Case #"<<nc+1<<":";
        forN ( i, G-1 ) {
            cout << endl << fixed << setprecision(6) << cut[i];
        }
        cout << endl;
    }
}
