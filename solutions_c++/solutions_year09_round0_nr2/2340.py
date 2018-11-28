#include<iostream>
#include<vector>
#include<set>

using namespace std;

enum FlowDirection
{
	None, North, West, East, South
};

struct cell
{
	int altitude;
	FlowDirection flowdir;
	char basinLabel;
};

vector< vector<cell> > grid;
int H, W;

set<int> nextlist;

inline int addr(int row, int col)
{
	return (row << 8) + col;
}

void label(int row, int col, char basinLabel)
{
	cell & thisCell = grid[row][col],
		& northCell = grid[row-1][col],
		& westCell = grid[row][col-1],
		& eastCell = grid[row][col+1],
		& southCell = grid[row+1][col];

	thisCell.basinLabel = basinLabel;

	if(northCell.basinLabel == 0)
		if(thisCell.flowdir == North or northCell.flowdir == South)
			label(row-1, col, basinLabel);
		else
			nextlist.insert(addr(row-1, col));

	if(westCell.basinLabel == 0)
		if(thisCell.flowdir == West or westCell.flowdir == East)
			label(row, col-1, basinLabel);
		else
			nextlist.insert(addr(row, col-1));

	if(eastCell.basinLabel == 0)
		if(thisCell.flowdir == East or eastCell.flowdir == West)
			label(row, col+1, basinLabel);
		else
			nextlist.insert(addr(row, col+1));

	if(southCell.basinLabel == 0)
		if(thisCell.flowdir == South or southCell.flowdir == North)
			label(row+1, col, basinLabel);
		else
			nextlist.insert(addr(row+1, col));
}

int main()
{
	int T;
	cin >> T;

	for(int X = 1; X <= T; ++X)
	{
		cin >> H >> W;

		grid.resize(H + 2);

		for(int i = 1; i <= H; ++i)
		{
			grid[i].resize(W + 2);

			for(int j = 1; j <= W; ++j)
			{
				cin >> grid[i][j].altitude;
				grid[i][j].basinLabel = 0;
			}
		}

		grid[0].resize(W + 2);
		grid[H + 1].resize(W + 2);

		for(int i = 1; i <= H; ++i)
		{
			grid[i][0].altitude = 10000;
			grid[i][0].flowdir = East;
			grid[i][0].basinLabel = -1;

			grid[i][W + 1].altitude = 10000;
			grid[i][W + 1].flowdir = West;
			grid[i][W + 1].basinLabel = -1;
		}

		for(int j = 1; j <= W; ++j)
		{
			grid[0][j].altitude = 10000;
			grid[0][j].flowdir = South;
			grid[0][j].basinLabel = -1;

			grid[H + 1][j].altitude = 10000;
			grid[H + 1][j].flowdir = North;
			grid[H + 1][j].basinLabel = -1;
		}

		for(int i = 1; i <= H; ++i)
		{
			for(int j = 1; j <= W; ++j)
			{
				int n = grid[i-1][j].altitude,
					w = grid[i][j-1].altitude,
					e = grid[i][j+1].altitude,
					s = grid[i+1][j].altitude,
					a = grid[i][j].altitude;

				if(n <= w)
					if(n <= e)
						if(n <= s)
							if(n < a)
								grid[i][j].flowdir = North;
							else
								grid[i][j].flowdir = None;
						else
							if(s < a)
								grid[i][j].flowdir = South;
							else
								grid[i][j].flowdir = None;
					else
						if(e <= s)
							if(e < a)
								grid[i][j].flowdir = East;
							else
								grid[i][j].flowdir = None;
						else
							if(s < a)
								grid[i][j].flowdir = South;
							else
								grid[i][j].flowdir = None;
				else
					if(w <= e)
						if(w <= s)
							if(w < a)
								grid[i][j].flowdir = West;
							else
								grid[i][j].flowdir = None;
						else
							if(s < a)
								grid[i][j].flowdir = South;
							else
								grid[i][j].flowdir = None;
					else
						if(e <= s)
							if(e < a)
								grid[i][j].flowdir = East;
							else
								grid[i][j].flowdir = None;
						else
							if(s < a)
								grid[i][j].flowdir = South;
							else
								grid[i][j].flowdir = None;
			}
		}

		nextlist.clear();

		nextlist.insert(addr(1, 1));
		char basinLabel = 'a';

		do
		{
			set<int>::const_iterator f = nextlist.begin();

			int n = *f;

			nextlist.erase(f);

			int row = n >> 8,
				col = n & 0xFF;

			if(grid[row][col].basinLabel == 0)
			{
				label(row, col, basinLabel);
				basinLabel++;
			}
		}
		while(!nextlist.empty());

		cout << "Case #" << X << ":\n";

		for(int i = 1; i <= H; ++i)
		{
			for(int j = 1; j <= W; ++j)
				cout << grid[i][j].basinLabel << " ";

			cout << '\n';
		}
	}

	return 0;
}