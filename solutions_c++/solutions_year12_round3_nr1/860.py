
#include <iostream>
#include <cmath>
#include<stdio.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<string.h>
using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	int i,j,k;
	for(i=0;i<t;i++)
	{
		int n;
		scanf("%d",&n);
		vector< vector<int> > N;
		for(j=0;j<n;j++)
		{
			int m;
			scanf("%d",&m);
			vector<int> temp;
			for(k=0;k<m;k++)
			{
				int temp1;
				scanf("%d",&temp1);
				temp.push_back(temp1);
			}
			N.push_back(temp);
		}
		int state=0;
		/*for(j=0;j<N.size();j++)
		{
			for(k=0;k<N[j].size();k++)
				printf("%d ",N[j][k]);
				printf("\n");
		}*/
		for(j=0;j<n;j++)
		{
			queue<int> q;
			for(k=0;k<N[j].size();k++)
				q.push(N[j][k]);
			int count[1002]={0};
			state=0;
			while(!q.empty())
			{
				int y=q.front();
				count[y]++;
				//printf("%d\n",count[y]);
				if(count[y]>1)
				{
					state=1;
					break;
				}
				q.pop();
				for(k=0;k<N[y-1].size();k++)
					q.push(N[y-1][k]);
			}
			if(state==1)
				break;
		}
		if(state==1)
			printf("Case #%d: Yes\n",i+1);
		else
			printf("Case #%d: No\n",i+1);
	}
	return 0;
}
