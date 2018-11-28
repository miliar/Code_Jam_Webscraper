// magicka.cpp : Defines the entry point for the console application.
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

typedef struct _case_t {
	std::list<std::string> C, D;
	std::string N;
} case_t;

typedef std::list<case_t> case_list_t;

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

void load_data(std::istream &in, case_list_t &cl)
{
	unsigned int T;

	std::string s;
	std::getline(in, s);
	T = strtoul(s.c_str(), NULL, 0);

	for ( ; T > 0; T--) {
		//
		case_t c;

		//
		std::getline(in, s);

		if (s.empty() == true)
			continue;

		//
		std::vector<std::string> v;
		std::split(s, std::string(" "), v);

		//
		int j = 0;

		//
		unsigned int C, D, N;

		C = strtoul(v.at(j++).c_str(), NULL, 0);
		for ( ; C > 0; C--)
			c.C.push_back(v.at(j++));

		D = strtoul(v.at(j++).c_str(), NULL, 0);
		for ( ; D > 0; D--)
			c.D.push_back(v.at(j++));

		N = strtoul(v.at(j++).c_str(), NULL, 0);
		c.N = v.at(j++).substr(0, N);

		//
		cl.push_back(c);
	}
}

void apply_combination(std::string &s, const std::list<std::string> &C)
{
	for (std::list<std::string>::const_iterator i = C.begin(); i != C.end(); i++) {
		//
		char l1, l2, r1;

		l1 = (*i).at(0);
		l2 = (*i).at(1);
		r1 = (*i).at(2);

		//
		std::string::size_type k;
		char l = 0;

		for (std::string::size_type j = 0; j < s.length(); j++) {
			if ((l != 0) && (s.at(j) == l)) {	// found end of sequence marker
				s.erase(k, (j - k) + 1);
				s.insert(k, 1, r1);
				break;
			} else
			if (s.at(j) == l1) {		// set next marker
				k = j;
				l = l2;
			} else
			if (s.at(j) == l2) {		// set (other) next marker
				k = j;
				l = l1;
			} else {					// reset (no markers)
				l = 0;
			}
		}
	}
}

void apply_opposition(std::string &s, const std::list<std::string> &C)
{
	for (std::list<std::string>::const_iterator i = C.begin(); i != C.end(); i++) {
		//
		char l1, l2;

		l1 = (*i).at(0);
		l2 = (*i).at(1);

		//
		char l = 0;

		for (std::string::size_type j = 0; j < s.length(); j++) {
			if ((l != 0) && (s.at(j) == l)) {
				s.clear();
				break;
			} else
			if (s.at(j) == l1) {
				l = l2;
			} else
			if (s.at(j) == l2) {
				l = l1;
			}
		}
	}
}

std::string compute(case_t c)
{
	// solve
	std::string s;

	for (std::string::const_iterator i = c.N.begin(); i != c.N.end(); i++) {
		s += *i;

		apply_combination(s, c.C);
		apply_opposition(s, c.D);
	}

	// format
	std::string out;
	for (std::string::const_iterator j = s.begin(); j != s.end(); j++) {
		if (out.empty() == false)
			out += ", ";
		out += *j;
	}

	return "[" + out + "]";
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
//	std::ifstream in("B-small-attempt0.in");
//	std::ofstream out("B-small-attempt0.out");
	std::ifstream in("B-large.in");
	std::ofstream out("B-large.out");

	case_list_t cl;

	load_data(in, cl);
	process_data(out, cl);

	return 0;
}
