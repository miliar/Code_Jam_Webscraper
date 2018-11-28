#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<iostream>
using namespace std;
struct point
{
       int l,r;
       bool operator <(const point & a)const
       {
            return l<a.l; 
       } 
}p[10005];
int a[10005];
int m;
int lowbit(int t)
{
    return t&(-t);
}
int modify(int x,int v)
{ 
    for(int i=x;i<=m;i+=lowbit(i))
    { 
            
            a[i]+=v;
    }
}
int sum(int x)
{ 
    int re=0;
    for(int i=x;i>0;i-=lowbit(i))
   
    re+=a[i];
    return re;
}

 
int main()
{   
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    int num=0;
    scanf("%d",&t);
    while(t--)
    {         
              num++;
              int n;
              scanf("%d",&n);
              m=0;
              for(int i=1;i<=n;i++)
              {
              scanf("%d%d",&p[i].l,&p[i].r);
              if(p[i].r>m)m=p[i].r;
              }
              sort(p+1,p+n+1);
              memset(a,0,sizeof(a));
              int re=0;
              for(int i=n;i>=1;i--)
              {
                      re+=sum(p[i].r);
                      modify(p[i].r,1);
              }
              printf("Case #%d: %d\n",num,re);
              //for(int i=1;i<=n;i++)
              //printf("%d %d\n",p[i].l,p[i].r);
    }
    //system("pause");
    return 0;
}
