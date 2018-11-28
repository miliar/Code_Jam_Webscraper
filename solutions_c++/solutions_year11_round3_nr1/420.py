#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <list>
#include <stack>
#include <map>
#include <set>
using namespace std;
 
#define DEBUG(x) //x
#define REP(i,a) for(int i=0;i<int(a);i++)
#define FOR(i,a,b) for(int i=a;i<int(b);i++)
#define VI vector<int>
#define size(x) int((x).size())
#define all(x) (x).begin(), (x).end()
#define MK(x, y) make_pair(x, y)
#define PB push_back
 
typedef pair<int, int> pii;

int n, mm;
char m[100][100], out[100][100];

bool paint(int i, int j)
{
	if (i+1 >= n || j+1 >= mm)
		return false;
	if (out[i][j+1] != ' ')
		return false;
		
	out[i][j] = '/'; out[i][j+1] = '\\';
	out[i+1][j]='\\'; out[i+1][j+1] = '/';
	return true;
}

int solve()
{
	scanf("%d %d\n", &n, &mm);
	REP(i, n)
	{
		char aux; 
		REP(j, mm)
			scanf("%c", &m[i][j]);
		scanf("%c", &aux);
	}

	memset(out, ' ', sizeof out);
	bool ok = true;
	REP(i, n)
	{
		REP(j, mm)
		{
			if (m[i][j] == '.')
				out[i][j] = '.';
			else
			{
				if (m[i][j] == '#' && out[i][j] == ' ')
				{
					ok = paint(i, j);
					if (!ok)
					{
						break;
					}
					j++;
				}
			}
		}
		if (!ok)
			break;
	}
	
	if (ok)
	{
		REP(i, n)
		{
			REP(j, mm)
				printf("%c", out[i][j]);
			printf("\n");
		}
	}
	else
		printf("Impossible\n");
}


/*********/

int main(void){
	int T,t;
	scanf("%d",&T);
	REP(t,T){
		printf("Case #%d:\n",t+1);
		solve();
	}
	return 0;
}

