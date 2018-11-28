#include <cstdio>
#include <cstring>
char s[101][101];
int m,n,x[1001],y[1001],yl;

void find(int i,char ss[])
{
for(int j=1;j<=n;j++)
	if(strcmp(ss,s[j])==0)
    	{
        x[i]=j;
        return;
        }
}

void SS(int z)
{
if(y[z]==0)
	{
    y[z]=1;
    yl++;
    }
}

int empty()
{
if(yl==m) return 0;
return 1;
}

void fill()
{
for(int i=1;i<=m;i++)
	y[i]=0;
yl=0;
}

void go(int t)
{
fill();
int R=0;
for(int i=1;i<=n;i++)
	{
    SS(x[i]);
    if(!empty())
    	{
        fill();
        SS(x[i]);
        R++;
        }
    }
printf("Case #%d: %d\n",t,R);
}

void rd()
{
int t;
scanf("%d",&t);
for(int i=1;i<=t;i++)
	{
	scanf("%d\n",&m);
    int j;
	for(j=1;j<=m;j++)
    	gets(s[j]);
    scanf("%d\n",&n);
    char ss[100];
    for(j=1;j<=n;j++)
    	{
        gets(ss);
        find(j,ss);
        }
    go(i);
    }
}

int main()
{
freopen("A.in","r",stdin);
freopen("A.out","w",stdout);

rd();

return 0;
}
