#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
using namespace std;

char mat[105][5];
struct chickqu 
{
	int pos;
	int speed;
};

//#define SMALL
#define LARGE
int main()
{
#ifdef SMALL
	freopen("A-small-attempt3.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","r",stdin);
	//freopen("A-small.in","r",stdin);
	freopen("A-large-practice.in.out","w",stdout);
#endif

	int case_n;
	char t;
	//printf("A");

	scanf("%d",&case_n);
	scanf("%c",&t);

	int times,cost=1;
	char rob[105];
	int pos_o[105];
	int pos_b[105];
	int pos_t[105];
	int sum_o=0,sum_b=0;

	for (int i=0; i<case_n; i++)
	{
		sum_o=0;
		sum_b=0;
		int cost_o=0;
		int cost_b=0;

		scanf("%d",&times);
		scanf("%c",&t);
		//printf("%d\n",times);
		for(int j=0;j<times;j++)
		{
			scanf("%c",&rob[j]);
			scanf("%c",&t);
			scanf("%d",&pos_t[j]);
			//printf("%d ",pos_t[j]);
			scanf("%c",&t);

		}
		int last_o=1;
		int last_b=1;
		int pre_o_t=-1;
		int pre_b_t=-1;
		cost=1;

		for(int j=0;j<times;j++)
		{			
			
			if(rob[j]=='O')
			{
				if(pre_o_t==-1)pre_o_t=0;
				if ((cost-pre_o_t)<=abs(pos_t[j]-last_o))
				{
					//cost_o+=abs(pos_t[j]-last_o)+1;
					cost+=(abs(pos_t[j]-last_o)-(cost-pre_o_t)+1);
				}
				else if(j!=0)
				{
					cost_o+=1;
					cost++;
				}
// 				if (j==0)
// 				{
// 					cost--;
// 				}
				
				//cost+=cost_o;
				last_o=pos_t[j];
				pre_o_t=cost;
				
			}
			else
			{
				if(pre_b_t==-1)pre_b_t=0;
				if ((cost-pre_b_t)<=abs(pos_t[j]-last_b))
				{
					//cost_b+=abs(pos_t[j]-last_b)+1;
					cost+=(abs(pos_t[j]-last_b)-(cost-pre_b_t)+1);
				}
				else if(j!=0)
				{
					//cost_b+=1;
					cost++;
				}
				//cost+=cost_b;
				//cost+=min(j-pre_b_t,pos_t[j]-pos_t[last_b]);
				last_b=pos_t[j];
				pre_b_t=cost;

			}
			//cost+=max(cost_o,cost_b);
			//cost=cost+1;
			
		}


		printf("Case #%d: %d\n",i+1,cost);

	}
	return 0;
}
