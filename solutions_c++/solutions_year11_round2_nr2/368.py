#include<cstdio>
#include<string>
#include<algorithm>
#include<vector>
#include<queue>
#include<cstring>
#include<map>
#include<cmath>
#include<iostream>
#define out(x) cout<<#x<<": "<<(x)<<endl;
using namespace std;

struct node
{
    double pp;
    double vv;
};

node pv[300];
double now[300];
double len[300];
double ini[300];
double eps=1e-8;
double dd;
int cc;
int sum=0;

int compare(node left,node right)
{
    return left.pp<right.pp;
}

int test(double tt)
{
    double now;
    int i;
    now=pv[0].pp-tt;
    for(i=0;i<cc;i++)
    {
        if(now<pv[i].pp-tt) now=pv[i].pp-tt;
        
        now+=(pv[i].vv-1)*dd;
        //out(now);
        if(abs(now-pv[i].pp)>tt+eps) return 0;
        
        now+=dd;
    }
    
    return 1;
}

double find(double left,double right)
{
    if(sum>500) return (left+right)/2;
    if(right-left<eps) return (left+right)/2;

    sum++;
 
    double mid=(left+right)/2;
    int res=test(mid);
    //out(mid);
    if(res) return find(left,mid);
    else return find(mid,right);
}    
        
int main()
{
    int CASE,T=1;
    int i;
    freopen("B-large.in","r",stdin);
    freopen("1.out","w",stdout);
    scanf("%d",&CASE);
    while(CASE--)
    {
        scanf("%d%lf",&cc,&dd);
        
        for(i=0;i<cc;i++) scanf("%lf%lf",&pv[i].pp,&pv[i].vv);
        
        sort(pv,pv+cc,compare);
        double temp=1000000;
        
        sum=0;
        double ans=find(0,temp*temp);
        
        printf("Case #%d: %.9lf\n",T++,ans);
    }
    return 0;
}
