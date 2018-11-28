// snapper_chain.cpp : Defines the entry point for the console application.
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
	int64_t N, K;
} case_t;

typedef std::list<case_t> case_list_t;

void load_data(std::istream &in, case_list_t &cl)
{
	int64_t T;

	in >> T;

	for ( ; T > 0; T--) {
		//
		case_t c;

		in >> c.N;
		in >> c.K;

		cl.push_back(c);
	}
}

std::string compute(case_t c)
{
	int64_t K = c.K;
	int64_t N = c.N;

	std::string s;
	while (K > 0) {
		s += ((K % 2) == 0) ? '0' : '1';
		K /= 2;
	}

	for (std::string::const_iterator i = s.begin(); i != s.end(); i++) {
		if ((*i) == '0')
			break;

		N -= 1;
		if (N == 0)
			break;
	}

	return (N == 0) ? "ON" : "OFF";
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
//	std::ifstream in("A-small-attempt0.in");
//	std::ofstream out("A-small-attempt0.out");
	std::ifstream in("A-large.in");
	std::ofstream out("A-large.out");

	case_list_t cl;

	load_data(in, cl);
	process_data(out, cl);

	return 0;
}
