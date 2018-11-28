#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	int r;
	scanf("%d\n",&r);
	for (int counter = 0; counter<r;counter++)
	{
		int n;
		scanf("%d",&n);
		char color;
		vector<int> blue;
		vector<int> orange;
		char order[1000];
		for (int i = 0; i<n;i++)
		{
			int t;
			scanf("%c",&color);
			scanf("%c %d",&color,&t);
			if (color=='B')
				blue.push_back(t);
			else
				orange.push_back(t);
			order[i]=color;
		}
		vector<int> orangeTimes;
		int oPos=1;
		for (int i =0;i<orange.size();i++)
		{
			orangeTimes.push_back(abs(orange[i]-oPos));
			
			oPos = orange[i];
		}	
		vector<int> blueTimes;
		int bPos=1;
		for (int i =0;i<blue.size();i++)
		{
			blueTimes.push_back(abs(blue[i]-bPos));
			bPos = blue[i];
		}
		
		int bCount = 0;
		int oCount = 0;
		int lastB = 0;
		int lastO = 0;
		int time = 0;
		
		for (int i = 0; i<n;i++)
		{
			if (order[i] =='O')
			{
				time = max(time+1,lastO+orangeTimes[oCount]+1);
				oCount++;
				lastO = time;
			}
			else
			{
				time = max(time+1,lastB+blueTimes[bCount]+1);
				bCount++;
				lastB = time;
			}
		}
		printf("Case #%d: %d\n",counter+1,time);
	}
	return 0;
}