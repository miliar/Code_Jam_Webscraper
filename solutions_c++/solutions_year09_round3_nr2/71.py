#include <iostream>
#include <cmath>
#include <set>
#include <map>
#include <vector>

#define sqr(x) ((x)*(x))

using namespace std;

typedef vector<int> VI;

long double X,Y,Z,VX,VY,VZ;

long double getdist(long double t)
{
    long double x,y,z;
    x = X + t*VX;
    y = Y + t*VY;
    z = Z + t*VZ;
    return sqrt(sqr(x)+sqr(y)+sqr(z));
}

void process(void)
{
    int N;
    cin >> N;
    X=Y=Z=VX=VY=VZ=0;
    for(int i=0;i<N;i++)
    {
        long double x,y,z,vx,vy,vz;
        cin >> x >> y >> z >> vx >> vy >> vz;
        X+=x;Y+=y;Z+=z;VX+=vx;VY+=vy;VZ+=vz;
    }

    long double s=0,e=1e8;

    for(int i=0;i<300000;i++)
    {
        long double m1 = (s*2.0+e)/3.0;
        long double m2 = (s+e*2.0)/3.0;
        long double dm1,dm2;
        dm1 = getdist(m1);
        dm2 = getdist(m2);

//        cout << m1 << " " << m2 << " " << dm1 << " " << dm2 << endl;

        if(dm1 < dm2 || (dm1-dm2 < 1e-12 && dm2-dm1 < 1e-12) )
            e=m2;
        else
            s=m1;
    }
    
    printf("%.8lf %.8lf\n",(double)getdist(s)/N, (double)e);
}

int main(void)
{
    int N;
    cin >> N;
    for(int i=1;i<=N;i++)
    {
        printf("Case #%d: ",i);
        process();
        cerr << i << endl;
    }
}
