// the_next_number.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <algorithm>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <string>


typedef std::list<long long> numbers_list_t;



void load_data(std::istream &in, numbers_list_t &nl)
{
	long long T;

	in >> T;

	for (long long k = 0U; k < T; k++) {
		//
		long long v;

		in >> v;

		nl.push_back(v);
	}
}

void frequency(long long n, long long F[10])
{
	memset(F, 0, sizeof(long long) * 10);
	F[0] = 100000000000000000;

	do {
		F[(n % 10)] += 1;
		n /= 10;
	} while (n > 0);
}

long long next_number(long long n)
{
	//
	long long F[10];

	frequency(n, F);

	//
	long long n1;

	for (n1 = n + 1; ; n1++) {
		long long F1[10];
		frequency(n1, F1);

		if (memcmp(F, F1, sizeof(long long) * 10) == 0)
			break;
	}

	return n1;
}

std::string next_number(std::string s)
{
	std::string aux = s;

	while (true) {
		std::list<std::string> perms;
		std::sort(aux.begin(), aux.end());
		do
			perms.push_back(aux);
		while (std::next_permutation(aux.begin(), aux.end()));
		perms.sort();

		for (std::list<std::string>::const_iterator i = perms.begin(); i != perms.end(); i++) {
			if ((*i).compare(s) > 0)
				return (*i);
		}

		aux = aux + "0";
		s = "0" + s;
	}

	return "";
}

void process_data(std::ostream &out, numbers_list_t &nl)
{
	for (int i = 0; nl.empty() == false; i++) {
		char s[128];
		sprintf(s, "%ld", nl.front());

		out << "Case #" << (i + 1) << ": " << next_number(s) << std::endl;

		nl.pop_front();
	}
}


int _tmain(int argc, _TCHAR* argv[])
{
// 	std::ifstream in("sample.in");
//	std::ofstream out("sample.out");
	std::ifstream in("B-small-attempt2.in");
	std::ofstream out("B-small-attempt2.out");
//	std::ifstream in("B-large.in");
//	std::ofstream out("B-large.out");

	numbers_list_t nl;

	load_data(in, nl);
	process_data(out, nl);

	return 0;
}
