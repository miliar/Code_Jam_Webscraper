#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#define oo 1e9
#define eps 1e-8

using namespace std;

long long m, n, T, t, ma, mi, q, w, e, r, s, cnt, l, c;
long long a[1100];
double p[1000010], an;
priority_queue<double> qq;

int main(){
    scanf("%lld", &T);
    for (int rr = 1; rr <= T; rr++){
        an = 0;
        printf("Case #%d: ", rr);
        scanf("%lld%lld%lld%lld", &l, &t, &n, &c);
        q = n;
        for (int i=0; i<c; i++)
            scanf("%lld", &a[i]);
        for (int i=0; i<n; i++)
            p[i] = a[i%c];
        for (int i=0; i<n; i++){
            if (t >= p[i]*2)
               t -= p[i]*2, an += p[i]*2;
            else {p[i] = p[i] - (double)t/(double)2; q = i; an += t; break;}
        }
        for (int i=q; i<n; i++){
            qq.push(p[i]);
        }

        for (int i=0; i<l; i++){            
            if (!qq.empty()){
               an += qq.top();
               qq.pop();
            } else break;            
        }
        while (!qq.empty()){
              an += (qq.top() * 2);
              qq.pop();      
        }
        printf("%lld\n", (long long)(an + eps));
    }
}
