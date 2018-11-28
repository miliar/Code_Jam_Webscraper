#include <stdio.h>
#include <string.h>
#include <set>
using namespace std;

long long dpmat[4][4];

long long calc(int cpos, int chas, long long multiplier, int xsum, int ysum){
    if (cpos>=3){
        if (xsum%3==0 && ysum%3==0){
            return multiplier;
        } else {
            return 0;
        }
    } else if (multiplier==0) {
        return 0;        
    } else {
        long long res = 0;
        for (int i=0;i<9;i++){
            int x = i%3;
            int y = i/3;
            if (dpmat[x][y]>0){
                long long tcal = dpmat[x][y]*multiplier;
                dpmat[x][y]--;
                res += calc(cpos+1, i, tcal, xsum+x, ysum+y);
                dpmat[x][y]++;
            }
        }
        return res;
    }
}

int main(){
    int ntc,ttc=0;
    scanf("%d", &ntc);
    while (ntc--){
        memset(dpmat,0,sizeof(dpmat));
        
        /*
        X = x0, Y = y0
        print X, Y
        for i = 1 to n-1
            X = (A * X + B) mod M
            Y = (C * Y + D) mod M
            print X, Y

        */
        long long n,a,b,c,d,x0,y0,m;
        scanf("%I64d%I64d%I64d%I64d%I64d%I64d%I64d%I64d", &n,&a,&b,&c,&d,&x0,&y0,&m);
        long long x = x0, y=y0;
        set<pair<long long,long long> > points;
        points.insert(make_pair(x,y));
        for (int i=1;i<=n-1;i++){
            x = (a*x+b) % m;
            y = (c*y+d) % m;
            points.insert(make_pair(x,y));
        }
        
        for (set<pair<long long,long long> >::iterator it = points.begin();it!=points.end();it++){
            pair<long long,long long> cur = *it;
            dpmat[cur.first%3][cur.second%3]++;
        }
        long long res = calc(0,0,1,0,0)/6;
        printf("Case #%d: %I64d\n", ++ttc, res);
        printf("DCase #%d: %I64d\n", ttc, calc(0,0,1,0,0));
    }
    
    return 0;
}
