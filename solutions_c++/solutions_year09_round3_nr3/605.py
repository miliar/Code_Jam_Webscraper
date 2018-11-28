#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <deque>
#include <list>
#include <map>
#include <bitset>
#include <functional>
#include <numeric>
#include <string>
#include <iterator>
#include <limits>
#include <sstream>
#include <iostream>
#include <stack>
#include <iomanip>

#include <boost/lexical_cast.hpp>
#include <boost/regex.hpp>
#define BOOST_REGEX_DYN_LIB

using namespace std;
using namespace boost;


int calc(vector<int> cells, int index, bool up)
{
	int total = 0;
	if(up)
	{
		if(index == cells.size() - 1)
			return 0;
		for(int i = index + 1; i < cells.size(); ++i)
		{
			if(cells[i] == 0)
				return total;
			++total;
		}
	}
	else
	{
		if(index == 0)
			return 0;
		for(int i = index - 1; i >= 0; --i)
		{
			if(cells[i] == 0)
				return total;
			++total;
		}
	}
	return total;
}

int calc_bribes(vector<int> cells, vector<int> order)
{
	int total = 0;
	for(int i = 0; i < order.size(); ++i)
	{
		int index = order[i];
		int bribes = 0;
		bribes += calc(cells, index-1, true);
		bribes += calc(cells, index-1, false);
		total += bribes;
		cells[index-1] = 0;
	}
	return total;
}
int main()
{
	ifstream in("B.in");
	ofstream out("B.out");
	int cases = 0;
	in >> cases;

	for(int case_number = 0; case_number < cases; ++case_number)
	{
		int P, Q;
		in >> P >> Q;
		vector<int> cells(P, (1));
		vector<int> order(Q);
		for(int i = 0; i < Q; ++i)
		{
			in >> order[i];
		}
		vector<int> total_bribes;
		do
		{
			total_bribes.push_back(calc_bribes(cells, order));
		} while(next_permutation(order.begin(), order.end()));

		sort(total_bribes.begin(), total_bribes.end());

		out << "Case #" << case_number + 1 << ": " << total_bribes[0] << endl;
	}
}