#include <iostream>
#include <vector>

using namespace std;

int ter[100][100];
int H;
int W;
char basin[100][100];
char curbasin;
vector<int> marked;

int alt(int x, int y)
{
	if (x < 0 || x >= W || y < 0 || y >= H)
		return 20000;
	else
		return ter[x][y];
}

void examine(int x, int y)
{
	for(;;)
	{
		int foundbasin = 0;
		if (!basin[x][y])
		{
			marked.push_back(x*100+y);
			
			int thisalt = alt(x,y);
			int bestx, besty, testalt, min = thisalt;
			
			testalt = alt(x, y-1); // north
			if (testalt < min)
			{
				bestx = x; besty = y-1; min = testalt;
			}
			testalt = alt(x-1, y); // west
			if (testalt < min)
			{
				bestx = x-1; besty = y; min = testalt;
			}
			testalt = alt(x+1, y); // east
			if (testalt < min)
			{
				bestx = x+1; besty = y; min = testalt;
			}
			testalt = alt(x, y+1); // south
			if (testalt < min)
			{
				bestx = x; besty = y+1; min = testalt;
			}
			
			if (min == thisalt) // This is a basin
			{
				foundbasin = 1;
			}
			else
			{
				x = bestx; y = besty;
			}
		}
		
		if (basin[x][y] || foundbasin)
		{
			char listbasin;
			if (basin[x][y])
				listbasin = basin[x][y];
			else
			{
				listbasin = curbasin;
				curbasin++;
			}
			for (int i = 0; i < marked.size(); i++)
			{
				basin[marked[i]/100][marked[i]%100] = listbasin;
			}
			marked.clear();
			break;
		}
	}
}

int main(int argc, char *argv[])
{
	int T;	// no. maps
	cin >> T;
	
	for (int t = 0; t < T; t++)
	{
		cin >> H >> W;
		for (int y = 0; y < H; y++)
			for (int x = 0; x < W; x++)
				cin >> ter[x][y];
		
		curbasin = 'a';
		marked.clear();
		for (int y = 0; y < 100; y++)
			for (int x = 0; x < 100; x++)
				basin[x][y] = (char)0;
			
		for (int y = 0; y < H; y++)
			for (int x = 0; x < W; x++)
			{
				examine(x, y);
			}
		
		cout << "Case #" << t+1 << ":" << endl;
		for (int y = 0; y < H; y++)
			for (int x = 0; x < W; x++)
			{
				cout << basin[x][y];
				if (x == W-1)
					cout << endl;
				else
					cout << " ";
			}
	}
	
	return 0;
}
