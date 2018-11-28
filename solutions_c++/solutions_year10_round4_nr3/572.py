#include<iostream>
#include<set>
#include<vector>
using namespace std;

int main()
{
	freopen("C-small-attempt0.in", "rt", stdin);
	//freopen("A-small.out", "wt", stdout);
	FILE * f =fopen("test.out","wt");
	int tests;
	scanf("%d", &tests);
	for(int num=1;num<=tests;++num)
	{
		int x1,y1,x2,y2;
		int r;
		//set<pair<int, int> > used;
		//int used[120][120] = {0};
		vector< vector<int> > used;
		used.resize(120);
		for(int i=0;i<120;++i)
			used[i].resize(120);
		scanf("%d", &r);
		for(int i=0;i<r;++i)
		{
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			for(int x=x1;x<=x2;++x)
			{
				for(int y=y1;y<=y2;++y)
				{
					used[x][y] = 1;
				}
			}
		}
		int time = 0;
		while(true)
		{
			int found = false;
			for(int x=100;x>0;--x)
			{
				for(int y=100;y>0;--y)
				{
					if(used[x][y])
						found = true;
					int u1 = used[x-1][y];
					int u2 = used[x][y-1];
					if(u1&&u2)
					{
						used[x][y] = 1;
					}
					if(!u1 && !u2)
					{
						used[x][y] = 0;
					}
				}
			}
			if(!found)
				break;
			++time;
		}
		printf("Case #%d: %d\n", num, time);
		fprintf(f, "Case #%d: %d\n", num, time);
	}

	return 0;
}