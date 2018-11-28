#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

int main()
{
	//freopen("C-small-attempt0.in","r",stdin);freopen("C-small-output.txt","w",stdout);
	//freopen("C-small-attempt2.in","r",stdin);freopen("C-small-output.txt","w",stdout);
	freopen("C-large.in","r",stdin);freopen("C-large-output.txt","w",stdout);

	int visited[1100];
	memset(visited,-1,sizeof(visited));
	
	visited[0]=0;
	int grp[1100];
	__int64 income[1100];
	int T;
	scanf("%d",&T);
	for(int Case=1;Case<=T;Case++)
	{
		int R,tot,N;
		scanf("%d %d %d",&R,&tot,&N);
		int i=0;
		for(i=0;i<N;i++)
			scanf("%d",&grp[i]);
		memset(visited,-1,sizeof(visited));
		memset(income,0,sizeof(income));
		visited[0]=0;
		int index = 0;
		__int64 ret = 0;
		__int64 sump = 0;
		for(i=0;i<N;i++)sump+=grp[i];
		if(sump<=tot)
		{
			ret = (__int64)sump*R;
		}else
		for(int step=1;step<=N+1 && step<=R;step++)
		{
			int sum = 0;
			while(sum<=tot)
			{
				sum+=grp[index];
				if(sum>tot)
				{
					sum-=grp[index];
					break;
				}else
				{
					index= (index+1)%N;
				}
			}
			if(visited[index]==-1)
			{
				income[step]=sum;
				ret += sum;
				visited[index]=step;
			}else if(visited[index]!=-1)
			{
				ret+=sum;
				income[step]=sum;
				int pre = visited[index];
				int dis = step-pre;
				int remind = R-step;
				__int64 Sum = 0;
				for(i=pre+1;i<=step;i++)
					Sum+=income[i];
				ret += ((__int64)remind/dis)*Sum;
				for(i=pre+1;i-pre<=remind%dis;i++)
					ret+=income[i];
				break;
			}
		}
		printf("Case #%d: %I64d\n",Case,ret);
	}
}