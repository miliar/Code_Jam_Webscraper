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

template<class T> inline void checkMin(T &a, T b){if (b<a) a=b;}
template<class T> inline void checkMax(T &a, T b){if (b>a) a=b;}

const int MOD = 1000000007;
const int INF = 0x7fffffff;

const int N = 50;
string a[N];

int n, m;

int ans;

void init(){
    cin >> n >> m;
    REP(i, n) cin >> a[i];
}

void solve(){
    REP(i, n-1){
        REP(j, m-1){
            if (a[i][j] == '#'){
                if (a[i][j+1] != '#' || a[i+1][j] != '#' || a[i+1][j+1] != '#'){
                    cout << "Impossible" << endl;
                    return;
                }
                else {
                    a[i][j] = a[i+1][j+1] = '/';
                    a[i][j+1] = a[i+1][j] = 92;
                    j++;
                }
            }
        }
        if (a[i][m-1] == '#') {
            cout << "Impossible" << endl;
            return;
        }
    }
    
    REP(j, m){
        if (a[n-1][j] == '#') {
            cout << "Impossible" << endl;
            return;
        }
    }
    
    REP(i, n)
    cout << a[i] << endl;
}


int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int T; cin >> T;
    REP_1(i, T){
        init();
        printf("Case #%d:\n", i);
         solve();
    }
}


