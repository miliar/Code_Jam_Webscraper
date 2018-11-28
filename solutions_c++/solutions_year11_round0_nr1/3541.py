// bot_trust.cpp : Defines the entry point for the console application.
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

typedef struct _move_t {
	char r;
	int p;
} move_t;

typedef struct _case_t {
	std::list<int> O, B;
	std::list<move_t> M;
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
		int N = strtoul(v.at(j++).c_str(), NULL, 0);

		for ( ; N > 0; N--) {
			move_t m;

			m.r = v.at(j).at(0);
			m.p = strtol(v.at(j + 1).c_str(), NULL, 0);
			c.M.push_back(m);

			if (m.r == 'O')
				c.O.push_back(m.p);
			else
				c.B.push_back(m.p);

			j += 2;
		}

		//
		cl.push_back(c);
	}
}

int compute(case_t c)
{
	// solve
	int o = 1, b = 1;
	int t = 0;

	while (c.M.empty() == false) {
		move_t m = c.M.front();
		bool b_push = false, o_push = false;	// mutually exlusive
		if (c.B.empty() == false) {
			int B = c.B.front();
			if (b < B)							// move forward towards target
				b += 1;
			else
			if (b > B)							// move backward towards target
				b -= 1;
			else
			if ((b == m.p) && (m.r == 'B'))		// target reached, it's my time to push?
				b_push = true;
		}
		if (c.O.empty() == false) {
			int O = c.O.front();
			if (o < O)
				o += 1;
			else
			if (o > O)
				o -= 1;
			else
			if ((o == m.p) && (m.r == 'O'))
				o_push = true;
		}

		if (b_push == true) {
			c.B.pop_front();
			c.M.pop_front();
		} else
		if (o_push == true) {
			c.O.pop_front();
			c.M.pop_front();
		}

		t += 1;
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
