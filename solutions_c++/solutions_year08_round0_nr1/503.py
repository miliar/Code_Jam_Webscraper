#include<iostream>
#include<map>
using namespace std;
map<string,int> hash;
const int maxn=100;
int n,test,tt,m,ans,v[maxn],cnt;
void init()
{
     ans=0;
     memset(v,0,sizeof(v));
     cnt=0;
     int i;
     string ss;
     scanf("%d\n",&n);
     for (i=0;i<n;i++)
     {
         getline(cin,ss);
         hash[ss]=i;
     }
     scanf("%d\n",&m);
}

void work()
{
     int i,x;
     string ss;
     for (i=0;i<m;i++)
     {
         getline(cin,ss);
         x=hash[ss];
         if (!v[x])
         {
            v[x]=1;
            cnt++;
            if (cnt==n)
            {
               ans++;
               cnt=1;
               memset(v,0,sizeof(v));
               v[x]=1;
            }
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
    scanf("%d\n",&test);
    for (tt=1;tt<=test;tt++)
    {
        init();
        work();
        print();
    }
    return 0;
}
