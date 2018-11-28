#include <iostream>
#include <string>
#include <vector>

using namespace std;

enum Cell
{
	Empty, Red, Blue
};

enum Result
{
	RNeither, RRed, RBlue, RBoth
};

void show_table(const vector<vector<Cell> > &table)
{
	cerr << "----" << endl;
	for (size_t y = 0; y < table.size(); ++y)
	{
		for (size_t x = 0; x < table.size(); ++x)
		{
			switch (table[y][x])
			{
			case Empty:
//				cout << '.';
				break;
			case Red:
//				cout << 'R';
				break;
			case Blue:
//				cout << 'B';
				break;
			}
		}
		cerr << endl;
	}
}

void rotate(vector<vector<Cell> > *table)
{
	vector<vector<Cell> > temp(*table);

	for (size_t src_y = 0; src_y < table->size(); ++src_y)
	{
		for (size_t src_x = 0; src_x < table->size(); ++src_x)
		{
			size_t dest_x = table->size() - src_y - 1;
			size_t dest_y = src_x;
			temp[dest_y][dest_x] = (*table)[src_y][src_x];
		}
	}

	table->swap(temp);
}

void gravity(vector<vector<Cell> > *table)
{
	for (size_t x = 0; x < table->size(); ++x)
	{
		size_t bottom = table->size() - 1;
		for (int y = table->size() - 1; y >= 0; --y)
		{
			if ((*table)[y][x] != Empty)
			{
				(*table)[bottom][x] = (*table)[y][x];
				--bottom;
			}
		}
		for (int y = bottom; y >= 0; --y)
			(*table)[y][x] = Empty;
	}
}

bool test(const vector<vector<Cell> > &table, int k, Cell cell)
{
	for (int y = 0; y < table.size(); ++y)
	{
		for (int x = 0; x < table.size(); ++x)
		{
			if (table[y][x] != cell)
				continue;

			// Test for right.
			int x_in = x + 1;
			if (x <= table.size() - k)
			{
				while (x_in < x + k)
				{
					if (table[y][x_in] != cell)
						break;
					++x_in;
				}
				if (x_in == x + k)
					return true;
			}

			// Test for up.
			if (y < k - 1)
				continue;

			int y_in = y - 1;
			while (y_in > y - k)
			{
				if (table[y_in][x] != cell)
					break;
				--y_in;
			}
			if (y_in == y - k)
				return true;

			if (x <= table.size() - k)
			{
				x_in = x + 1;
				y_in = y - 1;
				while (y_in > y - k)
				{
					if (table[y_in][x_in] != cell)
						break;
					--y_in;
					++x_in;
				}
				if (y_in == y - k)
					return true;
			}

			if (x_in >= k - 1)
			{
				x_in = x - 1;
				y_in = y - 1;
				while (y_in > y - k)
				{
					if (table[y_in][x_in] != cell)
						break;
					--y_in;
					--x_in;
				}
				if (y_in == y - k)
					return true;
			}
		}
	}

	return false;
}

Result calc(const vector<vector<Cell> > &src, int k)
{
	vector<vector<Cell> > table(src);
	rotate(&table);
	show_table(table);

	gravity(&table);
	show_table(table);

	bool red = test(table, k, Red);
	bool blue = test(table, k, Blue);

	if (red)
	{
		if (blue)
			return RBoth;
		return RRed;
	}
	else if (blue)
		return RBlue;
	return RNeither;
}

int main()
{
	int num_cases;
	cin >> num_cases;
	cerr << "cases: " << num_cases << endl;

	for (int i = 0; i < num_cases; ++i)
	{
		int n, k;
		cin >> n >> k;
		cerr << "N: " << n << ", K: " << k << endl;
		cin.ignore();

		vector<vector<Cell> > table(n);
		for (int j = 0; j < n; ++j)
		{
			table[j].resize(n);
			string line;
			getline(cin, line);
			for (int m = 0; m < n; ++m)
			{
				switch (line[m])
				{
				case '.':
					table[j][m] = Empty;
					break;
				case 'R':
					table[j][m] = Red;
					break;
				case 'B':
					table[j][m] = Blue;
					break;
				}
			}
		}
		show_table(table);

		Result result = calc(table, k);
		cout << "Case #" << (i + 1) << ": ";
		switch (result)
		{
		case RNeither:
			cout << "Neither";
			break;
		case RRed:
			cout << "Red";
			break;
		case RBlue:
			cout << "Blue";
			break;
		case RBoth:
			cout << "Both";
			break;
		}
		cout << endl;
	}

	return 0;
}
