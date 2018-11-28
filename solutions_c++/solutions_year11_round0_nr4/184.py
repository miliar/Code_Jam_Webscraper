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
char was[maxn];
int a[maxn];

real z[maxn];
int main(){
    z[1] = 0;

#if 0
    for (int i = 2; i < 20; i++){
        for (int j = 0; j < i; j++){
            a[j] = j;
        }
        int same = 0;
        int all = 0;
        for (;;){
            all++;
            memset(was,0,sizeof(was));
            for (int j = 0; j < i; j++) if (!was[j]){
                int p = j;
                int cur = 0;
                for (;!was[p];){
                    cur++;
                    was[p] = 1;
                    p = a[p];
                }
                if (cur==i) same++;
                else z[i] += z[cur];
            }
            if (!next_permutation(a,a+i))break;
        }
        z[i] = (all+z[i])/real(all-same);
        Eo(z[i]);
    }
#endif

    int T; cin >> T;
    for (int _ = 0; _ < T; _++){
        int n; cin >> n;
        for (int i = 0; i < n; i++){
            cin >> a[i];
            a[i]--;
        }
        memset(was,0,sizeof(was));
        int res = 0;
        for (int i = 0; i < n; i++) if (!was[i]){
            int p = i;
            int cur = 0;
            for (;!was[p];){
                cur++;
                was[p] = 1;
                p = a[p];
            }
            if (cur==1) continue;
            res += cur;
        }
        printf("Case #%d: %d.000000\n",_+1,res);
    }
	return 0;
}

