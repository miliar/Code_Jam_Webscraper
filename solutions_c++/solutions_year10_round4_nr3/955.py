#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

int gp[101][101];
int gp1[101][101];

int N = 100, M = 100;

bool HasW(int x, int y)
{
	if(x>1 && gp[x-1][y]) return 1;
	return 0;
}

bool HasN(int x, int y)
{
	if(y>1 && gp[x][y-1]) return 1;
	return 0;
}

void Doit(bool &flag)
{
	flag = false;
	memset(gp1, 0, sizeof(gp1));
	int i, j;
	for(i=1; i<=N; i++)
	{
		for(j=1; j<=M; j++)
		{
			//cout << gp[i][j];
			if(gp[i][j] == 0)
			{
				if(HasW(i, j) && HasN(i, j)){ gp1[i][j] = 1; flag = true;}
				else gp1[i][j] = 0;
			}
			else
			{
				if(!HasW(i, j) && !HasN(i, j)) gp1[i][j] = 0;
				else{ gp1[i][j] = 1; flag = true;}
			}
		
		}
		//cout << endl;
	}
	for(i=1; i<=N; i++)
		for(j=1; j<=M; j++) gp[i][j] = gp1[i][j];
}

int main()
{
	//freopen("C-small-attempt0.in", "r", stdin);
	//freopen("C-small.out", "w", stdout);
//	freopen("XXX-large.out", "w", stdout);
	int test, cas = 1;
	cin>>test;
	while(test--)
	{
		int R;
		
		cout << "Case #" << cas++ << ": ";
		int i, j, k;
		
		cin>>R;

		memset(gp, 0, sizeof(gp));

		for(i=0; i<R; i++)
		{
			int x0, y0, x1, y1;
			cin>>x0>>y0>>x1>>y1;
			for(j=x0; j<=x1; j++)
				for(k=y0; k<=y1; k++) gp[j][k] = 1;
		}

		bool flag = true;
		int ans = 0;
		while(flag)
		{
			Doit(flag);
			ans++;
		}

		cout << ans << endl;
	}
	return 0;
}