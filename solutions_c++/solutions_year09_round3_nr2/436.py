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
#include<fstream>

using namespace std;

int main()
{
    double t,d;
    int k,n,i;
    int x[500],y[500],z[500],vx[500],vy[500],vz[500];
    long long int xs=0,ys=0,zs=0,vxs=0,vys=0,vzs=0;
    fstream in("B-large.in",ios::in);
    fstream out("B-small-attempt1.out",ios::out);
    in>>k;
    for(int a=0;a<k;a++)
    {
        xs=0,ys=0,zs=0,vxs=0,vys=0,vzs=0;
        in>>n;
        for(i=0;i<n;i++)
        {
            in>>x[i]>>y[i]>>z[i]>>vx[i]>>vy[i]>>vz[i];
            xs+=x[i];
            ys+=y[i];
            zs+=z[i];
            vxs+=vx[i];
            vys+=vy[i];
            vzs+=vz[i];
        }
        t=0;
        if((vxs*vxs+vys*vys+vzs*vzs)!=0 && ((xs*vxs*-1+ys*vys*-1+zs*vzs*-1)>0))
        {
            t=(double)(xs*vxs*-1+ys*vys*-1+zs*vzs*-1)/(double)(vxs*vxs+vys*vys+vzs*vzs);
        }
        d=sqrt((xs+vxs*t)*(xs+vxs*t)+(ys+vys*t)*(ys+vys*t)+(zs+vzs*t)*(zs+vzs*t))/n;
        out<<fixed;
        out<<"Case #"<<a+1<<": "<<setprecision(8)<<d<<" "<<t<<endl;
    }
}
