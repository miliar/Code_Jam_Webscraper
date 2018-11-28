#include <iostream>
#include <iomanip>
#include <cstdio>
using namespace std;
int main()
{
    int t,x,a,b,i,j,k;
    double p[3],y,q[8],z;
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    cin>>t;
    for (x=1;x<=t;x++)
    {
        cin>>a>>b;
        for (i=0;i<a;i++) cin>>p[i];
        q[0]=p[0]*(a>1?p[1]:1)*(a>2?p[2]:1);
        q[1]=p[0]*(a>1?p[1]:1)*(a>2?(1-p[2]):1);
        q[2]=p[0]*(a>1?(1-p[1]):1)*(a>2?p[2]:1);
        q[3]=p[0]*(a>1?(1-p[1]):1)*(a>2?(1-p[2]):1);
        q[4]=(1-p[0])*(a>1?p[1]:1)*(a>2?p[2]:1);
        q[5]=(1-p[0])*(a>1?p[1]:1)*(a>2?(1-p[2]):1);
        q[6]=(1-p[0])*(a>1?(1-p[1]):1)*(a>2?p[2]:1);
        q[7]=(1-p[0])*(a>1?(1-p[1]):1)*(a>2?(1-p[2]):1);
        y=0;
        for (i=0;i<8;i+=(1<<(3-a)))
            if (i) y+=q[i]*(2*b-a+2);
            else y+=q[i]*(b-a+1);
        for (i=1;i<=a;i++)
        {
            z=0;
            for (j=k=0;j<8;j+=(1<<(3-a)),k++)
                if (k<(1<<i)) z+=q[j]*(b-a+2*i+1);
                else z+=q[j]*(2*b-a+2*i+2);
            if (z<y) y=z;
        }
        if (b+2<y) y=b+2;
        cout<<"Case #"<<x<<": "<<fixed<<setprecision(6)<<y<<endl;
    }
    return 0;
}
