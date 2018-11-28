#include <iostream>
#include <fstream>
#include <vector>

std::vector < std::pair < __int64, int> > boxes;
std::vector < std::pair < __int64, int> > toys;
int n;
int m;
__int64 gl_res;
__int64 max_;

void rec(int i, int j, __int64 st)
{
	if (st > max_)
		max_ = st;
	if (i >= n || j >= m)
		return;
	if (boxes[i].second == toys[j].second)
	{
		if (boxes[i].first == toys[j].first)
		{
			rec(i + 1, j + 1, st + boxes[i].first);
		}
		else if (boxes[i].first > toys[j].first)
		{
			__int64 cur_min = toys[j].first;
			boxes[i].first -= cur_min;
			rec(i, j + 1, st + cur_min);
			boxes[i].first += cur_min;
		}
		else 
		{
			__int64 cur_min = boxes[i].first;
			toys[j].first -= cur_min;
			rec(i + 1, j, st + cur_min);
			toys[j].first += cur_min;
		}
	}
	else 
	{
		rec(i + 1, j, st);
		rec(i, j + 1, st);
	}
	
}

__int64 stupid_sol()
{
	__int64 res = 0;
	if (n > 3)
	{
		std::cout << "N is too big!!!!" << std::endl;
		return -1;
	}
	gl_res = 0;
	max_ = 0;
	rec(0, 0, 0);
	return max_;
}

int main()
{
	int tt;
	std::ifstream input("input_c.txt");
	std::ofstream output("output_c.txt");
	input >> tt;
	for (int t = 1; t <= tt; ++t)
	{
		
		input >> n >> m;
		boxes.clear();
		toys.clear();
		for (int i = 0; i < n; ++i)
		{
			__int64 kol;
			int type;
			input >> kol >> type;
			boxes.push_back( std::make_pair(kol, type));
		}
		for (int i = 0; i < m; ++i)
		{
			__int64 kol;
			int type;
			input >> kol >> type;
			toys.push_back( std::make_pair(kol, type));
		}
		output << "Case #" << t << ": " << stupid_sol() << std::endl;
	}
	input.close();
	output.close();
	return 0;
}