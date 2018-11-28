#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<vector>
#include<list>
#include<map>
#include<string>
#include<set>
#include<algorithm>
using namespace std;

#define mm 30000
#define ll long long
int n,k;
char a[55][55],b[55][55];
int check(char tt,int r,int c,int ir,int ic)
{
    int cc=0;
    while(b[r][c]==tt)
    {cc++;
    if(cc==k)
    return 1;
    r=r+ir;
    c=c+ic;
}
return 0;
}
    

int fun(char cc)
{int s;
for(int j=1;j<=n;j++)
for(int i=1;i<=n;i++)
{if(check(cc,j,i,1,0)==1)
return 1;
}
for(int j=1;j<=n;j++)
for(int i=1;i<=n;i++)
{if(check(cc,j,i,0,1)==1)
return 1;
}

for(int j=1;j<=n;j++)
for(int i=1;i<=n;i++)
{if(check(cc,j,i,1,1)==1)
return 1;
}
for(int j=1;j<=n;j++)
for(int i=1;i<=n;i++)
{if(check(cc,j,i,1,-1)==1)
return 1;
}
return 0;
}

int main()
{freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
int c,sr,sb;
 int T,ii=0;cin>>T;while(T--)
{ii++;
scanf("%d %d",&n,&k);
for(int i=0;i<n;i++)
scanf("%s",a[i]);
//memset(b,sizeof(b),'.');
for(int i=0;i<55;i++)
for(int j=0;j<55;j++)
b[i][j]='.';
//printf("Hi");
for(int j=0;j<n;j++)
{c=1;
for(int i=n-1;i>=0;i--)
{if(a[j][i]!='.')
{b[j+1][c++]=a[j][i];
}}}//printf("Hi");
sr=fun('R');
//printf("Hi");
sb=fun('B');

//memset(a,sizeof(a),'.');
for(int i=0;i<55;i++)
for(int j=0;j<55;j++)
a[i][j]='.';
if(sr==0&&sb==0)
printf("Case #%d: Neither\n",ii);
if(sr==0&&sb==1)
printf("Case #%d: Blue\n",ii);
if(sr==1&&sb==0)
printf("Case #%d: Red\n",ii);
if(sr==1&&sb==1)
printf("Case #%d: Both\n",ii);
















}
//while(1);
return 0;
}
