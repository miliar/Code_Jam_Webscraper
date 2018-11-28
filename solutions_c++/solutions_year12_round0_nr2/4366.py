#include<iostream>
#include<algorithm>
using namespace std;
int i,j,k,n,m,s,p,cs,q=0;
int a[1234];
bool b[1234];
int c[1234];
int main()
{
  freopen("B-large.in","r",stdin);
     freopen("B.txt","w",stdout);
    scanf("%d",&cs);

    while (cs--)
    {
        int cnt=0;
        scanf("%d%d%d",&n,&s,&p);
        for (int i=0;i<n;i++)
        {
        scanf("%d",&a[i]);
        }
              sort(a,a+n);m=0;
             memset(b,true,sizeof(b));
             for (int i=0;i<n;i++)
             {
                    if (a[i]%3==2)
                   {
                         c[m]=a[i]/3+1;
                        if (a[i]==29)
                        {
                           cnt+=(10>=p);
                           b[m]=false;
                        }
                        m++;
                        
                }
                else if (a[i]%3==0) 
                 {
                       c[m]=a[i]/3;
                       if (a[i]==0||a[i]==30)
                       {
                          b[m]=false;
                          cnt+=(c[m]>=p);
                       }
                       m++;
                  }
           }
         for (int i=0;i<m;i++)
        {
                 if (c[i]+1>=p&&s&&b[i])
                 { 
                 
                      cnt++;
                     s--;
                    b[i]=false;
              }
        }
         for (int i=n-1;i>=0;i--)
          { 
                  if (a[i]%3==1)
                  {
                      cnt+=(a[i]/3+1>=p);
                     s--;
                  }
                               
           }
          for (int i=0;i<m;i++) 
         {
                    if (b[i]) 
                     cnt+=c[i]>=p;
          }
    printf("Case #%d: %d\n",++q,cnt);
    }
}
          
