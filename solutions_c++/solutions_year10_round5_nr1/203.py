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

int D, K;
int vv[10];
int dd[10];

const int MAX_P = 10010001;
int NP;
int pp[MAX_P];
bool cc[MAX_P];

void make_primes()
{
    cc[0] = cc[1] = 0;
    for ( int i = 2; i < MAX_P; ++i ) {
        if ( !cc[i] ) {
            pp[NP++] = i;
            for ( int j = i*2; j < MAX_P; j += i )
                cc[j] = 1;
        }
    }
    TR(NP|pp[NP-1]);
}


template<typename Int> struct extended_euclid {
    Int gcd, a, x, b, y; // gcd == gcd(a, b) == a*x+b*y
    extended_euclid(Int a_, Int b_) : gcd(a_), a(a_), x(1), b(b_), y(0)
    {
        if ( b != 0 ) {
            extended_euclid<Int> r(b, a%b);
            gcd = r.gcd;
            x = r.y;
            y = r.x-a/b*r.y;
        }
    }
};

inline int recip(int a, int p)
{
    extended_euclid<int> e(a, p);
    return e.gcd < 0? -e.x: e.x;
}

inline int next(int p)
{
    if ( K < 3 ) return -1;
    forNF ( i, 1, K-1 ) {
        assert(abs(dd[i]) < p);
    }
    int A = -1;
    forN ( i, K-2 ) {
        int d1 = dd[i+1], d0 = dd[i];
        int rd0 = recip(d0, p);
        int a = i64(d1)*rd0%p;
        if ( a < 0 ) a += p;
        //TR(p|i|a);
        if ( i == 0 ) {
            A = a;
            //TR(p|d0|d1|rd0|A);
        }
        else if ( a != A ) {
            return -1;
        }
    }
    int d = dd[K-2]*A % p;
    int v = (vv[K-1]+d)%p;
    if ( v < 0 ) v += p;
    //TR(p|A|d|v);
    return v;
}


int main(int /*argc*/, const char** /*argv*/)
{
    //NTR = 10000;
    int num_cases = 1;
    cin >> num_cases >> skip_endl;

    make_primes();

    forN ( nc, num_cases ) {
        // parse input
        cin >> D >> K >> skip_endl;
        assert(K <= 10);
        forN ( i, K ) {
            cin >> vv[i];
        }
        cin >> skip_endl;

        // error check
        if ( !cin ) cout << "Error parsing input" << endl;
        // main code

        int min_p = 1;
        forN ( i, D-1 ) min_p*=10;
        int max_p = min_p*10;
        min_p = 2;
        forNF ( i, 0, K ) min_p >?= vv[i] + 1;
        min_p = *lower_bound(pp, pp+NP, min_p);
        max_p = *(lower_bound(pp, pp+NP, max_p+1)-1);
        TR(D|A(vv,K)|min_p|max_p);

        int out = -1;

        forN ( i, K-1 ) dd[i] = vv[i+1]-vv[i];

        if ( K == 1 ) {
        }
        if ( 0 && K >= 2 && dd[K-2] == 0 ) {
            out = vv[K-1];
        }
        if ( 0 && out < 0 ) {
            forN ( i, K-1 ) {
                if ( vv[i] == vv[K-1] ) {
                    out = vv[i+1];
                    break;
                }
            }
        }
        if ( out < 0 && K == 2 && dd[0] == 0 ) {
            out = vv[1];
        }
        if ( 0 && out < 0 && K >= 3 ) {
            int s = -1;
            forN ( i, K-2 ) {
                if ( dd[i] == dd[i+1] ) {
                    s = i;
                    break;
                }
            }
            if ( s >= 0 ) {
                int d = dd[s];
                int p = min_p == max_p? min_p: -1;
                forN ( i, K-1 ) {
                    if ( dd[i] != d ) {
                        int x = abs(dd[i]-d);
                        assert(x >= min_p && x < max_p && !cc[x]);
                        assert(p == -1 || p == x);
                        p = x;
                    }
                }
                int v = vv[K-1] + d;
                if ( v >= 0 && v < min_p ) {
                    out = v;
                }
            }
        }
        if ( out < 0 ) {
            for ( int pi = lower_bound(pp, pp+NP, min_p)-pp; pp[pi] <= max_p; ++pi ) {
                int p = pp[pi];
                TR(p);
                int v = next(p);
                if ( v < 0 ) continue;
                if ( out < 0 ) {
                    out = v;
                    continue;
                }
                if ( v == out ) continue;
                out = -1;
                break;
            }
        }

        if ( 0 ) {
            int o = -1;
            if ( K > 1 ) {
                for ( int pi = lower_bound(pp, pp+NP, min_p)-pp; pp[pi] <= max_p; ++pi ) {
                    int p = pp[pi];
                    forN ( A, p ) {
                        int B = (vv[1] - i64(vv[0])*A) % p;
                        if ( B < 0 ) B += p;
                        int s = vv[0];
                        forNF ( i, 1, K ) {
                            s = (i64(s)*A+B)%p;
                            assert(i > 1 || s == vv[1]);
                            if ( vv[i] != s ) {
                                s = -1;
                                break;
                            }
                        }
                        if ( s < 0 ) continue;
                        s = (i64(s)*A+B)%p;
                        if ( o >= 0 && o != s ) {
                            TR(p|A|B|s|o);
                            o = -1;
                            goto done;
                        }
                        o = s;
                    }
                }
            done:;
            }
            else {
                o = -1;
            }
            TR(out|o);
            if ( out != o ) {
                NTR >?= 100;
                TR(D|A(vv,K)|out|o);
            }
            assert(out == o);
        }
        
        // output
        cout << "Case #"<<nc+1<<": ";
        if ( out < 0 )
            cout << "I don't know.";
        else
            cout << out;
        cout << endl;
    }
}
