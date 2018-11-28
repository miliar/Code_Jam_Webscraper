#include <vector>
#include <fstream>
#include <algorithm>
using namespace std;

bool blue = false, red = false;

void check_horizontal(vector<vector<char> > map, int k)
{
	for(int i = 0; i < map.size(); ++i)
	{
		int b = 0, r = 0;
		for(int j = 0; j < map[i].size(); ++j)
		{
			if(map[i][j] == 'R')
			{
				b = 0;
				r++;
			}
			else if(map[i][j] == 'B')
			{
				r = 0;
				b++;
			}
			else
			{
				b = 0;
				r = 0;
			}
			if(b >= k)
			{
				blue = true;
			}
			if(r >= k)
			{
				red = true;
			}
		}
	}
}

void check_vertical(vector<vector<char> > map, int k)
{
	for(int i = 0; i < map.size(); ++i)
	{
		int b = 0, r = 0;
		for(int j = 0; j < map[i].size(); ++j)
		{
			if(map[j][i] == 'R')
			{
				b = 0;
				r++;
			}
			else if(map[j][i] == 'B')
			{
				r = 0;
				b++;
			}
			else
			{
				b = 0;
				r = 0;
			}
			if(b >= k)
			{
				blue = true;
			}
			if(r >= k)
			{
				red = true;
			}
		}
	}
}

void check_diagonal(vector<vector<char> > map, int k)
{
	for(int i = 0; i < map.size(); ++i)
	{
		int b = 0, r = 0;
		for(int j = 0; (j + i)< map[i].size(); ++j)
		{
			if(map[j + i][j] == 'R')
			{
				b = 0;
				r++;
			}
			else if(map[j + i][j] == 'B')
			{
				r = 0;
				b++;
			}
			else
			{
				b = 0;
				r = 0;
			}
			if(b >= k)
			{
				blue = true;
			}
			if(r >= k)
			{
				red = true;
			}
		}
	}
	for(int i = 0; i < map.size(); ++i)
	{
		int b = 0, r = 0;
		int max = map[i].size() - 1;
		for(int j = 0; (j + i)< map[i].size(); ++j)
		{
			if(map[j + i][max - j] == 'R')
			{
				b = 0;
				r++;
			}
			else if(map[j + i][max - j] == 'B')
			{
				r = 0;
				b++;
			}
			if(b >= k)
			{
				blue = true;
			}
			if(r >= k)
			{
				red = true;
			}
		}
	}
}

int main()
{
	ifstream cin("A-small-attempt1.in");
	ofstream cout("A-small-attempt1.out");
	int cases = 0;
	cin >> cases;
	for(int t = 0; t < cases; ++t)
	{
		blue = false;
		red = false;
		int n = 0, k = 0;
		cin >> n >> k;

		vector<vector<char> > map(n, vector<char>(n));
		for(int i = 0; i < n; ++i)
		{
			for(int j = 0; j < n; ++j)
			{
				cin >> map[i][j];
			}
		}

		for(int i = 0; i < map.size(); ++i)
		{
			reverse(map[i].begin(), map[i].end());
			int index = 0, count = 0;
			while(index != map.size())
			{
				if(map[i][index] == '.')
				{
					map[i].erase(map[i].begin() + index);
					map[i].push_back('.');
					count++;
				}
				else
				{
					index++;
				}
				if(count == map.size())
				{
					break;
				}
			}
			reverse(map[i].begin(), map[i].end());
		}

		check_horizontal(map, k);
		check_vertical(map, k);
		check_diagonal(map, k);

		cout << "Case #" << t + 1 << ": ";
		if(blue && red)
		{
			cout << "Both";
		}
		else if(blue)
		{
			cout << "Blue";
		}
		else if(red)
		{
			cout << "Red";
		}
		else
		{
			cout << "Neither";
		}
		cout << endl;
	}
	return 0;
}