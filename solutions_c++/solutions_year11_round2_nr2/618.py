//Author : Nitin Gangahar
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <iostream>
#include <cstring>
#include <set>
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define isok(x,y) (x>=0 && x<R && y>=0 && y<C)
#define MAX 1000005
#define INF INF

using namespace std;

typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector< VI > VII;
int C,D,curr;
int P[MAX];
#define norm(x) (x+100000)
bool f(double val)
{
	//there are in total curr people on the line
	double prev = (double)0;
	prev = (double)P[0]-val;
	for(int i=1;i<curr;i++)
	{
		if(prev+D-P[i] > val)
			return false;
		prev = max(P[i]-val,prev+D); 
	}
	return true;
}
int main()
{
	int T,cases = 1;
	scanf("%d",&T);
	while(T--)
	{
		memset(P,0,sizeof P);
		scanf("%d %d",&C,&D);
		curr = 0;
		for(int i=0;i<C;i++)
		{
			int pt,v;
			scanf("%d %d",&pt,&v);
			for(int i=0;i<v;i++)
				P[curr++] = norm(pt);			
		}
		sort(P,P+curr);
		double min = 0,max = 1e27,mid;
		double ans = 0.00; 
		//binary search on time
		while((max-min) > 1e-8)
		{
			mid = (min+max)/(double)2.00;
			if(f(mid))
				max = mid;
			else
				min = mid;
		}
		printf("Case #%d: ",cases++);
		printf("%0.7lf\n",mid);
	}
	return 0;
}
