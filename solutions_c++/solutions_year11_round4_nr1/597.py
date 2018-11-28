#include <cstdio>
#include <iostream>
#include <utility>
#include <algorithm>

using namespace std;

const int MAXN = 1024;

int main(){
    int tst;
    cin >> tst;
    
    for(int lp=1;lp<=tst;++lp){
        int x,s,r,n;
        double t;
        cin >> x >> s >> r >> t >> n;
        r -= s;
        
        pair<int, int> trechos[MAXN];
        
        trechos[0].first = s;
        trechos[0].second = 0;
        int prev = 0;
        for(int i=1;i<=n;++i){
            int b,e,w;
            cin >> b >> e >> w;
            trechos[0].second += b-prev;
            prev = e;
            trechos[i].first = w+s;
            trechos[i].second = e-b;
        }
        trechos[0].second += x - prev;
        
        sort(&trechos[0],&trechos[n+1]);
        
        double resp = 0;
        
        for(int i=0;i<=n;++i){
            double ct = double(trechos[i].second)/(trechos[i].first+r);
            if(ct > t){
                ct = t + (trechos[i].second - (trechos[i].first+r)*t)/trechos[i].first;
                t = 0;
            }
            else{
                t -= ct;
            }
            resp += ct;
        }
        
        printf("Case #%d: %.6lf\n",lp,resp);
        
    }
    
    return 0;
}