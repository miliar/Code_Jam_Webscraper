/**********************************************************************
Author: hanshuai
Created Time:  2011/6/4 23:08:37
File Name: a.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;
typedef pair<double, double> PDD;
const double eps = 1e-8;
const int maxn = 2005;
int L[maxn], W[maxn];
vector<PDD> vp;
int sgn(double v){
    return (v>eps) - (v<-eps);
}
int main() {
    freopen("a.out", "w", stdout);
    int test, X, S, R, T, N, cas = 0;
    scanf("%d", &test);
    while(test --){
        scanf("%d%d%d%d%d", &X, &S, &R, &T, &N);
        int left = X;
        for(int i = 0; i < N; i ++){
            int t1, t2;
            scanf("%d%d%d", &t1, &t2, &W[i]);
            L[i] = t2 - t1;
            left -= L[i];
//            printf("%d %d %d\n", t1, t2, W[i]);
        }
        L[N] = left;
        W[N] = 0;
        N ++;
        vp.clear();
        for(int i = 0; i < N; i ++) vp.push_back(make_pair(W[i], L[i]));
        sort(vp.begin(), vp.end());
        double LT = T, ans = 0;
        for(int i = 0; i < (int)vp.size(); i ++){
            double use = 0;
            if(S >= R) use = 0;
            else if(sgn((R+vp[i].first)*LT-vp[i].second) < 0){
                use = LT;
            }else{
                use = vp[i].second / (R+vp[i].first);
            }
//            use = 0;
            LT -= use;
            ans += use;
            double lv = vp[i].second - (R+vp[i].first)*use;
//            printf("len = %lf w = %lf use = %lf lv = %lf\n", vp[i].second, vp[i].first, use, lv);
            ans += lv/(S+vp[i].first);
        }
        printf("Case #%d: ", ++cas);
        printf("%.10lf\n", ans);
        fprintf(stderr, "test = %d\n", test);
//        break;
        /*
        double wans = 0, ans;
        for(int i = 0; i < N; i ++){
            wans += (double)L[N]/(S+W[i]);
        }
        if(S >= R) ans = wans;
        else{
            double l = eps, r = ans;
            while(sgn(l-r) < 0){
                double mid = (l + r)/2;
                if(getT(mid)
            }
        }
        */
    }
    return 0;
}

