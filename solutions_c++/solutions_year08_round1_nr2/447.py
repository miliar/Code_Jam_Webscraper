#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <vector>
using namespace std;
typedef long long ll;

int n,c;
bool malted[10],bmalted[10];
char m[100][10];
const int INF=1<<30;
int minm;

bool customerSatisfied(int customer)
{
    for(int k=0;k<n;k++)
    {
	int x=m[customer][k];
	if(x==3)
	    return true;
	if(x==2&&malted[k])
	    return true;
	if(x==1&&!malted[k])
	    return true;
    }
    return false;
}

bool allSatisfied()
{
    for(int k=0;k<c;k++)
	if(!customerSatisfied(k))
	    return false;
    return true;
}

void recurse(int k,int num)
{
    if(k==n)
    {
	if(allSatisfied())
	    if(num<minm)
	    {
		for(int i=0;i<n;i++)
		    bmalted[i]=malted[i];
		minm=num;
	    }
	return;
    }
    malted[k]=false;
    recurse(k+1,num);
    malted[k]=true;
    recurse(k+1,num+1);
}

int main(int argc,char *argv[])
{
    freopen("Milkshakes.in", "r", stdin);
    freopen("Milkshakes.out", "w", stdout);
    int numCases;
    scanf("%d",&numCases);
    for(int curCase=1;curCase<=numCases;curCase++)
    {
	scanf("%d%d",&n,&c);
	memset(m,0,sizeof(m));
	minm=INF;
	for(int k=0;k<c;k++)
	{
	    int t;
	    scanf("%d",&t);
	    for(int j=0;j<t;j++)
	    {
		int x,y;
		scanf("%d%d",&x,&y);
		m[k][x-1]+=y+1;
	    }
	}
	recurse(0,0);
	printf("Case #%d: ",curCase);
	if(minm<INF)
	{
	    for(int i=0;i<n-1;i++)
		printf("%d ",bmalted[i]);
	    printf("%d\n",bmalted[n-1]);
	}
	else
	    printf("IMPOSSIBLE\n");
    }
    return 0;
}
   
