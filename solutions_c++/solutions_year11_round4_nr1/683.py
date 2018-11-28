/*
 * Author: OldY
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
using namespace std;
const int maxint = -1u>>1;
const double eps = 1e-6;
const double pi = acos(-1.0);


int T,n;
double x,s,r,t;
struct node{
    double s,e;
    double w;
    bool operator < (const node & a) const{
        return w < a.w;
    }
} ww[1010];

//bool cmp(node a , node b){
    //return a.w < b.w;
//}

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin >> T;
    for(int ca = 1 ; ca <= T ; ca++){
        cin >> x >> s >> r >> t >> n;
        double ans = 0.0;
        double needw = 0;
        for(int i = 0 ; i < n ; i++){
            cin >> ww[i].s >> ww[i].e >> ww[i].w;
            needw += ww[i].e - ww[i].s;
        }
        needw = x - needw;
        sort(ww , ww + n);
        //cout << needw << endl;
        double tmp;
        tmp = needw/r;
        if(tmp <= t){
            ans += tmp;
            t -= tmp;
        }
        else{
            ans += t + (needw-t*r)/s;
            t = 0.0;
        }
        for(int i = 0 ; i < n ; i++){
            if(t > 0){
                tmp = (ww[i].e-ww[i].s)/(r+ww[i].w);
                if(tmp <= t){
                    ans += tmp;
                    t -= tmp;
                }
                else{
                    ans += t + ((ww[i].e-ww[i].s)-t*(r+ww[i].w))/(s+ww[i].w);
                    t = 0.0;
                }
            }
            else{
                ans += (ww[i].e-ww[i].s)/(s+ww[i].w);
            }
        }
        cout << "Case #" << ca << ": ";
        printf("%.8f\n",ans);
    }
    return 0;
}

