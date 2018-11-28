#include <vector>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

int H, W, tB;
vector< vector< int > > basin, alt;

int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};

int Check(int x, int y)
{
	return x >= 0 && x < H && y >= 0 && y < W;
}

void go( int x, int y)
{
	//cout << "go " << x << ' ' << y << endl;
	if( basin[x][y] != -1 )
		return;

	int low = alt[x][y];
	for(int i = 0; i < 4; i++)
	{
		if( !Check(x+dx[i], y+dy[i]) )
			continue;

		low = min( low, alt[x+dx[i]][y+dy[i]]);
	}
	//cout << "low " << low << endl;

	if( low == alt[x][y] )
	{
		basin[x][y] = tB++;
		return;
	}

	for(int i = 0; i < 4; i++)
	{
		if( !Check(x+dx[i], y+dy[i]) )
			continue;

		if( alt[x+dx[i]][y+dy[i]] == low)
		{
			go(x+dx[i], y+dy[i]);
			basin[x][y] = basin[x+dx[i]][ y+dy[i]];
			return;
		}
	}
}

int main()
{
	int T;
	cin >> T;
	
	for( int t = 1; t <= T; t++)
	{
		cin >> H >> W;

		basin.assign( H, vector<int>(W, -1) );
		alt.assign( H, vector<int>(W, -1) );

		for(int i = 0; i < H; i++)
			for(int j = 0; j < W; j++)
				cin >> alt[i][j];

		tB = 0;
		for(int i = 0; i < H; i++)
			for(int j = 0; j < W; j++)
				go(i,j);

		cout << "Case #" << t << ": " << endl;
		for(int i = 0; i < H; i++)
		{
			for(int j = 0; j < W; j++)
			{
				if( j )
					cout << ' ';
				cout << (char)(basin[i][j] + 'a');
			}

			cout << endl;
		}
	}
}