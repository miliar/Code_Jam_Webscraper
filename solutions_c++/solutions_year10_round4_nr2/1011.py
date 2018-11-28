//{{{ Includes and typedefs
#include <iostream>
#include <algorithm>
#include <utility>
#include <fstream>
#include <set>
#include <string.h>
#include <gmpxx.h>
using namespace std;

typedef long long ll;
typedef mpz_class zz;
typedef mpq_class qq;
typedef mpf_class ff;
//}}}
// {{{ Constructs
#define START           int main (void) {                           \
                            ifstream in;                            \
                            in.open(INFILE);

#define END                 in.close();                             \
                            return 0;                               \
                        };                      

#define CASESTART       long CASES;                                 \
                        in >> CASES;                                \
                        for (long CCCC=1; CCCC<=CASES; CCCC++) {

#define CASEEND         };

#define CASERESULT(x)  cout << "Case #" << CCCC << ": " << x << "\n"

#define FORL(i,N)      for (ll i=0; i<(ll)N; i++)
#define FOR1(i,N)      for (ll i=1; i<=(ll)N; i++)
// }}}

#define INFILE "B-small-attempt0.in"

ll pow(ll base, ll exp) {
    if(exp==0) return 1;
    else return base*pow(base, exp-1);
};

START
CASESTART
    ll i,j;
    ll P;
    ll total=0;


    in >> P;
    ll length=pow(2,P);
    ll M[length];
    for (i=0; i<length; i++) in >> M[i];

    for (i=0; i<P; i++) { //round
        ll skip=pow(2,i); 
        for(j=0; j<length; j+=skip*2) {
            ll price; in >> price;
            if(M[j] <= 0 || M[j+skip] <= 0) {
                total+=price;
            };
            M[j]=min(M[j],M[j+skip])-1;
        };
    };

    CASERESULT(total);
CASEEND
END
