#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
using namespace std;
typedef long long ll;

const int INF=100000;

int t[10001][2];
int gate[5001];
bool change[5001];

int main(int argc,char *argv[])
{
    freopen("CheatingBooleanTree.in", "r", stdin);
    freopen("CheatingBooleanTree.out", "w", stdout);
    int numCases;
    scanf("%d",&numCases);
    for(int curCase=1;curCase<=numCases;curCase++)
    {
	int m,v;
	scanf("%d%d",&m,&v);
	int maxd=(int)(log(m)/log(2));
	for(int k=1;k<=m;k++)
	    t[k][0]=t[k][1]=INF;
	for(int k=1;k<=(m-1)/2;k++)
	{
	    int g,c;
	    scanf("%d%d",&g,&c);
	    gate[k]=g;
	    change[k]=c==1;
	}
	for(int k=(m+1)/2;k<=m;k++)
	{
	    int l;
	    scanf("%d",&l);
	    t[k][l]=0;
	}
	for(int d=maxd-1;d>=0;d--)
	    for(int k=1<<d;k<1<<d+1;k++)
	    {
		if(k*2>m)
		    break;
		int lc=k*2,rc=k*2+1;
		int or0=t[lc][0]+t[rc][0];
		int or1=min(t[lc][1],t[rc][1]);
		int and0=min(t[lc][0],t[rc][0]);
		int and1=t[lc][1]+t[rc][1];
		//printf("%d\n",k);
		//printf("%d %d %d %d\n",or0,or1,and0,and1);
		if(change[k])
		{
		    if(gate[k])
			++or0,++or1;
		    else
			++and0,++and1;
		    //printf("%d %d %d %d\n",or0,or1,and0,and1);	    
		    t[k][0]=min(and0,or0);
		    t[k][1]=min(and1,or1);
		    //printf("change");
		}
		else if(gate[k])
		{
		    t[k][0]=and0;
		    t[k][1]=and1;
		    //printf("and");	
		}
		else
		{
		    t[k][0]=or0;
		    t[k][1]=or1;
		    //printf("or");
		}
		//printf("%d %d\n",t[k][0],t[k][1]);
	    }
	if(t[1][v]<INF)
	    printf("Case #%d: %d\n",curCase,t[1][v]);
	else
	    printf("Case #%d: IMPOSSIBLE\n",curCase);
    }
    return 0;
}
    
