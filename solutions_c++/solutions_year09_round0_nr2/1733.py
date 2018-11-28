#include <iostream>
#include <vector>

using namespace std;

int id = 0;
int w, h;
int alt[100][100];
int reg[100][100];

bool on_field(int x, int y)
{
	if (x < 0 || y < 0 || x >= w || y >= h)
	{
		return false;
	}
	return true;
}
int get_sink_id(int x, int y)
{
	if (reg[y][x] != -1)
	{
		return reg[y][x];
	}
	
	int altn[5] = {
		alt[y][x],
		on_field(x, y - 1) ? alt[y - 1][x] : 100000,
		on_field(x - 1, y) ? alt[y][x - 1] : 100000,
		on_field(x + 1, y) ? alt[y][x + 1] : 100000,
		on_field(x, y + 1) ? alt[y + 1][x] : 100000
	};

	int min_index = 0;
	for (int i = 1; i < 5; ++i)
	{
		if (altn[i] < altn[min_index])
		{
			min_index = i;
		}
	}

	switch (min_index)
	{
	case 0:
		reg[y][x] = id++;
		break;
	case 1:
		reg[y][x] = get_sink_id(x, y - 1);
		break;
	case 2:
		reg[y][x] = get_sink_id(x - 1, y);
		break;
	case 3:
		reg[y][x] = get_sink_id(x + 1, y);
		break;
	case 4:
		reg[y][x] = get_sink_id(x, y + 1);
		break;
	}

	return reg[y][x];
}

int main()
{
	int t;

	cin >> t;

	for (int i = 0; i < t; ++i)
	{
		id = 0;
		cin >> h >> w;
		for (int y = 0; y < h; ++y) {
			for (int x = 0; x < w; ++x)
			{
				cin >> alt[y][x];
				reg[y][x] = -1;
			}
		}

		cout << "Case #" << i + 1 << ":" << endl;
		for (int y = 0; y < h; ++y) {
			for (int x = 0; x < w; ++x)
			{
				cout << (char)('a' + get_sink_id(x, y)) << ' ';
			}
			cout << endl;
		}
	}
	return 0;
}