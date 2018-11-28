#include <cstdio>
#include <cstring>
#include <iostream>

#define SIZE 10010
#define INF 10000000
#define AND 1
#define OR 0

using namespace std;
#define min(a,b) ((a)<(b))?(a):(b)


int G[SIZE];
int C[SIZE];
int value[SIZE];
int cache[SIZE][2];


int N,M;

int min_change(int, int);
/*inline bool is_ext(int n)
{
	return ;
}*/


int findmin(int node, int type, int value)
{
	int ret=INF;
	if (type==OR)
	{
		if (value)
			ret=min(min_change(node*2, value), min_change(((node*2)+1), value));
		else
			ret=min(ret,min_change(node*2, value)+min_change((node*2)+1, value));
	}
	else
	{
		if (value)
			ret=min(ret,min_change(node*2, value)+min_change((node*2)+1, value));
		else
			ret=min(min_change(node*2, value), min_change(((node*2)+1), value));	
	}
	return ret;
}
int min_change(int node, int value_needed)
{
	if (node>((M-1)/2)) return (value[node]==value_needed)?0:INF;
	else if (cache[node][value_needed]>-1) return cache[node][value_needed];
	else
	{
		//printf("node %d is not internal\n", node);
		int &ret=cache[node][value_needed];
		ret=INF;
		int type=G[node];
		ret=min(ret,findmin(node,type, value_needed));
		if (C[node]==1)
		ret=min(ret,findmin(node,1-type, value_needed)+1);
		//cout<<"node="<<node<<" ret="<<ret<<endl;
		return ret;
	} 
}
 
int main()
{
	int cas,V;
	scanf("%d",&N);
	for(cas=1;cas<=N;cas++)
	{
		scanf("%d %d", &M, &V);
		memset(cache,-1,sizeof(cache));
		
		for(int i=1;i<=M;i++)
		{
			if (i<=((M-1)/2))
			{
				scanf("%d %d", G+i,C+i);
			}
			else
				scanf("%d",value+i);
		}
		int answer=min_change(1,V);
		if (answer>=INF) printf("Case #%d: IMPOSSIBLE\n", cas);
		else printf("Case #%d: %d\n", cas, answer);
	}	
}
