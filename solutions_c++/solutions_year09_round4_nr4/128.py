#include<iostream>
#include<cmath>
using namespace std;
int cn,ci,n,i,j,k,L;
double A1,A2,B1,B2,C1,C2,P,Q,R;
double px[50],py[50],r[50];
int a[1001000];
double ar[1001000];
double d[50][50];
int m;
double ans,pi,pj;
double xx,yy;
double eps=1e-7;
double tmp;

double cross(double x1,double y1,double x2,double y2)
{
    return x1*y2-x2*y1;
}

double sqr(double x)
{
    return x*x;
}

double dis(double x1,double y1,double x2,double y2)
{
    return sqrt(sqr(x1-x2)+sqr(y1-y2));
}

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    scanf("%d",&cn);
    for (ci=1;ci<=cn;ci++)
    {
        scanf("%d",&n);
        for (i=0;i<n;i++) scanf("%lf %lf %lf",&px[i],&py[i],&r[i]);
        for (i=0;i<n;i++)
        for (j=0;j<n;j++) d[i][j]=dis(px[i],py[i],px[j],py[j]);
        if (n==1) ans=r[0];
        else
        {
            m=0;
            for (i=0;i<n;i++)
            {
                a[m]=1<<i;
                ar[m]=r[i];
                m++;
            }
            for (i=0;i<n;i++)
            for (j=i+1;j<n;j++)
            {
                R=(d[i][j]+r[i]+r[j])*0.5;
                pi=R-r[i];
                pj=R-r[j];
                xx=(px[i]*pj+px[j]*pi)/(pi+pj);
                yy=(py[i]*pj+py[j]*pi)/(pi+pj);
                a[m]=0;
                ar[m]=R;
                for (k=0;k<n;k++)
                if (dis(xx,yy,px[k],py[k])+r[k]<R+eps) a[m]|=(1<<k);
                m++;
            }
            for (i=0;i<n;i++)
            for (j=i+1;j<n;j++)
            for (k=j+1;k<n;k++)
            {
                A1=-px[i]*2+px[j]*2;
                A2=-px[j]*2+px[k]*2;
                B1=-py[i]*2+py[j]*2;
                B2=-py[j]*2+py[k]*2;
                C1=-r[i]+r[j]-sqr(px[i])-sqr(py[i])+sqr(px[j])+sqr(py[j]);
                C2=-r[j]+r[k]-sqr(px[j])-sqr(py[j])+sqr(px[k])+sqr(py[k]);
                P=cross(A1,A2,B1,B2);
                Q=cross(C1,B1,C2,B2);
                R=cross(A1,C1,A1,C2);
                if (fabs(P)>eps)
                {
                    xx=Q/P;
                    yy=R/P;
                    R=dis(xx,yy,px[i],py[i])+r[i];
                    a[m]=0;
                    ar[m]=R;
                    for (L=0;L<n;L++)
                    if (dis(xx,yy,px[L],py[L])+r[L]<R+eps) a[m]|=(1<<L);
                    m++;
                }
            }
            ans=1e30;
            for (i=0;i<m;i++)
            for (j=i+1;j<m;j++)
            if ((a[i]|a[j])==(1<<n)-1)
            {
                tmp=ar[i];
                if (ar[j]>tmp) tmp=ar[j];
                if (tmp<ans) ans=tmp;
            }
        }
        printf("Case #%d: %.6lf\n",ci,ans);
    }
    return 0;
}
