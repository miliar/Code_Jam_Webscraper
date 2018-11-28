#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;

#define FORALL(a,b) for(typeof((b).begin()) a = (b).begin(); a != (b).end(); ++a)
#define FOR(i,a,b) for(int i = a; i < (int)(b); ++i)

typedef long long LL;

const double EPS = 1e-6;
const int INF = 1<<29;

int arr[200];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int t, n, s, p, cas = 0;
    scanf("%d", &t);
    while (t--){
        scanf("%d %d %d", &n, &s, &p);
        for (int i = 0; i < n; ++i) scanf("%d", &arr[i]);
        int ret = 0;
        for (int i = 0; i < n; ++i){
            int a = p, b = max(0,p-2);
            int aa = p, bb = max(0,p-1);
            if (aa+bb+bb <= arr[i]) ++ret;
            else if (a+b+b <= arr[i] && s){
                --s, ++ret;
            }
        }
        printf("Case #%d: %d\n", ++cas, ret);
    }

    return 0;
}

