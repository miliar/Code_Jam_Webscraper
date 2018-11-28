#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
using namespace std;
#define mp make_pair
#define pb push_back
#define MAXINT 2147483647

int main(){
    int ntest,a,b,track[100];
    double temp,memo[100];
    vector<double>prob;
    scanf("%d",&ntest);
    for (int test=1;test<=ntest;++test){
        prob.clear();
        scanf("%d %d",&a,&b);
        for (int i=0;i<a;++i){
            cin >> temp;
            prob.pb(temp);
        }
        for (int i=0;i<100;++i) memo[i]=0.0;
        
        for (int mask=0;mask<(1<<a);++mask){
            double cnt=1.0+(1e-10);
            int miss=0;
            for (int i=0;i<a;++i){
                if (mask & (1<<i))
                   cnt*=prob[i];
                else{
                    cnt*=(1.0-prob[i]);
                    miss++;
                }
            }
            double now;
            int nowmiss;
            for (int stroke=1;stroke<=a;++stroke){
                now=0.0;
                nowmiss=0;
                for (int j=a-1;j>=a-stroke;--j){
                    if (!(mask & (1<<j))) nowmiss++;
                    now++;
                }
                now+=(b-(a-stroke))+1;
                if (nowmiss<miss) now+=b+1.0;
                memo[stroke]+=(now*cnt);
            }
            bool safe=1;
            for (int i=0;i<a;++i){
                if (!(mask & (1<<i))){
                   memo[0]+=(cnt*(2*b+2-a));
                   safe=0;
                   break;
                }
            }
            if (safe){
               memo[0]+=(cnt*(b+1-a));
            }
            memo[a+1]+=(cnt*(b+2));
        }
        double ret=1000000000+(1e-10);
        for (int i=0;i<a+2;++i){
            if (ret>memo[i]) ret=memo[i];
        }
        printf("Case #%d: %.6lf\n",test,ret);
    }
    return 0;
}
