#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>


using namespace std;

int main()
{
	int C;
	scanf("%d", &C);
	for (int ca=1; ca<=C; ca++)
	{
		int n, m;
		
		int maxx = -10000000, maxy = -10000000, minx = 10000000, miny = 10000000;
		scanf("%d", &n);
		
		int nb[2000][2], nbn = 0, bn = 0;
		
		set <pair<int,int> > all;
		
		for (int i=0; i<n; i++)
		{
			int x, y;
			char s[20];
			scanf("%d%d%s", &x, &y, s);
			if (s[0] == 'N')
			{
				scanf("%s", s);
				// not bird
				
				nb[nbn][0] = x;
				nb[nbn][1] = y;
				nbn++;				
			}
			else
			{
				// bird
				bn++;
				if (x > maxx) maxx = x;
				if (x < minx) minx = x;
				if (y > maxy) maxy = y;
				if (y < miny) miny = y; 
			}
		}
		
		// process not bird
		
		for (int i=0; i<nbn; i++)
		{
			all.insert(make_pair(nb[i][0], nb[i][1]));
		}

		//int a = 1000000000, b = -1000000000, c = 1000000000, d = -1000000000;
		bool unk = 1;
		int cminx, cminy, cmaxx, cmaxy;
		scanf("%d", &m);
		printf("Case #%d:\n", ca);
		for (int i=0; i<m; i++)
		{
			int x, y;
			scanf("%d%d", &x, &y);
			if (bn)
			{
				if (all.find(make_pair(x, y)) != all.end() )
					printf("NOT BIRD\n");
				else if (x >= minx && x <= maxx && y >=miny && y <= maxy)
					printf("BIRD\n");
				else
				{
					for (int i=0; i<nbn; i++)
					{
						if (nb[i][0] < minx && nb[i][1] <= maxy && nb[i][1] >= miny)
						{
							if (x <= nb[i][0]) { printf("NOT BIRD\n"); goto dn1; };
						}
						if (nb[i][0] > maxx && nb[i][1] <= maxy && nb[i][1] >= miny)
						{
							if (x >= nb[i][0]) { printf("NOT BIRD\n"); goto dn1; };
						}
						if (nb[i][1] < miny && nb[i][0] <= maxx && nb[i][0] >= minx)
						{
							if (y <= nb[i][1]) { printf("NOT BIRD\n"); goto dn1; };
						}
						if (nb[i][1] > maxy && nb[i][0] <= maxx && nb[i][0] >= minx)
						{
							if (y >= nb[i][1]) { printf("NOT BIRD\n"); goto dn1; };
						}
					}
					
					unk = 1;
					
					cminx = minx, cminy = miny, cmaxx = maxx, cmaxy = maxy;
					
	
					if (x < cminx) cminx = x;
					if (x > cmaxx) cmaxx = x;
					if (y < cminy) cminy = y;
					if (y > cmaxy) cmaxy = y;
					
					
					 
					for (int i=0; i<nbn; i++)
					{
						if (nb[i][0] >= cminx && nb[i][0] <= cmaxx && nb[i][1] >= cminy && nb[i][1] <= cmaxy)
						{
							unk = 0;
							break;
						}
					}
					if (unk)
						printf("UNKNOWN\n");
					else
						printf("NOT BIRD\n");
				}
dn1:;
			}
			else
			{
				if (all.find(make_pair(x, y)) != all.end() )
					printf("NOT BIRD\n");
				else
					printf("UNKNOWN\n");
			}			
		}
		
	}
}
