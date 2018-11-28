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
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <climits>
#include <queue>
using namespace std;

int main(){
    int x,y,z,vx,vz,vy;
    int t,n,no=1;
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        x=y=z=vx=vy=vz=0;
        int a,b,c,d,e,f;
        for(int i=0;i<n;i++){
            scanf("%d %d %d %d %d %d",&a,&b,&c,&d,&e,&f);
            x+=a;
            y+=b;
            z+=c;
            vx+=d;
            vy+=e;
            vz+=f;
        }
        //printf("%d %d %d %d %d %d\n",x,y,z,vx,vy,vz);
        if(vx*vx+vy*vy+vz*vz==0){
            //if(x*vx+y*vy+z*vz>=0)
                printf("Case #%d: %.8f %.8f\n",no++,sqrt(double(x*x)/double(n*n)+double(y*y)/double(n*n)+double(z*z)/double(n*n)),0.0);
            //else printf("Case #%d: %.8f %.8f\n",no++,0.0,-double(x*x+y*y+z*z)/double(x*vx+y*vy+z*vz)/2.0);
            continue;
        }
        double tm=-double(x*vx+y*vy+z*vz)/double(vx*vx+vy*vy+vz*vz);
        if(tm<0.0){
            //printf("Case #%d: %f %f\n",no++,sqrt(double(x*x+y*y+z*z)),0.0);
            //else printf("Case #%d: %.8f %.8f\n",no++,0.0,-double(x*x+y*y+z*z)/double(x*vx+y*vy+z*vz)/2.0);
            //continue;
            tm=0.0;
        }
        double dm=sqrt((((double)x+(double)vx*tm)/(double)n)*(((double)x+(double)vx*tm)/(double)n)+(((double)y+(double)vy*tm)/(double)n)*(((double)y+(double)vy*tm)/(double)n)+(((double)z+(double)vz*tm)/(double)n)*(((double)z+(double)vz*tm)/(double)n));
        printf("Case #%d: %.8f %.8f\n",no++,dm,tm);
    }
    return 0;
}

