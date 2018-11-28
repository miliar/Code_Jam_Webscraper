#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <complex>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <complex>
#include <stack>
#include <memory.h>
#ifdef NEV_DEBUG
#include <ctime>
#endif
using namespace std;

const int SIZE = 10;
const double pi = 3.1415926535897932384626433832795;


typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int uint;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;
typedef LL matrix[SIZE][SIZE];
typedef complex<double> base;

#define sz size()
#define mp make_pair
#define pb push_back
#define ALL(a) (a).begin(), (a).end()
#define FOR(i,a,b) for(int i=(a),_b(b); i<_b; ++i)
#define RFOR(i,a,b) for(int i=(a)-1,_b(b); i>=_b; --i)
#define CLR(a,b) memset(a,b,sizeof(a))
#define CPY(a,b) memcpy(a,b,sizeof(a))
#define sqr(a) ((a)*(a))
#define MIN(a,b) ((a)<(b)?(a):(b))

char ch[1<<20];
string gs() {scanf("%s",ch); return string(ch);}
string gl() {gets(ch); return string(ch);}
template <class T>
T gcd(T a, T b) { return (!a)?b:gcd(b%a,a); }
void error(){ int yyy=0; cout << 7/yyy; }

int O[1024];
int X[1024];
int N;

void solve() {
    int A,B,N;
    VS a,b;
    scanf("%d",&A);
    FOR(i,0,A) a.pb(gs());
    scanf("%d",&B);
    FOR(i,0,B) b.pb(gs());
    scanf("%d",&N);
    string s=gs();

    int C[26]={0};
    string r;
    FOR(i,0,s.sz){
        r+=s[i];
        ++C[s[i]-'A'];
        if (r.sz>=2) FOR(j,0,a.sz) {
            if (a[j][0]==r[r.sz-2] && a[j][1]==r[r.sz-1] || 
                a[j][1]==r[r.sz-2] && a[j][0]==r[r.sz-1]) {
                    --C[r[r.sz-1]-'A'];
                    --C[r[r.sz-2]-'A'];
                    r=r.substr(0,r.sz-2);
                    r+=a[j][2];
                    ++C[a[j][2]-'A'];
                    break;
            }
        }
        FOR(j,0,b.sz) if (C[b[j][0]-'A'] && C[b[j][1]-'A']) {
            r="";
            CLR(C,0);
            break;
        }
    }
    printf("[");
    FOR(i,0,r.sz) {
        if (i) printf(", ");
        printf("%c",r[i]);
    }
    printf("]\n");
}

int main() {
#ifdef NEV_DEBUG
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    clock_t beg = clock();
#else
    //freopen("ffriends.in","r",stdin);
    //freopen("ffriends.out","w",stdout);
#endif

    int tn; scanf("%d",&tn);
    for(int tc=1; tc<=tn; ++tc) { 
        printf("Case #%d: ",tc);
        solve();
    }

#ifdef NEV_DEBUG
    fprintf(stderr,"*** Total time: %.3lf ***\n",1.0*(clock()-beg)/CLOCKS_PER_SEC);
#endif
    return 0;
}