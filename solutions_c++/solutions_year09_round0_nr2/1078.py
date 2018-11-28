#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <stdio.h>

using namespace std;

#define CLEAR(x,with) memset(x,with,sizeof(x))  
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define sz(a) int((a).size())

typedef pair<int,int> pii;
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;


static const int dirV[5] = {-1, 0, 0, 1, 0};
static const int dirH[5] = {0, -1, 1, 0, 0};
int N, W, H;
int land[101][101], ans[101][101], flow_direction[101][101];

void dfs(int i, int j, int current_alpha, bool was_going_up)
{
	for(int dir=0; dir<4; dir++)
	{
		int ni = i + dirV[dir];
		int nj = j + dirH[dir];
		if( ni < 0 || ni >= H || nj < 0 || nj >= W ) continue;
		if( ans[ni][nj] != -1) continue;
//		cout << i << " " << j << " " << ni << " " << nj << " " << flow_direction[i][j] << endl;
		if( flow_direction[i][j] == dir  && !was_going_up ) // going down
		{
//			cout << i << " " << j << " " << ni << " " << nj << "---" << endl;
			ans[ni][nj] = current_alpha;
			dfs(ni, nj, current_alpha, false);
		}
		if( flow_direction[ni][nj] + dir == 3 ) // going up
		{
			ans[ni][nj] = current_alpha;
			dfs(ni, nj, current_alpha, true);
		}
	}
}

int main()
{
	cin >> N;
	for(int c=1; c<=N; c++)
	{
		cin >> H >> W;
		for(int i=0; i<101; i++) for(int j=0; j<101; j++) land[i][j] = 10010;

		for(int i=0; i<H; i++)
		{
			for(int j=0; j<W; j++)
			{
				int altitude;
				cin >> altitude;
				land[i][j] = altitude;
			}
		}

		// 0N, 1W, 2E, 3S, 4 sink
		for(int i=0; i<101; i++) for(int j=0; j<101; j++) flow_direction[i][j] = 4;

		for(int i=0; i<H; i++)
		{
			for(int j=0; j<W; j++)
			{
				int flowdir = 4, min = land[i][j];
				for(int k=0; k<4; k++)
				{
					int ni = i+dirV[k], nj = j+dirH[k];
					if( ni < 0 || ni >= H || nj < 0 || nj >= W ) continue;
					if( land[i][j] > land[ni][nj] && land[ni][nj] < min )
					{
						min = land[ni][nj];
						flowdir = k;
					}
				}
				flow_direction[i][j] = flowdir;
			}
		}

		int current_alpha = 0;
		for(int i=0; i<101; i++) for(int j=0; j<101; j++) ans[i][j] = -1;
		for(int i=0; i<H; i++)
		{
			for(int j=0; j<W; j++)
			{
				if(ans[i][j] != -1) continue;
				ans[i][j] = current_alpha;
				// find all others
				dfs(i, j, current_alpha, false);

				current_alpha++;
			}
		}

		cout << "Case #" << c << ":" << endl;
		for(int i=0; i<H; i++)
		{
			for(int j=0; j<W-1; j++)
			{
				cout << (char)(ans[i][j] + 'a') << " ";
			}
			cout << (char)(ans[i][W-1] + 'a') << endl;
		}
	}

	return 0;
}
