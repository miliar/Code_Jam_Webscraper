#include<iostream>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#include<math.h>
using namespace std;
int a,b,c,d,e,f;
double x[1005],y[1005];
int n,t;
int w,l;
int cas;
double r[1500];
int judge;
double dis(int i,int j)
{
    return (x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j]);
}

int sui()
{
    int a,b;
    int k;
    x[1]=0; y[1]=0;
    for (a=2;a<=n;a++)
    {
        for (b=1;b<=1000;b++) //Ëæ¼´100´Î
        {
            int jiao=rand()%628;
            double tt=jiao/100.0;
            int temp;
            temp=rand()%a;
            while (temp==0) temp=rand()%a;
            double rr=sqrt((r[a]+r[temp])*(r[a]+r[temp]))+1.5;
            x[a]=x[temp]+rr*cos(tt);
            y[a]=y[temp]+rr*sin(tt);
            //cout<<x[a]<<' '<<y[a]<<endl;
            if (x[a]<0 || x[a]>w) continue;
            if (y[a]<0 || y[a]>l) continue;
            for (c=1;c<a;c++)
            {
                if (dis(c,a)<(r[a]+r[c])*(r[a]+r[c]))
                {
                    break;
                }
            }
            if (c==a) break;
        }
        if (b==1001) break;
    }
    
    
    if (a==n+1) 
    {
        printf("Case #%d:",cas);
        judge=1;
        for (a=1;a<=n;a++) printf(" %.6lf %.6lf",x[a],y[a]);
        cout<<endl;
    }
}
int main()
{
    srand(unsigned(time(0)));
    freopen("B-large.in","r",stdin);
    freopen("1.out","w",stdout);
    cin>>t;
    for (cas=1;cas<=t;cas++)
    {
        cin>>n>>w>>l;
        judge=0;
        for (a=1;a<=n;a++) cin>>r[a];
        /*if (cas==5)
        {
            cout<<1<<endl;
            cout<<n<<' '<<w<<' '<<l<<endl;
            for (a=1;a<=n;a++) cout<<r[a]<<' ';
            return 0;
        }*/
        
        for (a=1;a<=10000;a++)
        if (judge==0)
        {
            sui();
        }
    }
    //while (1);
}
