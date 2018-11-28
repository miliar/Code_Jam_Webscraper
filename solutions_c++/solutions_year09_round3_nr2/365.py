#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

const int M=505;
int n;
double x[M],y[M],z[M],vx[M],vy[M],vz[M];


double f(double t){
    double xm,ym,zm;
    xm=ym=zm=0;
    //cout<<"+_++++"<<x[0]<<endl;
    for(int i=0;i<n;i++){
        xm+=(x[i]+t*vx[i]);
        ym+=(y[i]+t*vy[i]);
        zm+=(z[i]+t*vz[i]);
    }
    xm/=n;
    ym/=n;
    zm/=n;
    return xm*xm+ym*ym+zm*zm;
}

double ternarySearch(double left, double right, double absolutePrecision) {
    
    if (fabs(right-left) < absolutePrecision) return (left+right)/2;
    
    double leftThird = (left*2+right)/3;
    double rightThird = (left+right*2)/3;
    //printf("%.8llf %.8llf %.8llf %.8llf %.8llf %.8llf\n",left,right,leftThird,rightThird,f(leftThird),f(rightThird));
    
    if (f(leftThird) >= f(rightThird))
        return ternarySearch(leftThird, right, absolutePrecision);
    else
        return ternarySearch(left, rightThird, absolutePrecision);
}

int main(){
    int test;
    scanf("%d",&test);
    for(int t=1;t<=test;t++){
        printf("Case #%d: ",t);
        
        scanf("%d",&n);
        for(int i=0;i<n;i++){
            int a,b,c,d,e,f;
            scanf("%d %d %d %d %d %d",&a,&b,&c,&d,&e,&f);
            x[i]=a; y[i]=b; z[i]=c;
            vx[i]=d; vy[i]=e; vz[i]=f;
        }
        
        double l,r,pres;
        l=0;
        r=1e10;
        pres=1e-9;
        
        double res;
        //printf("%.8llf %.8llf %.8llf\n",f(0),f(1),f(r));
        if(fabs(f(r)-f(l))<pres) res=0; 
        else res=ternarySearch(l,r,pres);
        printf("%.8llf %.8llf\n",sqrt(f(res)),res);
        
    }
    return 0;
}
