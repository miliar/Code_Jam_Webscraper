#include <iostream>
#include <Cstdio>
using namespace std;
long long T,t,i,j,k,r,l,n,c,p;
double a[10001];
bool b[10001];
double tm,res;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    //T=9;
    for (r=1; r<=T; r++)
    {
        cin>>l>>t>>n>>c;
        for (i=1;i<=c;i++)
         cin>>a[i];
        for (i=c+1;i<=n;i++)
         a[i]=a[i-c];
         res=100000000000000;
         if (r==26)
         {
             int o=1;
         }
        for (i=0; i<=n; i++)
        {
         for (j=i+1; j<=n; j++)
          {
             if (l==1||l==2) b[i]=true;
             if (l==2) b[j]=true;
             tm=0;
             for(k=1; k<=n;k++)
              {
                  if (b[k-1]==true&&tm>=t)
                  {
                   tm+=a[k];
                   continue;
                  }
                  if (b[k-1]==true&&tm+a[k]*2>t)
                  {
                   tm+=((t-tm)+a[k]-(t-tm)*0.5);
                   continue;
                  }
                  tm+=a[k]*2;
              }
             b[i]=false;
             b[j]=false;
             res=min(tm,res);
          }
        }
          int ans=res+0.0000001;
          cout<<"Case #"<<r<<": "<<ans<<endl;

          }

    return 0;
}
