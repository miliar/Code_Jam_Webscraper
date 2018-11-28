#include<iostream>
#include <cstdio>
#include <string.h>
#include <map>
#include <string>
#include <algorithm>
using namespace std;
int n;
char a[100][101];
double ans[100];
double calwp(int v, int ex)
{
       int ct=0, win=0;
       for (int i =0;i < n;++i)
       if (i!=ex && a[v][i]!='.')
       {
                 ct++;
                 if (a[v][i]=='1') win++;
       }       
       return double(win)/double(ct);
}
double calowp(int v)
{
     int ct=0;
     double s=0;
     for (int i =0;i < n;++i)
     if (a[v][i]!='.') {ct++; s+=calwp(i,v);}
     return s/ct;
 }
 double caloowp(int v)
 {
     int ct=0;
     double s=0;
     for (int i =0;i < n;++i)
     if (a[v][i]!='.') {ct++; s+=calowp(i);}
     return s/ct;
        }
void work()
{
     for (int i =0;i < n;++i) ans[i]=0.25*calwp(i,-1) + 0.50 * calowp(i) + 0.25* caloowp(i);
 }
int main()
{
    int tc,cas;
    freopen("A-large.in","r",stdin);
    freopen("output_lr.txt","w",stdout);
    scanf("%d",&tc);
    for (cas=1;cas<=tc;++cas)
    {
        scanf("%d",&n);
        for (int i =0;i < n;++i)scanf("%s", a[i]);
        work();
        printf("Case #%d:\n", cas);
        for (int i=0;i<n;++i) printf("%.15llf\n", ans[i]);
    }
    return 0;
}
