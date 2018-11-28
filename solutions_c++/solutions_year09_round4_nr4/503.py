#include <stdio.h>
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

struct circle
{
    double x,y,r;
} c[60];

double dist(int i,int j)
{
    return sqrt((c[i].x-c[j].x)*(c[i].x-c[j].x)+(c[i].y-c[j].y)*(c[i].y-c[j].y));
}

int main()
{
    int T,cas,i,j,k,n;
    
    freopen("d://in.txt","r",stdin);
    freopen("d://out.txt","w",stdout);
    cin>>T;
    for (cas=1;cas<=T;cas++)
    {
        cin>>n;
        for (i=0;i<n;i++)
        {
            cin>>c[i].x>>c[i].y>>c[i].r;
        }
        cout<<"Case #"<<cas<<": ";
        if (n==1) cout<<c[0].r<<endl;
        else if (n==2) cout<<(c[0].r>c[1].r?c[0].r:c[1].r)<<endl;
        else
        {
            double res=1e300;
            for (i=0;i<n;i++)
            {
                for (j=i+1;j<n;j++)
                {
                    if (dist(i,j)<res) res=(dist(i,j)+c[i].r+c[j].r)/2.0;
                }
            }
            printf("%.8lf\n",res);
        }
    }
    return 0;
}
