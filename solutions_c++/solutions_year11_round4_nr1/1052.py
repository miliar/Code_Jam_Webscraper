#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <stack>
using namespace std;

#define PB push_back
#define MP make_pair

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int, double> PII;

int s[1011];
PII p[1011];

int main(){
    int i, j, k, cas, re, m, n;
    int X, S, R;
    double t;
    double T;
    freopen("A-large (1).in", "r", stdin); freopen("w.txt", "w", stdout);
    scanf("%d", &cas);
    for(re = 1; re <= cas; re++){
        printf("Case #%d: ", re);
        scanf("%d%d%d%lf%d", &X, &S, &R, &t, &n);
        for(i = 0; i < n; i++){
            int x, y;
            scanf("%d%d%d", &x, &y, &p[i].first);
            p[i].second = y - x;
            p[i].first += S;
            X -= y - x;
        }
        p[n] = MP(S, X);
        sort(p, p + n + 1);

        T = 0;
        for(i = 0; i <= n; i++){
            //printf("%d %d\n", p[i].second, p[i].first);
            if((p[i].first + R - S) * t * 1.0 >= p[i].second){
                t -= p[i].second * 1.0 / (p[i].first + R - S);
                T += p[i].second * 1.0 / (p[i].first + R - S);
            }else{
                T += t;
                p[i].second -= (p[i].first + R - S) * t * 1.0;
                T += p[i].second * 1.0 / (p[i].first);
                t = 0;
            }
            //printf("%.15lf\n", T);
        }
        printf("%.15lf\n", T);
  /*      m = t * (R - S);
        T = 0;
        sort(p, p + n);
        priority_queue<PII> q;
        int s = 0;
        for(i = 0; i < n; i++){
            if(p[i].first.first > s){
                q.push(MP(-S, p[i].first.first - s));
                //printf("first = %d s = %d\n", -S, s);
            }
            q.push(MP(-(S + p[i].second), - p[i].first.first + p[i].first.second));
            //printf("first = %d s = %d\n", p[i].first.first, -(S + p[i].second));
            s = p[i].first.second;
        }
        if(p[n - 1].first.second < X){
            q.push(MP(-S, - p[n - 1].first.second + X));
        }
        while(!q.empty()){
            int gap = q.top().second;
            int sp = -q.top().first;
            //printf("%d %d\n", gap, sp);
            double u = gap * 1.0 / (sp + (R - S));
            if(t >= u){
                t -= u;
                T += u;
            }else{
                T += t;
                gap = gap - t * (sp + (R - S));
                T += gap * 1.0 / (sp);
                t = 0;
            }
            //printf("%.15lf\n", T);
            q.pop();
        }
        printf("%.15lf\n", T);
        */
 /*
        if(m > X){
            for(i = 0; i < n; i++){
                T += (p[i].second - p[i].first) * 1.0 / (s[i] + R);
                X -= p[i].second - p[i].first;
            }
            T += X * R;
            printf("%.15lf\n", T);
        }else{
            for(i = 0; i < n; i++){
                T += (p[i].second - p[i].first) * 1.0 / (s[i] + R);
                X -= p[i].second - p[i].first;
            }
        }

*/
    }
}
