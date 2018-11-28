#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<ctime>

using namespace std;

#define MIN(a,b)  ((a) < (b) ? (a) : (b))
#define inf 200000
#define MAX 10005

int tree[MAX][2],parent[MAX],state[MAX],change[MAX],types[MAX];
int memo[MAX][3];

int solve(int node,int type)
{
	int ret=inf;
	int and=0,or=0;

	if(memo[node][type]!=-1) return memo[node][type];

	if(!parent[node])
	{
		if(state[node]==type) return 0;
		return inf;
	}

	int ca=0,co=0;

	if(types[node] || change[node]) and=1;
	if(!types[node] || change[node]) or=1;

	if(!types[node] &&  change[node]) ca=1;
	if( types[node] &&  change[node]) co=1;

	int a1,b1,a2,b2;
		
	a1=solve(tree[node][0],1);
	a2=solve(tree[node][0],0);
	b1=solve(tree[node][1],1);
	b2=solve(tree[node][1],0);


	if(and)
	{
		if(type)   ret=MIN(ret,ca+a1+b1);
		if(!type)  ret=MIN(ret,ca+a1+b2);
		if(!type)  ret=MIN(ret,ca+a2+b1);
		if(!type)  ret=MIN(ret,ca+a2+b2);
	}

	if(or)
	{
		if(type)  ret=MIN(ret,co+a1+b1);
		if(type)  ret=MIN(ret,co+a1+b2);
		if(type)  ret=MIN(ret,co+a2+b1);
		if(!type) ret=MIN(ret,co+a2+b2);
	}
//		printf("%d %d %d %d %d %d %d %d\n",node,type,a1,b1,a2,b2,ca,co);
//	printf("%d %d %d\n",and,or,ret);

	return memo[node][type]=ret;
}

int main()
{
	int i,j,k,tests,cs=0;

	//freopen("C:\\.in","r",stdin);
	freopen("C:\\Alarge.txt","w",stdout);

	scanf("%d",&tests);

	for(i=1;i<=MAX;i++)
	{
		tree[i][0]=2*i;
		tree[i][1]=2*i+1;
	}

	while(tests--)
	{
		int M,V;
		scanf("%d %d",&M,&V);
		memset(parent,0,sizeof(parent));
		memset(state,0,sizeof(state));

		for(i=1;i<=(M-1)/2;i++)
		{
			parent[i]=1;
			scanf("%d %d",&types[i],&change[i]);
		}

		for(;i<=M;i++)
			scanf("%d",&state[i]);

		memset(memo,-1,sizeof(memo));

		int sol=solve(1,V);



		printf("Case #%d: ",++cs);
		if(sol==inf)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",sol);



	}
	return 0;
}