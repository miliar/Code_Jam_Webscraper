#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>
#define MAXN 1005
using namespace std;

struct walkway{
    double b,e;
    double x;
    friend bool operator<(walkway a,walkway b){
        return a.x<b.x;
    }
}ww[MAXN];
int main(){
   // freopen("A-small-attempt1.in","r",stdin);
    freopen("A-large.in","r",stdin);
   freopen("A-largeout.txt","w",stdout);
    int T,N;
    double X,S,R,t;
    scanf("%d",&T);
    for(int ca=1;ca<=T;ca++){
        scanf("%lf %lf %lf %lf %d",&X,&S,&R,&t,&N);
        double sl=0;
        for(int i=0;i<N;i++){
            scanf("%lf %lf %lf",&ww[i].b,&ww[i].e,&ww[i].x);
            sl+=ww[i].e-ww[i].b;
        }
        ww[N].b=0;
        ww[N].e=X-sl;
        ww[N].x=0;
        N++;
        sort(ww,ww+N);
        double p=0,tt=0;
        for(int i=0;i<N;i++){
            double ds=ww[i].e-ww[i].b;
            if((R+ww[i].x)*t>ds){
                    t -= ds/(R+ww[i].x);
                    tt += ds/(R+ww[i].x);
            }
            else{
                    tt += t + (ds-t*(R+ww[i].x))/(S+ww[i].x);
                    t = 0;
            }

        }
        printf("Case #%d: %.12lf\n",ca,tt);
    }
    return 0;
}
