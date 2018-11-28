
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>

#include <cmath>

#define rep(I,N) for (int I=0; I<(N); I++)
#define rep2(I,B,E) for (int I=(B); I<=(E); I++)
#define repb(I,B,E) for (int I=(E); I>=(B); I--)

#define EPSILON 1E-6
#define eqr(A,B) (fabs( (A)-(B) ) < EPSILON)
#define ler(A,B) ( eqr(A,B) || (A)<(B) )
#define ger(A,B) ( eqr(A,B) || (A)>(B) )
#define MAXS 1001

using namespace std;

int l,n,c;
long t;
int A[MAXS];
int tmp[1000001];

long solve() {
    long time=0;
    int i=0;
    for (int star=0; star<n; star++) {
        int currdist = A[star % c];
        if (time < t) {
            long t2 = time + 2*currdist;
            if (t2 > t) {
                time = t;
                currdist = (t2-t)/2;
            } else {
                time = t2;
                continue;
            }
        }
        tmp[i++] = currdist;        
    }
    sort(tmp, tmp+i);
    repb(j,0,i-1) {
        if (l>0) {
            time += tmp[j];
            l--;
        } else {
            time += 2*tmp[j];
        }
    }
    return time;
}

int main() {
    int T;
    scanf("%i",&T);
    rep2(tc,1,T) {
        scanf("%i %i %i %i", &l, &t, &n, &c);
        rep(i,c) {
            scanf("%i", &A[i]);
        }
        printf("Case #%i: %i\n", tc, solve());
    }
}
