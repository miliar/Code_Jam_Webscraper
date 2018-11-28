#include<iostream>
using namespace std;
typedef long long int64;
const int maxr=1000001;
int d,n,m,l,ans,tt,cases,p[maxr];
int64 a[20];
void init()
{
     int i;
     scanf("%d%d",&d,&n);
     m=1;
     for (i=0;i<d;i++) m*=10;
     l=1;
     for (i=0;i<n;i++) 
     {
         scanf("%d",&a[i]);
         l>?=a[i];
     }
     l++;
}

int solve(int64 a,int64 b,int64 c,int64 &x,int64 &y)
{
     if (b==0)
     {
        x=c;
        y=0;
        return a;
     }     
     int64 t;
     int tmp=solve(b,a%b,c,x,y);
     t=x;
     x=y;
     y=t-a/b*y;
     return tmp;
}

int check(int64 x,int64 y,int64 z)
{
    int i;
    for (i=0;i+1<n;i++)
    if ((x*a[i]+y)%z!=a[i+1]) return -1;
    return (x*a[n-1]+y)%z;
}

void work()
{
     ans=-1;
     if (n==1) return;
     if (n==2)
     {
        if (a[0]==a[1]) ans=a[0];
        else ans=-1;
        return;
     }
     int i,tmp;
     int64 gcd,x,y,z;
     for (i=l;i<=m;i++)
     if (!p[i])
     {
        gcd=solve((a[0]-a[1]+i)%i,i,(a[1]-a[2]+i)%i,x,y);
        z=i/gcd;
        x=x%z;
        x=(x+z)%z;
        if (x<i)
        {
        y=a[0]*x%i;
        y=(a[1]-y+i)%i;
        tmp=check(x,y,i);
        if (tmp!=-1) 
        {
        if (ans==-1) ans=tmp;
        else 
        if (ans!=tmp)
        {
           ans=-1;
           return;
        }
        }
        x+=z;
        }
     }
}

void prepare()
{
     memset(p,0,sizeof(p));
     int i,j;
     for (i=2;i*i<maxr;i++)
     if (!p[i])
         for  (j=i*i;j<maxr;j+=i)
         p[j]=1;
}

void print()
{
     printf("Case #%d: ",tt+1);
     if (ans==-1) puts("I don't know.");
     else printf("%d\n",ans);
}

int main()
{
    prepare();
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    for (scanf("%d",&cases),tt=0;tt<cases;tt++)
    {
        init();
        work();
        print();
    }
    return 0;
}
