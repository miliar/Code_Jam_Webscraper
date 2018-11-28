#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<time.h>
#include<math.h>
using namespace std;
int T;
int n;
double W,L;
double a[11111];
double x[11111],y[11111];
double dis(double x1,double y1,double x2,double y2)
{
  return sqrt(((x1-x2)*(x1-x2))+((y1-y2)*(y1-y2)));
}
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    srand(time(NULL));
    int i,j,k;
    int p,q,r;
    double d,dd;
    double dx,dy;
    scanf("%d",&T);
    for(int ii=0;ii<T;ii++)
     {
       scanf("%d",&n);
       scanf("%lf %lf",&W,&L);
       for(i=0;i<n;i++)scanf("%lf",&a[i]);
      // for(i=0;i<n;i++)a[i]*=-1;
       //sort(a,a+n);
       //for(i=0;i<n;i++)a[i]*=-1;
     //  printf("\n>>> ");for(i=0;i<n;i++)printf("%lf ",a[i]);printf("\n");
       
       x[0]=0;
       y[0]=0;
       for(i=1;i<n;i++)
        {
          while(1)
          {
          p=(rand()%1000)*1000000+(rand()%1000)*1000+(rand()%1000);
          p%=(int)(W);
          q=(rand()%1000)*1000000+(rand()%1000)*1000+(rand()%1000);
          q%=(int)(L);
          dx=p;
          dy=q;
          r=1;
          for(j=0;j<i;j++)
           {
             if((int)(dis(x[j],y[j],dx,dy))>=(a[j]+a[i]+1))
              {
                r=r;
              }
             else {r=0;}
           }
           if(r==1)break;
          }
        x[i]=dx;
        y[i]=dy;
        }
       printf("Case #%d: ",ii+1);
       for(i=0;i<n;i++)printf("%lf %lf ",x[i],y[i]);
       if(ii<T-1)printf("\n");
     }
    
    scanf(" ");
    return 0;
}
