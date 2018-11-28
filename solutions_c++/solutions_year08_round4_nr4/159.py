#include<iostream>
using namespace std;
const int maxk=20;
int n,k,test,t,v[maxk],a[maxk],ans;
string s1,s2;
void init()
{
     ans=100000;
     scanf("%d",&k);
     cin >> s1;     
     n=s1.size();
}

void work()
{
     s2="";
     int i,j,x;
     for (i=0;i<n/k;i++)
         for (j=0;j<k;j++)
         s2+=s1[i*k+a[j]];
     for (x=1,i=1;i<n;i++)
     if (s2[i]!=s2[i-1]) x++;
     ans<?=x;
}

void dfs(int dep)
{
     if (dep==k)
     {
        work();
        return;
     }
     int i;
     for (i=0;i<k;i++)
     if (!v[i])
     {
        v[i]=1;
        a[dep]=i;
        dfs(dep+1);
        v[i]=0;
     }
}

void print()
{
     printf("Case #%d: %d\n",t,ans);
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    for (scanf("%d",&test),t=1;t<=test;t++)
    {
        init();    
        dfs(0);
        print();                        
    }
}
