// file_fix_it.cpp : Defines the entry point for the console application.
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
	std::list<std::string> N;
	std::list<std::string> M;
} case_t;

namespace std {

    template <class T, class C>
    void split(const T &source, const T &separator, C &items)
    {
        //
        items.clear();

        //
        T::size_type i = 0, j;

        do {
            //
            T value;

            j = source.find(separator, i);

            if (j != T::npos)
                value = source.substr(i, j - i);
            else
                value = source.substr(i);

            //
			if (value.empty() == false)
	            items.push_back(value);

            //
            i = j + separator.length();
        } while (j != T::npos);
    }

};

typedef std::list<case_t> case_list_t;

void load_data(std::istream &in, case_list_t &cl)
{
	int64_t T;

	in >> T;

	for ( ; T > 0; T--) {
		//
		case_t c;
		int64_t N, M;

		in >> N;
		in >> M;

		//
		std::string s;
		c.N.push_back("/");

		for ( ; N > 0; N--) {
			in >> s;
			c.N.push_back(s);
		}

		for ( ; M > 0; M--) {
			in >> s;
			c.M.push_back(s);
		}

		//
		cl.push_back(c);
	}
}

int64_t compute(case_t c)
{
	int64_t t = 0;

	for (std::list<std::string>::const_iterator i = c.M.begin(); i != c.M.end(); i++) {
		std::list<std::string> vTokens;
		std::split((*i), std::string("/"), vTokens);

		std::string s = "";
		for (std::list<std::string>::const_iterator j = vTokens.begin(); j != vTokens.end(); j++) {
			s += "/";
			s += *j;

			std::list<std::string>::const_iterator k = std::find(c.N.begin(), c.N.end(), s);
			if (k == c.N.end()) {
				c.N.push_back(s);
				t += 1;
			}
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
//	std::ifstream in("A-small-attempt0.in");
//	std::ofstream out("A-small-attempt0.out");
	std::ifstream in("A-large.in");
	std::ofstream out("A-large.out");

	case_list_t cl;

	load_data(in, cl);
	process_data(out, cl);

	return 0;
}
