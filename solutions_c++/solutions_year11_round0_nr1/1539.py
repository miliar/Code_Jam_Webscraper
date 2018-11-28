#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

struct node
{
	char col;
	int pos;
}seq[102];

int myabs(int x)
{
	if (x < 0)
		return	-x;
	else
		return	x;
}

int main()
{
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	int nCase;
	scanf("%d",&nCase);
	for (int nc = 0 ; nc < nCase ; nc++)
	{
		int n;
		scanf("%d",&n);
		for (int i=0;i<n;i++)
			scanf(" %c %d",&seq[i].col,&seq[i].pos);
		int ans = 0;
		int posB = 1 , posO = 1;
		int step = 0;

		if (seq[0].col == 'O')
		{
			ans += 1 + abs(seq[0].pos - posO) - step; 
			step = 1 + abs(seq[0].pos - posO);
			posO = seq[0].pos;
		}
		else
		if (seq[0].col == 'B')
		{
			ans += 1 + abs(seq[0].pos - posB) - step; 
			step = 1 + abs(seq[0].pos - posB);
			posB = seq[0].pos;
		}
		else
			cerr << "INPUT ERROR" << endl;
		for (int i=1;i<n;i++)
		{
			if (seq[i].col == 'O' && seq[i-1].col != 'O')
			{
				if (abs(seq[i].pos - posO) >= step)
				{
					ans += 1 + abs(seq[i].pos - posO) - step;
					step = 1 + abs(seq[i].pos - posO) - step;
				}
				else
				{
					ans += 1;
					step = 1;
				}
				posO = seq[i].pos;
			}
			else
			if (seq[i].col == 'B' && seq[i-1].col != 'B')
			{
				if (abs(seq[i].pos - posB) >= step)
				{
					ans += 1 + abs(seq[i].pos - posB) - step;
					step = 1 + abs(seq[i].pos - posB) - step;
				}
				else
				{
					ans += 1;
					step = 1;
				}
				posB = seq[i].pos;
			}
			else
			if (seq[i].col == 'B')
			{
				ans += 1 + abs(seq[i].pos - posB);
				step += 1 + abs(seq[i].pos - posB);
				posB = seq[i].pos;
			}
			else
			if (seq[i].col == 'O')
			{
				ans += 1 + abs(seq[i].pos - posO);
				step += 1 + abs(seq[i].pos - posO);
				posO = seq[i].pos;
			}
			else
				cerr << "INPUT ERROR" << endl;
		}
		printf("Case #%d: %d\n",nc+1,ans);
	}
	return	0;
}