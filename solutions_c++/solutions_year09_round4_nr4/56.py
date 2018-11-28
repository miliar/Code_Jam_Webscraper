#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <cmath>
#include <complex>
#include <numeric>
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

typedef complex<double> P;
int N;
const int MAX_N = 40;
int xx[MAX_N];
int yy[MAX_N];
P pp[MAX_N];
int rr[MAX_N];

int xx1[MAX_N];
int yy1[MAX_N];
P pp1[MAX_N];
int rr1[MAX_N];

P side_center(P p1, P p2, int r1, int r2, double r)
{
    double d1 = r-r1;
    double d2 = r-r2;
    P dp = p2-p1;
    double d = abs(dp);
    if ( d >= d1+d2 ) return P(1e9, 1e9);
    double rd = 1/d;
    double a = d*.5 + (d1*d1-d2*d2)*rd*.5;
    if ( a < 0 || a > d ) return P(1e9, 1e9);
    double s = sqrt(d1*d1-a*a);
    return p1 + dp*rd*P(a, s);
}

bool covers(double r)
{
    if ( N <= 2 ) return r >= rr[0];
    forN ( i, N ) forN ( j, N ) {
        if ( j == i ) continue;
        P p = side_center(pp[i], pp[j], rr[i], rr[j], r);
        if ( p.real() > 1e8 ) continue;
        TR(pp[i]|rr[i]);
        TR(pp[j]|rr[j]);
        TR(r|p);
        assert(abs(abs(p-pp[i])-(r-rr[i])) < 1e-9);
        assert(abs(abs(p-pp[j])-(r-rr[j])) < 1e-9);
        int M = 0;
        forN ( i, N ) {
            if ( abs(pp[i]-p) > r-rr[i]+1e-9 ) {
                pp1[M] = pp[i];
                rr1[M] = rr[i];
                ++M;
            }
        }
        TR(M);
        if ( M <= 1 ) return 1;
        forN ( i, M ) forN ( j, M ) {
            if ( j == i ) continue;
            P p = side_center(pp1[i], pp1[j], rr1[i], rr1[j], r);
            if ( p.real() > 1e8 ) continue;
            forN ( i, M ) {
                if ( abs(pp1[i]-p) > r-rr1[i]+1e-9 ) {
                    goto bad;
                }
            }
            return 1;
        bad:;
        }
    }
    return 0;
}

int main()
{
    //init_table();

    int num_cases = 1;
    cin >> num_cases >> skip_endl;

    forN ( nc, num_cases ) {
        // parse input
        cin >> N >> skip_endl;
        forN ( i, N ) {
            cin >> xx[i] >> yy[i] >> rr[i] >> skip_endl;
            pp[i] = P(xx[i], yy[i]);
        }

        // error check
        if ( !cin ) cout << "Error parsing input" << endl;
        // main code

        double min = *max_element(rr,rr+N), max = 2000;
        while ( max - min > .3e-6 ) {
            double r = (max+min)*.5;
            if ( covers(r) )
                max = r;
            else
                min = r;
        }
        double out = (min+max)*.5;

        // output
        cout << "Case #"<<nc+1<<": ";
        cout << fixed << out;
        cout << endl;
    }
}
