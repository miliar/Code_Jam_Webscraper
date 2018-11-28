#include<iostream>
#include<cmath>
using namespace std;
char ss[100];
int fd,n;
int check(long long x)
{
    long long y=(int)sqrt(x);
    if (y*y==x||(y-1)*(y-1)==x||(y+1)*(y+1)==x) return 1;
    return 0;
}

void dfs(int x,long long y,long long z)
{
     if (fd) return;
     if (x<0)
     {
        if (check(z)) 
        {
           puts(ss);
           fd=1;
        }
        return;
     }
     if (ss[x]=='1') dfs(x-1,y*2,z+y);
     else
     if (ss[x]=='0') dfs(x-1,y*2,z);
     else
     {
         ss[x]='1';
         dfs(x-1,y*2,z+y);
         ss[x]='0';
         dfs(x-1,y*2,z);
         ss[x]='?';
     }
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tt,cases;
    for (scanf("%d",&cases),tt=0;tt<cases;tt++)
    {
        scanf("%s",&ss);
        n=strlen(ss);
        printf("Case #%d: ",tt+1);
        fd=0;
        dfs(n-1,1,0);
    }   
}
