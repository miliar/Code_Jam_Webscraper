#include<iostream>
using namespace std;
const int maxn=5010;
const int limit=10000;
int ans,a[maxn][3],n,test,tt,tot,r[maxn],s[limit<<2];
void init()
{
     scanf("%d",&n);
     int i,j;
     for (i=0;i<n;i++)
         for (j=0;j<3;j++) scanf("%d",&a[i][j]);     
}

int cmp(int x,int y)
{
    return a[x][1]<a[y][1];
}

void add(int num,int ll,int rr,int x)
{
     if (ll>x) return;
     if (rr<x) return;
     if (ll==rr) 
     {
        s[num]++;
        return;
     }
     int mid;
     mid=(ll+rr)/2;
     add(num*2,ll,mid,x);
     add(num*2+1,mid+1,rr,x);
     s[num]=s[num*2]+s[num*2+1];
}

int query(int num,int ll,int rr,int l1,int r1)
{
    if (ll>r1) return 0;
    if (rr<l1) return 0;
    if ((l1<=ll)&&(r1>=rr)) return s[num];
    int mid;
    mid=(ll+rr)/2;
    return query(num*2,ll,mid,l1,r1)+query(num*2+1,mid+1,rr,l1,r1);
}

void work()
{
     ans=0;
     int i1,i,j,x;
     for (i=0;i<=limit;i++)
     {
         tot=0;
         for (j=0;j<n;j++)
         if (a[j][0]<=i)
         {
            r[tot]=j;
            tot++;
         }
         sort(r,r+tot,cmp);
         memset(s,0,sizeof(s));
         for (j=0;j<tot;j++)
         {
             x=limit-i-a[r[j]][1];
             add(1,0,limit,a[r[j]][2]);
             if (j<ans) continue;
             ans>?=query(1,0,limit,0,x);
         }
     }
}

void print()
{
     printf("Case #%d: %d\n",tt,ans);
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    for (scanf("%d",&test),tt=1;tt<=test;tt++)
    {
        init();
        work();
        print();
    }
    return 0;
}
