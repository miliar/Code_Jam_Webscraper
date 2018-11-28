#include<iostream>
#include<cmath>
using namespace std;
int T,R,C,D;
int Mass[512][512];



void Solve()
{
     int ans=-1;
     for (int i=0;i<R-2;++i)
     for (int j=0;j<C-2;++j)
     for (int k=3;k<=min(R-i,C-j);++k)
     {
         
         double Midi=double(i+i+k-1)/2;
         double Midj=double(j+j+k-1)/2;
         double sumi=0,sumj=0;
         for (int a=i;a<=i+k-1;++a)
         for (int b=j;b<=j+k-1;++b)
         {
              if (a==i && b==j) continue;
              if (a==i+k-1 && b==j) continue;
              if (a==i && b==j+k-1) continue;
              if (a==i+k-1 && b==j+k-1) continue;
              sumi+= double(a-Midi) * Mass[a][b];
              sumj+= double(b-Midj) * Mass[a][b];
         }
         if ( fabs(sumi)<1e-6 && fabs(sumj)<1e-6 )
         ans=max(ans,k);
     }
     if (ans<0) printf("IMPOSSIBLE\n"); else
                printf("%d\n",ans);
     
  
}

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.txt","w",stdout);
    scanf("%d\n",&T);
    for (int id=1;id<=T;++id)
    {
          scanf("%d %d %d\n",&R,&C,&D);
          char tmp[1024];
          for (int i=0;i<R;++i)
          {
              gets(tmp);
              for (int j=0;j<C;++j)
              Mass[i][j]=tmp[j]-'0';              
          } 
          printf("Case #%d: ",id);
          Solve();
    }
    return 0;
}
