#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <iostream>
using namespace std;
char s[100][100];
int mp[100][100];
int D;
const double eps=1e-8;
bool check(int x1,int x2,int y1,int y2,double x,double y)
{
   double ans1=0.0;
   double ans2=0.0;
   for(int i=x1;i<=x2;i++)
     for(int j=y1;j<=y2;j++)
     {
         if(i==x1&&j==y1)
             continue;
         if(i==x1&&j==y2)
             continue;
          if(i==x2&&j==y1)
             continue;
          if(i==x2&&j==y2)
             continue;
          ans1+=(i-x)*(mp[i][j]+D)*1.0;
          ans2+=(j-y)*(mp[i][j]+D)*1.0;
          //cout<<i<<" "<<j<<" "<<x1<<" "<<x2<<" "<<y1<<" "<<y2<<endl;
     }
     if(fabs(ans1)<=eps&&fabs(ans2)<=eps)
       return true;
     return false;
}

int main()
{
    int t,R,C;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    scanf("%d",&t);
    int cas=0;
    while(t--)
    {
      scanf("%d%d%d",&R,&C,&D);
      for(int i=0;i<R;i++)
        scanf("%s",s[i]);
      for(int i=0;i<R;i++)
        for(int j=0;j<C;j++)
          mp[i][j]=s[i][j]-'0';
      bool flag=false;
      int re;
      for(int K=min(R,C);K>=3&&!flag;K--)
      {
           for(int i=0;i+K-1<R&&!flag;i++)
             for(int j=0;j+K-1<C&&!flag;j++)
             {
                 double x=(i+i+K-1)/2.0;
                 double y=(j+j+K-1)/2.0;
                 if(check(i,i+K-1,j,j+K-1,x,y))
                 {
                     flag=true;
                     re=K;
                     break;
                 }
            }
          //cout<<"asf"<<endl;
      }
      printf("Case #%d: ",++cas);
      if(!flag)
        printf("IMPOSSIBLE\n");
      else
        printf("%d\n",re);

    }
    return 0;
}
