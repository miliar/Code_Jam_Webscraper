#include <cstdio>
#include<stdlib.h>
#include<vector>

using namespace std;

#define DEBUG 0

int T, H, W;
int map[200][200];
char ans[200][200], next;

struct Pair
{
	int r ,c;
}dir[4];  //0: N, 1: W, 2: E, 3: S

vector<Pair> v;

void readin(void)
{
	for(int i = 0; i < H; i++)
		for(int j = 0; j < W; j++)
		{
			scanf("%d", &map[i][j]);
			ans[i][j] = '\0';
		}
}

int findDir(int r, int c)
{
	int min = map[r][c];
	int d = -1;

	for(int i = 0; i < 4; i++)
		if(r + dir[i].r >=0 && r + dir[i].r < H && c + dir[i].c >= 0 && c + dir[i].c < W && 
			map[r + dir[i].r][c + dir[i].c] < min)
		{
			min = map[r + dir[i].r][c + dir[i].c];
			d = i;
		}
	return d;
}

void solve(void)
{
	int d, r, c, nextr, nextc;
	Pair p;

	for(int i = 0; i < H; i++)
		for(int j = 0; j < W; j++)
		{
			r = nextr = i;
			c = nextc = j;
			d = findDir(r, c);

			if(ans[r][c] != '\0')
			{
				while(d >= 0)
				{
					r = nextr;
					c = nextc;
					nextr = r + dir[d].r;
					nextc = c + dir[d].c;
					ans[nextr][nextc] = ans[r][c];
					d = findDir(nextr, nextc);
				}
			}
			else
			{
				v.clear();
				p.r = r; p.c = c;
				v.push_back(p);

				while(d >= 0 && ans[nextr][nextc] == '\0')
				{
					r = nextr;
					c = nextc;
					nextr = r + dir[d].r;
					nextc = c + dir[d].c;
					p.r = nextr; p.c = nextc;
					v.push_back(p);
					d = findDir(nextr, nextc);
				}

				if(ans[nextr][nextc] !='\0')
				{
					for(int i = 0; i < v.size(); i++)
						ans[v[i].r][v[i].c] = ans[nextr][nextc];
				}
				else
				{
					for(int i = 0; i < v.size(); i++)
						ans[v[i].r][v[i].c] = next;
					next++;
				}
			}

		}

	for(int i = 0; i < H; i++)
	{
		printf("%c", ans[i][0]);
		for(int j = 1; j < W; j++)
			printf(" %c", ans[i][j]);
		printf("\n");
	}

}




int main()
{
	freopen("B-large.in","r",stdin);
	//freopen("B-small.in","r",stdin);

#if !DEBUG
	freopen ("B-large.out","w",stdout);
#endif

	dir[0].r = -1; dir[0].c =  0;
	dir[1].r =  0; dir[1].c = -1;
	dir[2].r =  0; dir[2].c =  1;
	dir[3].r =  1; dir[3].c =  0;

	scanf("%d\n", &T);

	for(int i = 1; i <= T;i++)
	{
		scanf("%d %d\n", &H, &W);
		readin();

		ans[0][0] = 'a';
		next = 'b';

		printf("Case #%d:\n", i);
		solve();
	
	}
	

#if !DEBUG
	fclose (stdout);
#endif

	return 0;
}