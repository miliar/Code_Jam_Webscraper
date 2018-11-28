#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <complex>
#include <limits>
#include <string.h>
#include <fstream>
using namespace std;
#define rep(x,n) for(int x=0;x<n;x++)
#define mp(x,y) make_pair(x,y)
#define getBit(code, i) (code & (1 << i))
#define setBit(code, i) (code | (1 << i))
#define resetBit(code, i) (code & ~(1 << i))
#define mem(a, b) memset(a, b, sizeof(a))

char grid[55][55];
int H,W;

void main2()
{
	cin >> H >> W;
	rep(i,H)rep(j,W)cin >> grid[i][j];
	bool ok = true;
	rep(i,H)
	{
		rep(j,W)
		{
			if(grid[i][j] == '#')
			{
				if(j+1 >= W || i+1 >= H || grid[i][j+1] != '#' || grid[i+1][j] != '#' || grid[i+1][j+1] != '#' )
				{
					ok = false;
					break;
				}
				else
				{
					grid[i][j] = '/';
					grid[i][j+1] = '\\';
					grid[i+1][j] = '\\';
					grid[i+1][j+1] = '/';
				}
			}
		}
		if(!ok)
			break;
	}
	if(ok)
	{
		cout << endl;
		rep(i,H)
		{
			rep(j,W)
				cout << grid[i][j];
			cout << endl;
		}
	}
	else
	{
		printf("\nImpossible\n");
	}
}

int main()
{
	freopen("in.txt", "r", stdin);
	//freopen("1small.txt", "w", stdout);
	freopen("1big.txt", "w", stdout);
	int K;
	cin >> K;
	rep(kase,K)
	{
		printf("Case #%d: ",kase+1);
		main2();
	}
	return 0;
}
