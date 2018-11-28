#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <bitset>
#include <list>
#include <set>
#include <map>

using namespace std;

#define DO(N) while(N--)
#define REP(I, N) for (int I=0;I<int(N);++I)
#define FOR(I, A, B) for (int I=int(A);I<int(B);++I)
#define DWN(I, B, A) for (int I=int(B-1);I>=int(A);--I)
#define SQZ(I, J, A, B) for (int I=int(A),J=int(B)-1;I<J;++I,--J)
#define REP_1(I, N) for (int I=1;I<=int(N);++I)
#define FOR_1(I, A, B) for (int I=int(A);I<=int(B);++I)
#define DWN_1(I, B, A) for (int I=int(B);I>=int(A);--I)
#define SQZ_1(I, J, A, B) for (int I=int(A),J=int(B);I<=J;++I,--J)
#define REP_C(I, N) for (int N____=int(N),I=0;I<N____;++I)
#define FOR_C(I, A, B) for (int A____=int(A),B____=int(B),I=A____;I<B____;++I)
#define DWN_C(I, B, A) for (int A____=int(A),B____=int(B),I=B____-1;I>=A____;--I)
#define REP_1_C(I, N) for (int N____=int(N),I=1;I<=N____;++I)
#define FOR_1_C(I, A, B) for (int A____=int(A),B____=int(B),I=A____;I<=B____;++I)
#define DWN_1_C(I, B, A) for (int A____=int(A),B____=int(B),I=B____;I>=A____;--I)

#define ALL(A) A.begin(), A.end()
#define RST(A) memset(A, 0, sizeof(A))
#define CLR(A) REP(i, n) A[i].clear()
#define CPY(A, B) memcpy(A, B, sizeof(A))
#define INS(A, P, B) A.insert(A.begin() + P, B)
#define ERS(A, P) A.erase(A.begin() + P) 
#define SRT(A) sort(ALL(A))
#define SZ(A) int(A.size())
#define PB push_back
#define MP(A, B) make_pair(A, B)

typedef long long LL;
typedef double DB;

const int MOD = 1000000007;
const int INF = 0x7fffffff;

const int N = 100;


typedef pair<DB, int> PDI;
#define x first
#define y second


DB RPI[N]; PDI WP[N], OWP[N], OOWP[N];
string R[N];
int n;


PDI wp(string S){
    DB p = 0; int q = 0;
    REP(i, n){
        if (S[i]=='.') continue;
        ++q;
        if (S[i] == '1') p++;
    }
    return MP(p, q);
}

PDI owp(string S){
    DB p = 0; int q = 0;
    REP(i, n){
        if (S[i] == '.') continue;
        ++q;
        if (S[i] == '1') p += (WP[i].x) / (WP[i].y - 1);
        else p += (WP[i].x - 1) / (WP[i].y - 1);
    }
    return MP(p, q);
}

PDI oowp(string S){
    DB p = 0; int q = 0;
    REP(i, n){
        if (S[i] == '.') continue;
        ++q;
        p += OWP[i].x / OWP[i].y;
    }
    return MP(p, q);
}

void init(){
    cin >> n;
    REP(i, n){
        cin >> R[i];
        WP[i] = wp(R[i]);
//        cout << WP[i] << endl;
    }
    
    REP(i, n)
        OWP[i] = owp(R[i]);
    
    
    REP(i, n) OOWP[i] = oowp(R[i]);
    
    
    
    //cout << WP[0] << " " << OWP[0] << " " << OOWP[0] << endl;
    
    REP(i, n) RPI[i] = DB ( WP[i].x / WP[i].y + 2 * OWP[i].x/OWP[i].y + OOWP[i].x / OOWP[i].y) / 4;
    
    
  //  REP(i, n) cout << WP[i] << " "; cout << endl;
   // REP(i, n) cout << OWP[i].x / OWP[i].y << " "; cout << endl;
    //REP(i, n) cout << OOWP[i] << " "; cout << endl;
    
    
    
    
}

void solve(){
    
}


int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int T; cin >> T;
    REP_1(i, T){
        init(); solve();
        printf("Case #%d:\n", i);
        REP(i, n) cout << RPI[i] << endl;
    }
}


