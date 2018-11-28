#include <iostream>
#include <vector>
#include <algorithm>
#include <gmpxx.h>	/* GNU MP, http://gmplib.org/, link with -lgmp -lgmpxx */
#include <string>
#include <cmath>


using namespace std;

struct cell {
	double x;
	double y;
};

bool mysort(struct cell a, struct cell b)
{
	if (a.x < b.x)
		return true;
	if (b.x < a.x)
		return false;
	return (a.y < b.y);
}

vector<struct cell> cells;
int ncells = 0;

bool binsearch(int low, int high, int x, int y)
{
	//cout << "Binsearch called with low " << low << " high " << high << " x " << x << " y " << y << endl;
	if (high == low)
		return false;
	if (high < low)
		return false;
	if (high - low == 1)
		return false;
	int mid = (high - low) / 2 + low;
	if (cells[mid].x == x && cells[mid].y == y)
		return true;
	else
	{
		if (cells[mid].x > x)
		{
			high = mid;
			return binsearch(low, high, x, y);
		}
		if (cells[mid].x < x)
		{
			low = mid;
			return binsearch(low, high, x, y);
		}
		if (cells[mid].y < y)
		{
			low = mid;
			return binsearch(low, high, x, y);
		}
		high = mid;
		return binsearch(low, high, x, y);
	}
}

bool cellat(int x, int y)
{
	if (cells.size() == 0)
		return false;
	struct cell start, end;
	start = cells[0];
	end = cells[cells.size() - 1];
	if ((start.x == x && start.y == y) || (end.x == x && end.y == y))
		return true;
	if (binsearch(0, cells.size()-1, x, y))
	{
		//cout << "Cellat succeeded for " << x << " " << y << endl;
		return true;
	}
	//cout << "Cellat failed for " << x << " " << y << endl;
	return false;
}

int main (int argc, char *argv[])
{
	int T, t;
	cin >> T;
	for (t = 1; t <= T; t++)
	{
		int R;
		cin >> R;
		for (int r = 0; r < R; r++)
		{
			int x1, y1, x2, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			for (int x = x1; x <= x2; x++)
			{
				for (int y = y1; y <= y2; y++)
				{
					if (!cellat(x, y))
					{
						//cout << "initing cell at " << x << " " << y << endl;
						struct cell c;
						c.x = x;
						c.y = y;
						cells.push_back(c);
					}
				}
			}
		}
		sort(cells.begin(), cells.end(), mysort);
		
		long long steps = 0;
		
		while (cells.size() > 0)
		{
			/*cout << "Sorted cells:" << endl;
			for (int A = 0; A < cells.size(); A++)
			{
				cout << cells[A].x << " " << cells[A].y << endl;
			}*/
			//cout << "Vector size is " << cells.size() << endl;
			vector<struct cell> cells2;
			for (vector<struct cell>::iterator it = cells.begin(); it < cells.end(); it++)
			{
				//cout << "Testing cell at " << it->x << " " << it->y << endl;
				if (cellat(it->x - 1, it->y) || cellat(it->x, it->y-1))
				{
					//cout << "Keeping a cell at " << it->x << " " << it->y << endl;
					struct cell foo;
					foo.x = it->x;
					foo.y = it->y;
					cells2.push_back(foo);
				}
				else
				{
					//cout << "Killing a cell" << endl;
				}
				if (!cellat(it->x, it->y+1) && cellat(it->x - 1, it->y + 1))
				{
					//cout << "Babby at " << it->x << " " << it->y+1 << endl;
					struct cell foo;
					foo.x = it->x;
					foo.y = it->y+1;
					cells2.push_back(foo);
				}
			}
			cells.clear();
			cells = cells2;
			sort(cells.begin(), cells.end(), mysort);
			steps++;
		}
		
		
		cout << "Case #" << t << ": " << steps << endl;
	}
	
	return 0;
}


