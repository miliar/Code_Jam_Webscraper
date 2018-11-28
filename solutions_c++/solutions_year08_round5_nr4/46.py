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

/*
pair<int, int> extended_gcd(int a, int b)
{
	int x = 0;
	int lastx = 1;
	int y = 1;
	int lasty = 0;
	while(b != 0)
	{
		int temp = b;
		int quotient = a / b;
		int b = a / b;
		int a = temp
        
		temp = x;
		x = lastx-quotient*x;
		lastx = temp;
        
		temp = y;
		y = lasty - quotient*y;
		lasty = temp;
	}
	return make_pair(lastx, lasty);
}

int minv(int a, int p)
{
	return extended_gcd(a, p).first;
}

int minvs[10010];

int binom(int a, int b)
{
	return fact / 
}

int ways(int x, int y)
{
	int s = x + y;
	if(s % 3)
		return 0;
	
	s /= 3;
	int d = x - y;
	int h = (s + d) / 2;
	int v = (s - d) / 2;
	if(h < 0 || v < 0)
		return 0;
	
	return binom(h, h + v);
}
*/

int mat[128][128];
int rocks[128][128];

void solve_case(int casen)
{
	int H, W, R;
	in >> H;
	in >> W;
	in >> R;

	memset(mat, 0, sizeof(mat));
	memset(rocks, 0, sizeof(rocks));

	for(int i = 0; i < R; ++i)
	{
		int y;
		int x;
		in >> y >> x;
		--y;
		--x;
		rocks[y][x] = 1;
	}
	
	for(int y = 0; y < H; ++y)
	{
		for(int x = 0; x < W; ++x)
		{
			if(rocks[y][x])
				continue;

			int ry = y - 2;
			int rx = x - 1;
			int uy = y - 1;
			int ux = x - 2;
			int v = (y == 0) && (x == 0);

			if(ry >= 0 && rx >= 0)
				v += mat[ry][rx];
			if(uy >= 0 && ux >= 0)
				v += mat[uy][ux];
			mat[y][x] = v % 10007;
//			cerr << y << ' ' << x << ' ' << v << endl;
		}
	}
	
	out << "Case #" << (casen + 1) << ": " << mat[H - 1][W - 1] << endl;
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

