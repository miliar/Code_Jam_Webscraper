#include <stdio.h>
#include <string.h>
#include <math.h>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#define mp(a, b) make_pair(a, b)
#define pair_mst pair <int, pair <int, int> >

using namespace std;

int main()
{
	int t, n, b, p = 0;
	char r[2];
	
//	freopen("A-large.in", "r", stdin);
//	freopen("A-large.out", "w", stdout);
	
	scanf("%d", &t);
	while (t--)
	{
		p++;
		vector <string> turn;
		vector <int> robot[2];
		
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
		{
			scanf("%s %d", r, &b);
			turn.push_back(r);
			if (strcmp(r, "O") == 0)
				robot[0].push_back(b);
			else
				robot[1].push_back(b);
		}
		
		int i = -1, j = -1, counter = 0, flag;
		int pos_o = 1, pos_b = 1, seconds = 0;
		
		while (counter != turn.size())
		{
			flag = 0;
			if (i != robot[0].size() - 1)
			{
				if (pos_o < robot[0][i+1])
					pos_o++;
				else if (pos_o == robot[0][i+1])
				{
					if (strcmp(turn[counter].c_str(), "O") == 0)
					{
						i++;
						flag = 1;
					}
				}
				else
					pos_o--;
			}
			
			if (j != robot[1].size() - 1)
			{
				if (pos_b < robot[1][j+1])
					pos_b++;
				else if (pos_b == robot[1][j+1])
				{
					if (strcmp(turn[counter].c_str(), "B") == 0)
					{
						j++;
						flag = 1;
					}
				}
				else
					pos_b--;
			}
			
			if (flag)
				counter++;
			
			seconds++;
		}
		printf("Case #%d: %d\n", p, seconds);
	}

   return 0;
}
