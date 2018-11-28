#include<iostream>
using namespace std;
const int maxn=210;
int x1[maxn],y1[maxn],x2[maxn],y2[maxn],x[maxn];
double ly[maxn],hy[maxn],area[maxn];
int n1,n2,w,g,n;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int cases,tt;
    int i,j,k;
    double s,l,r,mid;
    for (scanf("%d",&cases),tt=0;tt<cases;tt++)
    {
        scanf("%d%d%d%d",&w,&n1,&n2,&g);
        memset(ly,0,sizeof(ly));
        memset(hy,0,sizeof(hy));
        memset(area,0,sizeof(area));
        for (i=0;i<n1;i++) scanf("%d%d",&x1[i],&y1[i]);
        for (i=0;i<n2;i++) scanf("%d%d",&x2[i],&y2[i]);
        i=1;
        j=1;
        n=1;
        x[0]=0;
        ly[0]=y1[0];
        hy[0]=y2[0];
        area[0]=0;
        while (1)
        {
              if (i==n1&&j==n2) break;
              if (j==n2||i<n1&&x1[i]<x2[j])
              {
                 if (x1[i]!=x[n-1])
                 {
                    x[n]=x1[i];
                    ly[n]=y1[i];
                    hy[n]=hy[n-1]+1.0*(x[n]-x[n-1])*(y2[j]-y2[j-1])/(x2[j]-x2[j-1]);
                    area[n]+=area[n-1]+(hy[n]-ly[n]+hy[n-1]-ly[n-1])*(x[n]-x[n-1])/2;
                    n++;
                 }
                 i++;
              }
              else
              {
                  if (x2[j]!=x[n-1])
                  {
                     x[n]=x2[j];
                     hy[n]=y2[j];
                     ly[n]=ly[n-1]+1.0*(x[n]-x[n-1])*(y1[i]-y1[i-1])/(x1[i]-x1[i-1]);
                     area[n]+=area[n-1]+(hy[n]-ly[n]+hy[n-1]-ly[n-1])*(x[n]-x[n-1])/2;
                     n++;
                  }
                  j++;
              }
        }
        printf("Case #%d:\n",tt+1);
        for (i=1,j=0;i<g;i++)
        {
            s=area[n-1]/g*i;
            while (area[j+1]<s) j++;
            l=0;
            r=x[j+1]-x[j];
            for (k=0;k<100;k++)
            {
                mid=(l+r)/2;
                if (mid*(hy[j]*2-ly[j]*2+(hy[j+1]-ly[j+1]-hy[j]+ly[j])/(x[j+1]-x[j])*mid)/2>=s-area[j]) r=mid;
                else l=mid; 
            }
            printf("%.10lf\n",x[j]+r);
        }
    }
    return 0;
}
