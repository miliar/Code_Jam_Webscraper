#include <iostream> 
#include <vector> 
#include <algorithm> 
#include <string> 
#include <sstream> 
#include <map> 
#include <set> 
#include <cmath> 
#include <queue> 
#include <stack> 
#include <list> 
#include <numeric> 
#include <bitset> 
#include <ext/algorithm> 
#include <ext/numeric> 
#define fr(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++) 
#define fo(_a,_n) fr(_a,0,_n) 
#define all(_v) (_v).begin(),(_v).end() 
#define sz size() 
typedef long long LL; using namespace std; using namespace __gnu_cxx; 

const int inf = 10000000;

int N;

string C[305];
vector<string> cols;
int A[305], B[305];


int main() {
    int tests;
    scanf("%d", &tests);
    fr(test,1,tests+1) {
        scanf("%d", &N);
        cols.clear();
        fo(i, N) {
            cin >> C[i];
            cols.push_back(C[i]);
            scanf("%d %d", A + i, B + i);
        }
        
        fo(i,N) fr(j,i+1,N) if (A[j] < A[i] || (A[j] == A[i] && B[j] > B[i])) {
            swap(A[i], A[j]);
            swap(B[i], B[j]);
            swap(C[i], C[j]);
        }
        
        if (A[0] > 1) {
            printf("Case #%d: IMPOSSIBLE\n", test);
            continue;
        }
        
        sort(all(cols));
        cols.resize(unique(all(cols)) - cols.begin());

        int sol = inf;
        fo(a,cols.sz)fr(b,a,cols.sz)fr(c,b,cols.sz) {
            int sure = -1;
            int lmax = -1;
            int cnt = 1;
            bool hashole = false;
            fr(i, 0, N) if (C[i] == cols[a] || C[i] == cols[b] || C[i] == cols[c]) {
                if (sure == -1) {
                    sure = B[i];
                    lmax = B[i];
                    if (A[i] > 1) { hashole = true; break; }
                    continue;
                }
                if (sure + 1 < A[i]) {
                    if (lmax + 1 < A[i]) {
                        hashole = true;
                        break;
                    }
                    sure = lmax;
                    lmax = B[i];
                    ++cnt;
                } else
                    lmax = max(lmax, B[i]);
            }
            if (sure == -1) continue;
            if(hashole || lmax < 10000) continue;
            if (sure < 10000) ++cnt;
            sol = min(sol, cnt);
        }
        
        if (sol == inf) 
            printf("Case #%d: IMPOSSIBLE\n", test);
        else
            printf("Case #%d: %d\n", test, sol);
    }
    
    return 0;
}
