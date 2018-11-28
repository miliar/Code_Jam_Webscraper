#include <iostream>
#include <cmath>

using namespace std;

int c,n;
double x[15],y[15],r[15];
int jjj;
int i,j;
double ans=100000000.0;

double maxx(double xxx,double yyy)
{
    if(xxx>yyy)
    return xxx;
    else
    return yyy;
}

double minn(double xxx,double yyy)
{
    if(xxx>yyy)
    return yyy;
    else
    return xxx;
}

int main()
{
    FILE *fin=fopen("D-small-attempt0.in","r");
    FILE *fout=fopen("D.out","w");
    fscanf(fin,"%d",&c);
    for(jjj=1;jjj<=c;jjj++)
    {
        fscanf(fin,"%d",&n);
        for(i=1;i<=n;i++)
        {
            fscanf(fin,"%lf %lf %lf",&x[i],&y[i],&r[i]);
        }
        if(n==1)
        {
            fprintf(fout,"Case #%d: %lf\n",jjj,r[1]);
        }
        else if(n==2)
        {
            fprintf(fout,"Case #%d: %lf\n",jjj,maxx(r[1],r[2]));
        }
        else
        {
            ans=100000000.0;
            for(i=1;i<=n;i++)
            {
                for(j=i+1;j<=n;j++)
                {
                    ans=minn(ans,maxx(r[6-i-j],maxx(sqrt((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j]))+r[i]+r[j],2.00*maxx(r[i],r[j]))/2.00));
                }
            }
            fprintf(fout,"Case #%d: %lf\n",jjj,ans);
        }
    }
    return 0;
}
