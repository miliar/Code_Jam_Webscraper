#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#define MAXN 300
using namespace std;
int CAS;
int c,d;
double ans;
long long ma = 1000000000;
int p[MAXN],v[MAXN];
double lm[MAXN],rm[MAXN];

double absx(double a)
{
    if(a < 0)
        return -a;
    return a;
}
double maxx(double a,double b)
{
    if(a>b)
        return a;
    return b;
}
int count(long long time)
{
    lm[0] = p[0]-time*0.5;
    rm[0] = lm[0]+(v[0]-1)*d;
    for(int i = 1;i < c;i++)
    {
        lm[i] = maxx(p[i] - time*0.5,rm[i-1]+d);
        rm[i] = lm[i]+(v[i]-1)*d;
    }
    //for(int i = 0;i < c;i++)
    //    printf("(%lf %lf) ",lm[i],rm[i]);
    //printf("\n");
    //printf("time:%lld\n",time);
    for(int i = 0;i < c;i++)
    {
        //printf("%d %d\n",i,p[i]);
        if(rm[i]-lm[i] > time)
            return 1;
        //printf("a\n");
        if(absx(rm[i] - 1.0*p[i]) > time*0.5)
            return 1;
        //printf("b\n");
        if(absx(lm[i] - 1.0*p[i]) > time*0.5)
            return 1;
        //printf("c\n");
    }
    return 0;
}
long long erfen(long long l,long long r)
{
    long long mid = (l+r)/2;
    if(l == r)
        return l;
    //printf("xx:%lld %d\n",mid,count(mid));
    if(count(mid) == 0)
        return erfen(l,mid);
    else return erfen(mid+1,r);
}

bool cmp1(int a,int b)
{
    return a<b;
}
int main()
{
    freopen("b.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&CAS);
    for(int cas = 1;cas <= CAS;cas++)
    {
        scanf("%d%d",&c,&d);
        for(int i = 0;i < c;i++)
            scanf("%d%d",&p[i],&v[i]);
        //printf("adsf\n");
        sort(p,p+c,cmp1);
        ans = erfen(0,ma)*0.5;
        printf("Case #%d: %lf\n",cas,ans);
    }
    fclose(stdin);
    fclose(stdout);
}
