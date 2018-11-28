#include <iostream>
#include <utility>
#include <deque>

#define INSIDE(H,W,h,w) ((h>=0)&&(h<H)&&(w>=0)&&(w<W))
#define UNREACHABLE     999999

using namespace std;

typedef pair<int, int> Cell;

enum DIR {NORTH, WEST, EAST, SOUTH, NONE};

Cell get_neighbor(int h, int w, DIR dir)
{
	Cell p;
	switch(dir)
	{
	case NORTH:
		p.first = h - 1;
		p.second = w;
		break;
	case WEST:
		p.first = h;
		p.second = w - 1;
		break;
	case EAST:
		p.first = h;
		p.second = w + 1;
		break;
	case SOUTH:
		p.first = h + 1;
		p.second = w;
		break;
	default:
		p.first = -1;
		p.second = -1;
	}
	return p;
}

DIR get_opposite(DIR dir)
{
	switch(dir)
	{
	case NORTH:
		return SOUTH;
	case WEST:
		return EAST;
	case EAST:
		return WEST;
	case SOUTH:
		return NORTH;
	default:
		return NONE;
	}
}

void main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out", "w", stdout);

	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		int H, W;
		cin >> H >> W;
		int altitudes[120][120];
		char label[120][120];
		DIR from[120][120][4];
		DIR to[120][120];
		for (int h = 0; h < H; h++)
			for (int w = 0; w < W; w++)
			{
				cin >> altitudes[h][w];
				label[h][w] = ' ';
				for (int k = 0; k < 4; k++)
					from[h][w][k] = NONE;
				to[h][w] = NONE;
			}

		for (int h = 0; h < H; h++)
		{
			for (int w = 0; w < W; w++)
			{
				int naltitudes[4];
				for (int dir = NORTH; dir < NONE; dir++)
				{
					Cell neighbor = get_neighbor(h, w, (DIR)dir);
					if (INSIDE(H, W, neighbor.first, neighbor.second))
						naltitudes[dir] = altitudes[neighbor.first][neighbor.second];
					else
						naltitudes[dir] = UNREACHABLE;
				}

				int lowest = altitudes[h][w];
				DIR toDir = NONE;
				for (int i = 0; i < 4; i++)
				{
					if (naltitudes[i] < lowest)
					{
						lowest = naltitudes[i];
						toDir = (DIR)i;
					}
				}
				if (toDir != NONE)
				{
					Cell dest_neighbor = get_neighbor(h, w, toDir);
					to[h][w] = toDir;
					int k = 0;
					for (k = 0; k < 4; k++)
					{
						if (from[dest_neighbor.first][dest_neighbor.second][k] == NONE)
							break;
					}
					from[dest_neighbor.first][dest_neighbor.second][k] = get_opposite(toDir);
				}
			}
		}

		char currentL = 'a';
		for (int h = 0; h < H; h++)
		{
			for (int w = 0; w < W; w++)
			{
				if (label[h][w] != ' ')
					continue;

				deque<Cell> q;
				Cell c;
				c.first = h;
				c.second = w;
				q.push_back(c);
				label[h][w] = currentL;
				while(!q.empty())
				{
					Cell cell = q.front();
					q.pop_front();

					int dirTo = to[cell.first][cell.second];

					if (dirTo != NONE)
					{
						Cell dest = get_neighbor(cell.first, cell.second, (DIR)dirTo);
						if (label[dest.first][dest.second] == ' ')
						{
							label[dest.first][dest.second] = currentL;
							q.push_back(dest);
						}
					}

					for (int k = 0; k < 4; k++)
					{
						int dirFrom = from[cell.first][cell.second][k];
						if (dirFrom != NONE)
						{
							Cell dest = get_neighbor(cell.first, cell.second, (DIR)dirFrom);
							if (label[dest.first][dest.second] == ' ')
							{
								label[dest.first][dest.second] = currentL;
								q.push_back(dest);
							}
						}
						else
							break;
					}
				}
				currentL++;
			}
		}

		cout << "Case #" << t+1 << ":" << endl;
		cerr << "Case #" << t+1 << ":" << endl;
		for (int h = 0; h < H; h++)
		{
			for (int w = 0; w < W; w++)
			{
				cout << label[h][w] << " ";
			}
			cout << endl;
		}

	}
}