#include<iostream>
#include<cmath>
using namespace std;

double W;
int L,U,G;

struct POINT
{
    double x, y;
} UP[128],DP[128];
double Sarea()
{
       double ans=0;
       for (int i=1;i<L;++i)
           ans+=(UP[i-1].y + UP[i].y) * (UP[i].x-UP[i-1].x);
       for (int i=1;i<U;++i)
           ans-=(DP[i-1].y + DP[i].y) * (DP[i].x-DP[i-1].x);
       return ans/=2;
}
double Carea(double t)
{
       double ans=0;
       int k=0;
       while (k<L && UP[k].x<t) ++k;
       for (int i=1;i<k;++i)
           ans+=(UP[i-1].y + UP[i].y) * (UP[i].x-UP[i-1].x);
       POINT tp;
       double Scale=(t-UP[k-1].x) / (UP[k].x-UP[k-1].x);
       tp.x=Scale *( UP[k].x-UP[k-1].x )  + UP[k-1].x;
       tp.y=Scale *( UP[k].y-UP[k-1].y )  + UP[k-1].y;
           ans+=(tp.y+UP[k-1].y) * (tp.x-UP[k-1].x);
           
       k=0;
       while (k<U && DP[k].x<t) ++k;
       for (int i=1;i<k;++i)
           ans-=(DP[i-1].y + DP[i].y) * (DP[i].x-DP[i-1].x);
        tp;
        Scale=(t-DP[k-1].x)/(DP[k].x-DP[k-1].x);
       tp.x=Scale *( DP[k].x-DP[k-1].x )  + DP[k-1].x;
       tp.y=Scale *( DP[k].y-DP[k-1].y )  + DP[k-1].y;
           ans-=(tp.y+DP[k-1].y) * (tp.x-DP[k-1].x);
           
           return ans/2;       
}
void Cut(double t)
{
            int k=0;
       while (k<L && UP[k].x<t) ++k;
       POINT tp;
       double Scale=(t-UP[k-1].x)/(UP[k].x-UP[k-1].x);
       int tn;
       POINT ttt[128];
        if (fabs(Scale-1)<1e-8)
        tn=0; else
        {
         tp.x=Scale *( UP[k].x-UP[k-1].x )  + UP[k-1].x;
         tp.y=Scale *( UP[k].y-UP[k-1].y )  + UP[k-1].y;
         tn=1;
          ttt[0]=tp;
        }
       for (int i=k;i<L;++i) ttt[tn++]=UP[i];
       for (int i=0;i<tn;++i) UP[i]=ttt[i];
       L=tn;
       
           
       k=0;
       while (k<U && DP[k].x<t) ++k;
        Scale=(t-DP[k-1].x)/(DP[k].x-DP[k-1].x);
        if (fabs(Scale-1)<1e-8)
        tn=0; else
        {
              tp.x=Scale *( DP[k].x-DP[k-1].x )  + DP[k-1].x;
              tp.y=Scale *( DP[k].y-DP[k-1].y )  + DP[k-1].y;
              tn=1;
              ttt[0]=tp;
        }
       for (int i=k;i<U;++i) ttt[tn++]=DP[i];
       for (int i=0;i<tn;++i) DP[i]=ttt[i];
       U=tn;
}
void Solve()
{
     cin>>W>>U>>L>>G;
     double miny=100000000;
     for (int i=0;i<U;++i)
     {
         cin>>DP[i].x>>DP[i].y;
         miny=min(DP[i].y,miny);
     }
     for (int i=0;i<L;++i)
     {
         cin>>UP[i].x>>UP[i].y;
         miny=min(UP[i].y,miny);
     }
     for (int i=0;i<L;++i)UP[i].y-=miny;
     for (int i=0;i<U;++i)DP[i].y-=miny;
     
     double Need=Sarea()/G;
     for (int i=0;i<G-1;++i)
     {
         double lb=UP[0].x,rb=UP[L-1].x;
              int cnt=0;
         while (fabs(lb-rb)>1e-10 || cnt>100)
         {
               double mid=(lb+rb)/2;
               if (Carea(mid) < Need)
                              lb=mid; else rb=mid;
               cnt++;
         }
         printf("%.8lf\n",lb);
         Cut(lb);
     }
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
    int t;
    cin>>t;
    for (int i=1;i<=t;++i)
    {
        printf("Case #%d:\n",i);
        Solve();
    }
    return 0;
}
