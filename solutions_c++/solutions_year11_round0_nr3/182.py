#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <string>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cctype>

using namespace std;
typedef long long int64;
const int inf = 0x3f3f3f3f;
typedef double real;
const real eps = 1e-6;
typedef pair<int,int> pip;
#define Eo(x) { cerr << #x << " = " << (x) << endl; }

const int maxn = 1010;
int a[maxn];
int b[maxn];
const int maxq = (1<<20);
int d[2][maxq];

int main(){
    int T; cin >> T;
    for (int _ = 0; _ < T; _++){
        int n; cin >> n;
        int xr = 0;
        memset(b,0,sizeof(b));
        int sum = 0;
        int mn = inf;
        for (int i = 0; i < n; i++){
            cin >> a[i];
            sum += a[i];
            xr ^= a[i];
            if (mn>a[i]) mn = a[i];
            for (int p = a[i], q = 0;p;p>>=1,q++){
                if (p&1){ 
                    b[q]++;
//                    Eo(q);Eo(b[q]);
                }
            }
        }
        printf("Case #%d: ",_+1);
        if (xr){
            puts("NO");
            continue;
        }
        printf("%d\n",sum-mn);
        continue;
#if 0
        memset(d,0x3f,sizeof(d));
        int fr = 0;
        int ba = 1;
        d[fr][0] = 0;
        for (int i= 0; i < n; i++){
            Eo(i);
            swap(fr,ba);
            memset(d[fr],0x3f,sizeof(d[fr]));
            for (int j = 0; j < maxq; j++) if (d[ba][j] < inf){
                Eo(j);
                d[fr][j^a[i]] = min(d[fr][j^a[i]],d[ba][j]+a[i]);
            }
        }
        int best = inf;
        for (int i = 0; i < maxq; i++){
            int x = d[fr][i];
            int y = sum-x;

        }
        if (d[fr][mid] >= inf){
            puts("NO");
            continue;
        }
        printf("%d\n",sum-d[fr][mid]);
#endif
    }
	return 0;
}

