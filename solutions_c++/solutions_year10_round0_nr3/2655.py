// theme_park.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <fstream>
#include <sstream>
#include <bitset> 
#include <deque> 
#include <list>
#include <map>
#include <queue> 
#include <set>
#include <stack> 
#include <vector>
#include <string>
#include <limits>

typedef long long int64_t;
typedef unsigned long long uint64_t;

typedef struct _case_t {
	int64_t R, k;
	std::list<int64_t> G;
} case_t;

typedef std::list<case_t> case_list_t;

void load_data(std::istream &in, case_list_t &cl)
{
	int64_t T;

	in >> T;

	for ( ; T > 0; T--) {
		//
		case_t c;
		int64_t N;

		in >> c.R;
		in >> c.k;
		in >> N;

		//
		for ( ; N > 0; N--) {
			int64_t g;

			in >> g;
			c.G.push_back(g);
		}

		//
		cl.push_back(c);
	}
}

int64_t compute(case_t c)
{
	int64_t t = 0;

	for (; c.R > 0; c.R--) {
		std::list<int64_t> G;
		int64_t v = 0;

		while (c.G.empty() == false) {
			int64_t g = c.G.front();

			if (v + g > c.k)
				break;

			v += g;

			c.G.pop_front();

			G.push_back(g);
		}

		c.G.insert(c.G.end(), G.begin(), G.end());

		t += v;
	}

	return t;
}

void process_data(std::ostream &out, case_list_t &cl)
{
	for (int i = 0; cl.empty() == false; i++) {
		out << "Case #" << (i + 1) << ": " << compute(cl.front()) << std::endl;

		cl.pop_front();
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
// 	std::ifstream in("sample.in");
//	std::ofstream out("sample.out");
	std::ifstream in("C-small-attempt0.in");
	std::ofstream out("C-small-attempt0.out");
//	std::ifstream in("C-large.in");
//	std::ofstream out("C-large.out");

	case_list_t cl;

	load_data(in, cl);
	process_data(out, cl);

	return 0;
}
