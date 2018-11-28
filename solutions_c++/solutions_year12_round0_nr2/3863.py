#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    freopen("result.out","w",stdout);
    freopen("aa.in","r",stdin);
    int T;
    cin>>T;
    for (int u=1; u<=T; u++)
    {
          int n,s,p;
          int a[200];
          cin>>n>>s>>p;
          for (int i=0; i<n; i++) cin>>a[i];
          int ans=0;
          for (int i=0; i<n; i++)
          {
              int k=(a[i]-a[i]%3)/3;
              if (a[i]%3==1)
              {
                  if (k+1>=p) ans++;
              }
              if (a[i]%3==0)
              {
                  if (k>=p) ans++;
                  else if ((s>0) && (k>=1)) if (k+1>=p) {ans++; s--;}
              }
              if (a[i]%3==2)
              {
                  if (k+1>=p) ans++;
                  else if ((s>0) && (k<=8)) if (k+2>=p) {ans++; s--;}
              }
          }
          cout<<"Case #"<<u<<": "<<ans<<endl;
    }
    return 0;
}
