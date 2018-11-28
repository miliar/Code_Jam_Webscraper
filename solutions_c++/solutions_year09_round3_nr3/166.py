#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <algorithm>
#include <utility>
#include <string>
#include <functional>
#include <sstream>
#include <fstream>
using namespace std;
#define FOR(i,a,b) for (i=(a);i<=(b);i++)
#define fori(it,v) for (it=(v).begin();it!=(v).end();it++)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define all(c) c.begin(),c.end()
#define pf push_front
#define popb pop_back
#define popf pop_front
typedef pair<int,int> ii;
FILE *in,*out;
int v[150][150],a[150][150],val[150];
const int inf=1<<30;
int dfs(int x,int y)
{	
	if (x>=y)
		return 0;
	if (x+1==y)
		return 0;
	if (v[x][y])
		return a[x][y];
	v[x][y]=1;
	int i;
	a[x][y]=inf;
	FOR(i,x+1,y-1)
		a[x][y]=min(a[x][y],dfs(x,i)+dfs(i,y));
	a[x][y]+=val[y]-val[x]-2;
	return a[x][y];
}
int main()
{
	int p,q,T,t,i;
	in=fopen("test.in","r");
	out=fopen("test.out","w");
	fscanf(in,"%d",&t);
	FOR(T,1,t)
	{
		memset(a,0,sizeof(a));
		memset(v,0,sizeof(v));
		memset(val,0,sizeof(val));
		fscanf(in,"%d%d",&p,&q);
		FOR(i,1,q)
			fscanf(in,"%d",&val[i]);
		sort(val+1,val+q+1);
		val[0]=0;
		val[q+1]=p+1;
/*		minv=inf;
		FOR(i,1,q)
a			minv=min(dfs(1,val[q]-1)+dfs(val[q]+1,p),minv);
		if (minv==inf)
			minv=0;
		if (q)
		{
			minv+=p-1;
		}*/
		fprintf(out,"Case #%d: %d\n",T,dfs(0,q+1));
	}
	fclose(in);
	fclose(out);
        return 0;
}
