#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

typedef long long ll;
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define for0(a,b) for(int a = 0; a < b; a ++)
#define for1(a,b) for(int a = 1; a <= b; a ++)

using namespace std;

// int bacs[201][201];
int maxx = 200, maxy=200;
int bacs[201][201];
// int maxx = 10, maxy=10;

// int bacs[1001][1001];
// int maxx = 1000, maxy=1000;

int main()
{
	int T; cin >> T;
	for1(kase,T)
	{
		for0(x,maxx) for0(y,maxy) bacs[x][y] = 0;
		int r; cin >> r;
		bool alive = false;
		for0(i,r)
		{
			int x1, x2, y1, y2;
			cin >> x1 >>y1 >> x2 >> y2;
			// cout << x1 << "," << x2 << "," << y1 << "," << y2 << endl;
			for (int x = x1; x <= x2; x ++)
				for (int y = y1; y <= y2; y ++)
				{
					// cout << x << "," << y << endl;
					alive = true;
					bacs[x][y] = 1;
					}
		}
		
			// for0(x,maxx) {
				// for0(y,maxy)
				// {
					// cout << bacs[x][y];
				// }
				// cout << endl;
			// }
		int time = 0;
		while(alive)
		{
			time ++;
			// if (time > 5) break;
			// cout << time << endl;
			for (int x = maxx-1; x >= 0; x --)
				for(int y = maxy-1; y > 0; y --)
			// for0(x,maxx)
				// for0(y,maxy)
				{
					if (bacs[x][y] == 1)
					{
						if (x >= maxx-50 || y >= maxy-50)
							cout << "der";
					if ((x == 0 || bacs[x-1][y] == 0) &&
						(y == 0 || bacs[x][y-1] == 0))
						bacs[x][y] = 2;
						}
						
					if (bacs[x][y] == 0)
					{
					if ((x != 0 && bacs[x-1][y] != 0) &&
						(y != 0 && bacs[x][y-1] != 0))
						bacs[x][y] = 1;
					}
				}
				
			alive = false;
			for0(x,maxx) {
				for0(y,maxy)
				{
					// cout << bacs[x][y];
					if (bacs[x][y] == 2) bacs[x][y] = 0;
					if (bacs[x][y] == 1)
						alive = true;
				}
				// cout << endl;
			}
			// cout << "------------" << endl;
			// for0(x,maxx) {
				// for0(y,maxy)
				// {
					// cout << bacs[x][y];
				// }
				// cout << endl;
			// }
		}
		
		
		
		cout << "Case #" << kase << ": " << time << endl;
	}
}
