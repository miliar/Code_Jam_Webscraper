#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;

const int size = 55;
char g[size][size];
bool visited[size][size];

int R, C;

bool Check()
{
	int blues = 0;
	int i,j;
	for(i = 0; i < R; i++)
	{
		for(j = 0;j < C; j++)
		{
			if(g[i][j] == '#')
				blues++;
		}
	}

	if(blues % 4 != 0)
		return false;

	int cnt = 0;
	for(i = 0; i< R; i++)
	{
		for(j = 0; j < C; j++)
		{
			if(visited[i][j])continue;
			if(g[i][j] == '#')
			{
				if(g[i][j+1] == '#' && g[i+1][j+1] == '#' && g[i+1][j] == '#' && visited[i][j] == false && visited[i+1][j] == false && visited[i+1][j+1] == false && visited[i][j+1] == false)
				{
					cnt += 4;
					g[i][j] = '/';
					g[i][j+1] ='\\';
					g[i+1][j+1] = '/';
					g[i+1][j] = '\\';
					visited[i][j] = true;
					visited[i+1][j] = true;
					visited[i+1][j+1] =true;
					visited[i][j+1] = true;

				}
				else
				{
					return false;
				}
			}
		}
	}

	if(cnt == blues)
		return true;
	else
		return false;
}

void main2()
{

	memset(visited, false, sizeof(visited));
	memset(g,' ', sizeof(g));

	scanf("%d %d", &R, &C);
	gets(g[0]);
	int i;
	for(i = 0; i < R; i++)
	{
		gets(g[i]);
	}

	if(Check()){
		printf("\n");
		for(i = 0; i < R; i++)
		{
			printf("%s\n", g[i]);
		}
	}
	else
	{
		printf("\nImpossible\n");
	}

}

int main() {

#define GETANS

#ifdef GETANS
	 freopen("A-large.in","rt",stdin);
	freopen("ans.out","wt",stdout);
#endif

	int c,t;
	c = 0;
	scanf("%d", &t);
	while(t--)
	{
		c++;
		printf("Case #%d:", c);
		main2();
	}

	return 0;
}