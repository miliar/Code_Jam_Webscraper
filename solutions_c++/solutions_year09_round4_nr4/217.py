#include<iostream>
#include<cmath>
int x[50],y[50],r[50];
int l,t,i,n;
double ans;

double max(double x,double y)
{
    if(x>y)return x;else return y;
}

double min(double x,double y)
{
    if(x<y)return x;else return y;
}

double dis(int p1,int p2)
{
    return sqrt(pow(x[p1]-x[p2],2)+pow(y[p1]-y[p2],2));
}

int main()
{
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    scanf("%d",&t);
    for(l=1;l<=t;++l)
    {
        scanf("%d",&n);
        for(i=1;i<=n;++i)scanf("%d%d%d",&x[i],&y[i],&r[i]);
        if(n==1)ans=r[1];
        else if(n==2)ans=max(r[1],r[2]);
        else
        {
            ans=1e30;
            ans=min(ans,max(r[1],dis(2,3)+r[2]+r[3])/2);
            ans=min(ans,max(r[2],dis(1,3)+r[1]+r[3])/2);
            ans=min(ans,max(r[3],dis(1,2)+r[1]+r[2])/2);
        }
        printf("Case #%d: %.6lf\n",l,ans);
    }
    return 0;
}


            