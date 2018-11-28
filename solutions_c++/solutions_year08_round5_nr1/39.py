#ifndef DBG
#define DBG(x) x
#endif

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

#include <bitset>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <valarray>
#include <vector>
#include <fstream>

#include <tr1/unordered_set>
#include <tr1/unordered_map>

#include <boost/foreach.hpp>
#include <boost/rational.hpp>
// BGL

#include <gmpxx.h>
// mpz_class, mpq_class, mpf_class

using namespace std;
using namespace std::tr1;
using namespace boost;
#define DBL_ERR 1E-9

typedef long long s64;
typedef unsigned long long u64;

#define foreach_iter(i, c) for(typeof((c)op.begin()) i = (c).begin(); i != (c).end(); ++i)
#define foreach(r,c) BOOST_FOREACH(typeof((c).front())& r, c)

ifstream in;
ofstream out;

void init()
{
	
}

#define HALF 3010
#define TOT 6048
#define CL 32
#define INF 0x7fffffff

#define right _right

char up[TOT * TOT];
char right[TOT * TOT];
char draw[TOT * TOT];
char drawq[TOT * TOT];

#define P_(x, y) (((y) * TOT) + (x))
#define Q_(x, y) (((x) * TOT) + (y))

#define P(x, y) P_((x) + HALF, (y) + HALF)
#define Q(x, y) Q_((x) + HALF, (y) + HALF)

void solve_case(int casen)
{
	memset(up, 0, sizeof(up));
	memset(right, 0, sizeof(right));
	memset(draw, 0, sizeof(draw));
	memset(drawq, 0, sizeof(drawq));

	int dir = 0;
	int x = 0;
	int y = 0;
	int L;
	in >> L;
	for(int i = 0; i < L; ++i)
	{
		string S;
		int T;
		in >> S >> T;
		
		for(int j = 0; j < T; ++j)
		{
			for(int k = 0; k < (int)S.size(); ++k)
			{
				char c = S[k];
				if(c == 'L')
					dir = (dir + 1) & 3;
				if(c == 'R')
					dir = (dir - 1) & 3;
				if(c == 'F')
				{
					if(dir == 0)
					{
						up[P(x, y)] = 1;
						++y;
					}
					else if(dir == 1)
					{
						--x;
						right[Q(x, y)] = 1;
					}
					else if(dir == 2)
					{
						--y;
						up[P(x, y)] = 1;
					}
					else if(dir == 3)
					{
						right[Q(x, y)] = 1;
						++x;
					}
				}
			}
		}
	}
	
	assert(x == 0);
	assert(y == 0);
	
	for(int y = 0; y < TOT; ++y)
	{
		bool in = false;
		int start = INF;
		for(int x = 0; x < TOT; ++x)
		{
			if(up[P_(x, y)])
			{
				if(in)
					start = x;
				else
				{
					if(start != INF)
					{
						for(int x1 = start; x1 < x; ++x1)
							draw[P_(x1, y)] = 1;
					}
				}
				in = !in;
				
//				cerr << x - HALF << ' ' << y - HALF << ' ' << in << endl;
			}
		}
	}
	
	for(int x = 0; x < TOT; ++x)
	{
		bool in = false;
		int start = INF;
		for(int y = 0; y < TOT; ++y)
		{
			if(right[Q_(x, y)])
			{
				if(in)
					start = y;
				else
				{
					if(start != INF)
					{
						for(int y1 = start; y1 < y; ++y1)
							drawq[Q_(x, y1)] = 1; // cache prob
//						cerr << "DRAW " << x - HALF << ": " << start - HALF << ' ' << y - HALF << endl;
					}
				}
				in = !in;

//				cerr << "R " << x - HALF << ' ' << y - HALF << ' ' << in << endl;
			}
		}
	}
	
	for(int x = 0; x < TOT; x += CL)
	{
		for(int y = 0; y < TOT; y += CL)
		{
			for(int x1 = 0; x1 < CL; ++x1)
			{
				for(int y1 = 0; y1 < CL; ++y1)
				{
					if(drawq[Q_(x + x1, y + y1)])
						draw[P_(x + x1, y + y1)] = 1;
				}
			}
		}
	}
	
	int res = 0;
	
	for(int y = 0; y < TOT; ++y)
	{
		for(int x = 0; x < TOT; ++x)
		{
			if(draw[P_(x,y)])
			{
//				cerr << x - HALF << ' ' << y - HALF << endl;
				++res;
			}
		}
	}

	out << "Case #" << (casen + 1) << ": " << res << endl;
}

int main(int argc, char** argv)
{
	if(argv[1])
	{
		in.open(argv[1]);
		if(argv[2])
		{
			out.open(argv[2]);
		}
		else
		{
			out.open("/dev/stdout");
		}
	}
	else
	{
		in.open("/dev/stdin");
		out.open("/dev/stdout");
	}

	init();

	int cases;
	in >> cases;
	
	for(int i = 0; i < cases; ++i)
		solve_case(i);
	
	return 0;
}

