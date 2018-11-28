#include<iostream>
#include<cstdlib>
#include<fstream>
#include<cmath>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    const int lxx=200+5;
    const double eps=0.001;
    int ts;
    cin>>ts;
    for (int ti=0; ti<ts; ti++)
    {
        double c, d, p[lxx], v[lxx];
        cin>>c>>d;
        for (int i=0; i<c; i++)
            cin>>p[i]>>v[i];
        double x0=0, x1=10000000*d;
        while (x0+eps<x1)
        {
            double x=(x0+x1)/2;
            bool flag=true;
            double q=-10000000*d;
            for (int i=0; i<c; i++)
            {
                double q2=p[i]-x;
                if (q2<q+d)
                    q2=q+d;
                q=q2+d*(v[i]-1);
                if (q>p[i]+x)
                {
                    flag=false;
                    break;
                }
            }
            if (flag)
                x1=x;
            else
                x0=x;
        }
        cout<<"Case #"<<ti+1<<": ";
        x0=floor(x0*2+0.1)/2;
        printf("%.8lf\n",x0);
    }
    return 0;
}
                
