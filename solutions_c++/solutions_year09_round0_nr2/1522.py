#include <iostream>
#include <vector>

using namespace std;

int alts[102][102];

int conn[102][102][4];

int memb[102][102];
char names[102*102];

void add(int membership, int x, int y, int W)
{
	if (memb[x][y] != x + y * (W+1)) return;

	memb[x][y] = membership;
	if (conn[x][y][0])
	{
		add(membership, x, y-1, W);
	}
	if (conn[x][y][1])
	{
		add(membership, x-1, y, W);
	}	
	if (conn[x][y][2])
	{
		add(membership, x+1, y, W);
	}	
	if (conn[x][y][3])
	{
		add(membership, x, y+1, W);
	}	
}

int main(int argc, char** argv)
{	
	int T;
	cin >> T;
	
	for (int i = 0; i < T; i++)
	{
		
		int H, W;
		cin >> H >> W;
		
		for (int j = 0; j <= H + 1; j++)
		{
			for (int k = 0; k <= W + 1; k++)
			{
				if (j == 0 || j == H+1 || k == 0 || k == W+1)
				{
					alts[k][j] = 10001;
				}
				else
				{
					int a;
					cin >> a;
	
					alts[k][j] = a;
				}
			}
		}
		
		// build connections
		memset(conn, 0, sizeof(conn));
		for (int j = 1; j <= H; j++)
		{
			for (int k = 1; k <= W; k++)
			{
				vector<int> neighbours;
				neighbours.push_back(alts[k][j-1]*4 + 0);
				neighbours.push_back(alts[k-1][j]*4 + 1);
				neighbours.push_back(alts[k+1][j]*4 + 2);
				neighbours.push_back(alts[k][j+1]*4 + 3);
				
				sort(neighbours.begin(), neighbours.end());
				
				if (neighbours[0] / 4 < alts[k][j])
				{
					conn[k][j][neighbours[0] % 4] = 1;
					switch (neighbours[0] % 4)
					{
						case 0:
							conn[k][j-1][3] = 1;
							break;
						case 1:
							conn[k-1][j][2] = 1;
							break;
						case 2:
							conn[k+1][j][1] = 1;
							break;
						case 3:
							conn[k][j+1][0] = 1;
							break;
					}
				}
			}
		}
		
		// init membership
		for (int j = 1; j <= H; j++)
		{
			for (int k = 1; k <= W; k++)
			{
				memb[k][j] = k + j*(W+1);
			}
		}
		
		// connect
		for (int j = 1; j <= H; j++)
		{
			for (int k = 1; k <= W; k++)
			{
				add(memb[k][j], k, j, W);
			}
		}
		
		// rename
		memset(names, 0, sizeof(names));
		char currname = 'a';
		for (int j = 1; j <= H; j++)
		{
			for (int k = 1; k <= W; k++)
			{
				if (names[memb[k][j]] == 0)
				{
					names[memb[k][j]] = currname;
					currname++;
				}
			}
		}
		
		// print
		cout << "Case #" << i + 1 << ":" << endl;
		for (int j = 1; j <= H; j++)
		{
			for (int k = 1; k <= W; k++)
			{
				cout << names[memb[k][j]] << " ";
			}
			cout << endl;
		}
		
	}
}