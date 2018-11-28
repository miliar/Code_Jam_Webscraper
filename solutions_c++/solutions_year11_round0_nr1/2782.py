#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>
#include <stdlib.h>
#include <cmath>
using namespace std;

int main()
{
	freopen("e:\\A-small.in", "r", stdin);	freopen("e:\\A-small.out", "w", stdout);
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		printf("Case #%d: ",i+1);
		int n;
		scanf("%d",&n);
		getchar();
		int res=0;
		int place[2]={1,1};//0 is O,1 is B
		int place1;
		char last;
		int timeused=0;
		int x;
		scanf("%c %d",&last,&x);
		res=res+x;
		timeused=res;
		if(last == 'O')
			place1=0;
		else
			place1=1;
		place[place1]=x;
		for(int j=1;j<n;j++)
		{
			char which;
			int button;
			getchar();
			scanf("%c %d",&which,&button);
			if(which == last)
			{
				res=res+abs(place[place1]-button)+1;
				timeused=timeused+abs(place[place1]-button)+1;
			}
			else if(which != last)
			{
				last=which;
				place1=((place1+1)%2);
				int timeneed=abs(button-place[place1])-timeused;
				if(timeneed > 0)
					res+=timeneed;
				res++;
				timeused=1;
			}
		}
		printf("%d\n",res);
	}
	return 0;
}