// cheburashka, bear-mouse, team template

#include <cstdlib>
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>
#include <cstdio>
#include <sstream>
#include <stack>
#include <string.h>
#include <cmath>
#include <queue>
#include <set>
using namespace std;

typedef long long ll;
typedef vector < string > vs;
typedef vector <int> vi;
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define deb(x) cout << #x << ": " << x << endl;
#define debv(x) for(int i = 0; i < (x).size(); i++) cout << x[i] << ' '; cout << endl;

//string split given string a and delimiters

const int MAXR = 105, MAXC = 105;


int dy[] = { -1,0,0,1 };
int dx[] = { 0, -1, 1, 0 };

int basin[MAXR][MAXC];
int flowdir[MAXR][MAXC];
int tude[MAXR][MAXC];
int R,C;
int curbasin = 0;

inline bool INB(int y, int x)
{
	if(y < 0 || x < 0)
	 return false;
	if(y >= R || x >=  C)
		return false;
	
	return true;
}




int flowdown(int y, int x)
{
	if(basin[y][x] != -1)
		return basin[y][x];
	
	if(flowdir[y][x] == -1)
		return basin[y][x] = curbasin++;
	
	int dir = flowdir[y][x];
	
	return basin[y][x] = flowdown( y + dy[dir], x + dx[dir] );
}

void setflows()
{
	for(int cr = 0; cr < R; cr++)
	{
		for(int cc = 0; cc < C; cc++)
		{
			
			int bestd = -1;
			int lowest = 10001;
			for(int d = 0; d < 4; d++)
			{
				int nr = cr  + dy[d];
				int nc = cc + dx[d];
				
				if(!INB(nr,nc)) continue;
				
				if(tude[nr][nc] >= tude[cr][cc] || tude[nr][nc] >= lowest)
					continue;
				
				lowest = tude[nr][nc];
				bestd = d;
			}
			
			flowdir[cr][cc] = bestd;
		}
	}
	
	return;
}
				

int main()
{
	int TC = 0;
	cin >> TC;
	
	for(int tcase = 1; tcase <= TC; tcase++)
	{
		cin >> R >> C;
		curbasin = 0;
		
		memset(tude,0,sizeof(tude));
		memset(basin,-1,sizeof(basin));
		memset(flowdir,-1,sizeof(flowdir));
		
		for(int i = 0; i < R; i++)
		{
			for(int j = 0; j < C; j++)
			{
				cin >> tude[i][j];
			}
		}
		
		setflows();
		for(int i = 0; i < R; i++)
		{
			for(int j = 0; j < C; j++)
			{
				flowdown(i,j);
			}
		}
		
		printf("Case #%d:\n",tcase);
		for(int i = 0; i < R; i++)
		{
			for(int j = 0; j < C; j++)
			{
				if(j > 0) printf(" %c", (char)(basin[i][j]+'a'));
				else printf("%c", (char)(basin[i][j]+'a'));
			}
			printf("\n");
		}
	}

  return 0;
}















