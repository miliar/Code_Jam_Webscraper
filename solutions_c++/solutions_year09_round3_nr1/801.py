// all_your_base.cpp : Defines the entry point for the console application.
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

typedef std::list<std::string> symbols_list_t;



void load_data(std::istream &in, symbols_list_t &sl)
{
	long long T;

	in >> T;

	for ( ; T > 0; T--) {
		//
		std::string v;

		in >> v;

		sl.push_back(v);
	}
}

std::string filter_unique(const std::string &s)
{
	bool m[256];
	memset(m, 0, sizeof(bool) * 256);

	std::string r;

	for (std::string::size_type i = 0; i < s.length(); i++) {
		if (m[s[i]] == false) {
			m[s[i]] = true;
			r += s[i];
		}
	}

	return r;
}

std::string build_base(const std::string &s)
{
	bool m[256];
	memset(m, 0, sizeof(bool) * 256);

	std::string aux;
	aux = filter_unique(s);
	std::string r;

	r += aux[1];	// zero
	r += aux[0];	// one

	m[r[0]] = true;
	m[r[1]] = true;

	for (std::string::size_type i = 0; i < s.length(); i++) {
		if (m[s[i]] == false) {
			m[s[i]] = true;
			r += s[i];
		}
	}

	return r;
}

uint64_t find_unit(const std::string &s, char c)
{
	uint64_t u = 0;

	for (std::string::size_type i = 0; i < s.length(); i++) {
		if (c == s[i]) {
			u = i;
			break;
		}
	}

	return u;
}

uint64_t compute(std::string s)
{
	std::string aux;
	aux = build_base(s);
	uint64_t b = aux.length();
	uint64_t m = 1;
	uint64_t r = 0;

	for (int i = (s.length() - 1); i >= 0; i--) {
		r += find_unit(aux, s[i]) * m;
		m *= b;
	}

	return r;
}

void process_data(std::ostream &out, symbols_list_t &sl)
{
	for (int i = 0; sl.empty() == false; i++) {
		out << "Case #" << (i + 1) << ": " << compute(sl.front()) << std::endl;

		sl.pop_front();
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

	symbols_list_t sl;

	load_data(in, sl);
	process_data(out, sl);

	return 0;
}
