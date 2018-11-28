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
#define MAX MAX
#define INF INF

using namespace std;

typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector< VI > VII;

int main()
{
	int T;
	scanf("%d",&T);
	int N,Pd,Pg;
	int cases = 1;
	while(T--)
	{
		scanf("%d %d %d",&N,&Pd,&Pg);
		bool flag = false;
		if(Pg==0)
		{
			if(Pd == 0)
				printf("Case #%d: Possible\n",cases++);
			else
				printf("Case #%d: Broken\n",cases++);
			continue;
		}
		if(Pg == 100)
		{
			if(Pd == 100)
				printf("Case #%d: Possible\n",cases++);
			else
				printf("Case #%d: Broken\n",cases++);
			continue;
		}
		for(int D=1;D<=N;D++)
		{
			if((Pd*D)%100 == 0)
			{
				flag = true;
				break;
			}				
		}
		if(!flag)
			printf("Case #%d: Broken\n",cases++);
		else
			printf("Case #%d: Possible\n",cases++);
	}
	return 0;
}
