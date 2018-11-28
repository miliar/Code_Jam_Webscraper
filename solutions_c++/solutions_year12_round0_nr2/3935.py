#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <cassert>
#define FAST __attribute__((optimize("O3")))

using namespace std;

#define all(c)    (c).begin(),  (c).end()
#define rall(c)  (c).rbegin(), (c).rend()

#define _auto(var, x)           typeof(x) var = (x)
#define _auxforeach(it, b, e)   for(_auto(it, b), _itend = e; it != _itend; ++it)
#define foreach(it, r...)       _auxforeach(it, r)

typedef long long LLONG;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef vector<VB> VVB;

enum { INF = 1<<30 };

int main(){
    int t, s, p, n, x;
    int caso=1;
    scanf("%d", &t);
    while(t--){
        scanf("%d %d %d", &n, &s, &p);
        int pre=0;
        int res=0;
        for(int i=0; i<n; ++i){
            scanf("%d", &x);
            if(x<p) continue;
            //printf("%d\n", x);
            //printf("%d > %d\n", x-(2*p-1), p-1);
            //printf("%d > %d\n", x-(2*p-1), p-3);
            if(x-(2*p-1) >= p-1) res++;
            else if(x-(2*p-1) >= p-3) pre++;
            //printf("%d %d\n", res, pre);
        }

        printf("Case #%d: %d\n", caso++, res+min(pre, s));
    }

}
