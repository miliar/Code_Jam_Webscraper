// rope_intranet.cpp : Defines the entry point for the console application.
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
	int64_t N;
	std::vector<int64_t> A;
	std::vector<int64_t> B;
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

		in >> N;

		c.N = N;

		for ( ; N > 0; N--) {
			int64_t Ai, Bi;

			in >> Ai;
			in >> Bi;

			c.A.push_back(Ai);
			c.B.push_back(Bi);
		}

		cl.push_back(c);
	}
}

int64_t compute(case_t c)
{
	int64_t t = 0;

	for (int i = 0; i < c.N; i++) {
		for (int j = i + 1; j < c.N; j++) {
			if ((c.B[i] > c.B[j] && c.A[i] < c.A[j]) ||
			   (c.B[i] < c.B[j] && c.A[i] > c.A[j]))
				t += 1;
		}
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
//	std::ifstream in("A-small-attempt1.in");
//	std::ofstream out("A-small-attempt1.out");
	std::ifstream in("A-large.in");
	std::ofstream out("A-large.out");

	case_list_t cl;

	load_data(in, cl);
	process_data(out, cl);

	return 0;
}
