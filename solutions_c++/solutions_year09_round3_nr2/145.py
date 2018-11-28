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
using namespace std;

int main()
{

    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    int C=1;
    while(T--){
        double x,y,z,vx,vy,vz;
        double X,Y,Z,VX,VY,VZ;
        
        int N;
        scanf("%d",&N);
        X=Y=Z=VX=VY=VZ=0;
        for(int i=0;i<N;i++){
            scanf("%lf %lf %lf %lf %lf %lf",&x,&y,&z,&vx,&vy,&vz);
            X+=x;
            Y+=y;
            Z+=z;
            VX+=vx;
            VY+=vy;
            VZ+=vz;
        }
        double t=-(VX*X+Y*VY+Z*VZ)/( (VX*VX+VY*VY+VZ*VZ));
//        printf("%lf \n",t);
        if(t>0);
        else t=0;
        double d=sqrt( (X+VX*t)*(X+VX*t) + (Y+VY*t)*(Y+VY*t) + (Z+VZ*t)*(Z+VZ*t)     );
        d/=N;
        printf("Case #%d: %.8lf %.8lf\n",C,d,t);
        C++;
    }

    return 0;
}










