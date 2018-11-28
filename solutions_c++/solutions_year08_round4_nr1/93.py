#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int Visit[10000][2],Table[10000][2];
int Data[10000],Oper[10000],Cb[10000],N,V;
int calc(int o,int a,int b) {return (o>0)?(a&b):(a|b);}
int solve(int node,int v)
{
	if (Visit[node][v]) return Table[node][v];
	Visit[node][v]=1;
	int &ret=Table[node][v];
	ret=-1;
	if (node>=N/2) 
	{
		if (Data[node]==v) return ret=0;
		return ret=-1;
	}
	int L=node*2+1;
	int R=L+1;
	int q,w,e;
	for (q=0;q<=Cb[node];q++) for (w=0;w<=1;w++) for (e=0;e<=1;e++)
		if (calc(Oper[node]^q,w,e)==v)
		{
			if (solve(L,w)<0) continue;
			if (solve(R,e)<0) continue;
			if (ret<0 || solve(L,w)+solve(R,e)+q<ret)
				ret=solve(L,w)+solve(R,e)+q;
		}
	return ret;
}
int main()
{
	int t,T;
	scanf("%d",&T);
	for (t=1;t<=T;t++)
	{
		scanf("%d %d",&N,&V);
		int q;
		for (q=0;q<N;q++)
		{
			Visit[q][0]=Visit[q][1]=0;
			if (q<N/2) scanf("%d %d",Oper+q,Cb+q);
			else scanf("%d",Data+q);
		}
		int z=solve(0,V);
		if (z<0) printf("Case #%d: IMPOSSIBLE\n",t);
		else printf("Case #%d: %d\n",t,z);
	}
	return 0;
}
