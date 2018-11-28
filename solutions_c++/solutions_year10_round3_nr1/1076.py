#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <cassert>
#include <typeinfo>

using namespace std;

#define	Int	int
#define UInt unsigned int
//#define	Int	long long int;

#define rep(i,n) for(UInt i=0, i##_size_dummy=n; i<i##_size_dummy; ++i)

#define	MAKE_TEST	(0x01<<0)
#define	SOLVE_TEST	(0x01<<1)
#define	SOLVE_SMALL	(0x01<<2)
#define	SOLVE_LARGE	(0x01<<3)

#define	PROBREM	"A"
#define MODE	SOLVE_LARGE


namespace
{
#if (MODE & MAKE_TEST)
	const string IN_FILE_NAME(PROBREM"-test.in");
#elif (MODE & SOLVE_TEST)
	const string IN_FILE_NAME(PROBREM"-test.in");
	const string OUT_FILE_NAME(PROBREM"-test.out");
#elif (MODE & SOLVE_SMALL)
	const string IN_FILE_NAME(PROBREM"-small-attempt0.in");
	const string OUT_FILE_NAME(PROBREM"-small.out");
#elif (MODE & SOLVE_LARGE)
	const string IN_FILE_NAME(PROBREM"-large.in");
	const string OUT_FILE_NAME(PROBREM"-large.out");
#endif
}

struct Data
{
	int id;
	int left;
	int right;
};
typedef vector<Data> DataList;

// vector‚ð“ñŽŸŒ³ƒe[ƒuƒ‹‚Æ‚µ‚ÄŽg‚¢‚½‚¢ê‡
// ‰¡‚©‚çc‚Ö
// “Y‚¦Žš‚Ì”ÍˆÍ:[1, size]
const Data &
get_data_of_i_j(const DataList &source, UInt i, UInt j)
{
	assert(!source.empty() && source.size()>=i*j);

	return source[i*j-1];
}

void
make_test(ofstream &out)
{
	assert(out.is_open());

	int case_num = 15;
	out << case_num << endl;

	rep(cn, case_num)
	{
		int rope_num = max(1, rand()%1000);

		out << rope_num << endl;

		rep(i, rope_num)
		{
			int left_side  = max(1, rand()%10000);
			int right_side = max(1, rand()%10000);
			out << left_side << " " << right_side << endl;
		}
	}
}

void
solve(ifstream &in, ofstream &out)
{
	assert(in.is_open() && out.is_open());

	int case_num;
	in >> case_num;

	rep(cn, case_num)
	{
		int rope_num;
		in >> rope_num;
		vector<int> left_side(rope_num);
		vector<int> right_side(rope_num);

		rep(i, rope_num)
		{
			in >> left_side[i];
			in >> right_side[i];
		}

		int intersection_num = 0;
		rep(i, rope_num)
		{
			rep(j, rope_num)
			{
				if ((left_side[i] < left_side[j] && right_side[i] > right_side[j] ) ||
					(left_side[i] > left_side[j] &&	right_side[i] < right_side[j] ) )
				{
					++intersection_num;
				}
			}
		}
		intersection_num /= 2;

		out << "Case #" << cn+1 << ": ";
		out << "" << intersection_num;	// output!
		//rep(i, rope_num)
		//{
		//	out << left_side[i] << " ";
		//	out << right_side[i] << " ";
		//}
		out << endl;
	}
}

int main()
{
#if (MODE&MAKE_TEST)
	make_test(ofstream(IN_FILE_NAME.c_str()));
#else
	solve(ifstream(IN_FILE_NAME.c_str()), ofstream(OUT_FILE_NAME.c_str()));
#endif
	return 0;
}
