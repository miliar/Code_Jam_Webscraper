#include<iostream>
#include<cmath>
using namespace std;
int T,N;

const int maxn=1000010;
bool Prime[maxn];
int pn,p[maxn];

void GetP()
{
     memset(Prime,true,sizeof(Prime));
     for (int i=2;i<sqrt(maxn)+2;++i)
     {
         if (Prime[i])
         for (int tmp=i*2;tmp<maxn;tmp+=i)
         Prime[tmp]=false;
      }
      pn=0;
      for (int i=2;i<maxn;++i)
      if (Prime[i]) p[pn++]=i;
}
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.txt","w",stdout);
    GetP();
    cin>>T;
    for (int i=1;i<=T;++i)
    {
        long long x;
        cin>>x;
        int ans=1;
        if (x==1)
        { ans=0;} else
        {
          for (int j=0;j<pn;++j)
          {
            long long tmp=p[j],tt=p[j];
            int k=0;
            while (tmp<=x) 
            {
                  tmp=tmp*tt;
                  k++;
            }
            if (k>1) ans+=k-1;
          }
        }
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
