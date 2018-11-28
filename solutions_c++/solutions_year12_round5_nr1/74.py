# include <cstdio>
# include <iostream>
# include <algorithm>
# include <vector>
# include <cstring>
# include <cctype>
# include <set>
# include <map>
# include <cmath>
# include <queue>
# include <string>

using namespace std;

struct two
{
	int index,time,percent;
}ar[1000];

bool operator<(const two& t1,const two& t2)
{
	if(t1.percent*t2.time!=t2.percent*t1.time)return t1.percent*t2.time>t2.percent*t1.time;
	return t1.index<t2.index;
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		printf("Case #%d:",t);
		
		int N;
		scanf("%d",&N);
		
		for(int i=0;i<N;i++)
			scanf("%d",&ar[i].time);
		for(int i=0;i<N;i++)
			scanf("%d",&ar[ar[i].index=i].percent);
		
		sort(ar,ar+N);
		
		for(int i=0;i<N;i++)
			printf(" %d",ar[i].index);
		
		printf("\n");
	}
	return 0;
}
