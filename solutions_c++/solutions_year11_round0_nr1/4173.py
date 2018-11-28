
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
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int GR[101];
int GP[101];
int done[101];

int cur[3]; 
int nextgoal[3]; 

int pressed = 0;

void findnextgoal(int x)
{
	int y = nextgoal[x];
	nextgoal[x] = 0;
	for(int i = y + 1; i < 101;++i)
	{
		if(GR[i] == x)
		{
			nextgoal[x] = i;
			break;
		}
	}
}
void robot(int x)
{
	if (nextgoal[x] == 0) return;
	if (cur[x] != GP[nextgoal[x]])
	{
		//printf("%d move 1 step\n",x);
		if (cur[x] < GP[nextgoal[x]]) 
			cur[x]++;
		else cur[x] --;
		return;
	}
	else  if (done[nextgoal[x]-1] && ! pressed)
	{
		//printf("%d press button %d\n", x, GP[nextgoal[x]]);
		done[nextgoal[x]] = 1;
		pressed = 1;
		findnextgoal(x);
		//printf("new goal for %d is %d\n", x, nextgoal[x]);
	}
		


}

void init()
{
	for(int i=0;i<=101;++i)
		GR[i]=GP[i]=done[i]=0;
	cur[1]=cur[2]=1;
	nextgoal[1]=nextgoal[2]=0;
	done[0]=1;
}



int solve(int n)
{
	for(int x = 1; x<=2;++x)
	for(int i=1;i<=n;++i)
	{
		if (GR[i] == x)
		{
			nextgoal[x] = i;
			break;
		}
	}

	for(int i=1;i<=n;++i) done[i] = 0;

	int steps = 0;
	while(1)
	{
		steps++;
		//printf("--------- step %d\n", steps);
		pressed = 0; 
		robot(1);
		robot(2);
		if (done[n])
			break;
	}
	return steps; 
}


int main()
{
	int tc;
	//GR[1]=2;GP[1]=2;
	//GR[2]=2;GP[2]=1;
	//GR[3]=0;GP[3]=0;
	//GR[4]=0;GP[4]=0;
	//int xx = solve(2);
	//printf("result = %d\n", xx);

	freopen("..\\A-large.in", "r", stdin);
//	freopen("a.out", "w", stdou);

	scanf("%d", &tc);
	for(int i=1;i<=tc;++i)
	{
		int n;
		init();
		scanf("%d", &n);
		for(int j=1;j<=n;++j)
		{
			char rc;
			int p;
			scanf(" %c",&rc);
			scanf(" %d",&p);
			if (rc=='O') GR[j] = 1;
			if (rc=='B') GR[j] = 2;
			GP[j] = p;
		}
		for(int j=1;j<=n;++j)
		{
			//printf("%d %d, ", GR[j], GP[j]);
		}
		if (i==4)
		{
			int stop = 1;
		}
		printf("Case #%d: %d\n", i, solve(n));
	}
	return 0;
}