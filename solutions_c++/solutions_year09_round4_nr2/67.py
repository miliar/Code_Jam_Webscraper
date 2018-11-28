#include <iostream>
#include <fstream>
#include <vector>
#include <assert.h>
#include <memory.h>
using namespace std;

ifstream in;
ofstream out;

unsigned long long cave[64];

#define INF 65536
int R, C, F;

static inline int go__(int h, int c, int l, bool lwall, int r, bool rwall);

int mem[1 << 26];

static inline int go_(int h, int c, int l, bool lwall, int r, bool rwall)
{
	unsigned k = ((r - c) << 20) | ((c - l) << 14) | (c << 8) | (h << 2) | (lwall ? 2 : 0) | (rwall ? 1 : 0);
	int& v = mem[k];
	if(!v)
	{
		v = go__(h, c, l, lwall, r, rwall) + 1;
		//cout << h << ' ' << c << ' ' << l << ' ' << lwall << ' ' << r << ' ' << rwall << ": " << (v - 1) << endl;
	}
	return v - 1;
}

static inline int go(int h, int c, int digl, int digr)
{
	if(h >= (R - 1))
		return 0;

	unsigned long long row = cave[h];
	unsigned long long next = cave[h + 1];
	int l, r;
	bool lwall;
	bool rwall;
	for(r = c;; ++r)
	{
		if(r >= digr && (row & (1ULL << r)))
		{
			rwall = true;
			break;
		}

		if(!(next & (1ULL << r)))
		{
			rwall = false;
			break;
		}
	}

	for(l = c;; --l)
	{
		if(l <= digl && (row & (1ULL << l)))
		{
			lwall = true;
			break;
		}

		if(!(next & (1ULL << l)))
		{
			lwall = false;
			break;
		}
	}

	return go_(h, c, l, lwall, r, rwall);
}

static inline int fall_(int r, int c, int ldig, int rdig)
{
	int i;
	for(i = r + 2; i < R; ++i)
	{
		if(cave[i] & (1ULL << c))
			break;
	}

	int f = i - r - 1;
	if(f > F)
		return INF;

	if(i == R)
		return 0;

	if(i == (r + 2))
		return go(i - 1, c, ldig, rdig);
	else
		return go(i - 1, c, c - 1, c + 1);
}

static inline int fall(int r, int c)
{
	return fall_(r, c, c - 1, c + 1);
}

static inline int go__(int h, int c, int l, bool lwall, int r, bool rwall)
{
	int v = INF;

	if(!lwall)
		v = min(v, fall(h, l));
	if(!rwall)
		v = min(v, fall(h, r));

	if((r - l) <= 2)
		return v;

	v = min(v, fall(h, l + 1) + 1);
	v = min(v, fall(h, r - 1) + 1);

	for(int i = l + 2; i <= r - 2; ++i)
	{
		v = min(v, fall(h, i) + 1);

		for(int j = i + 2; j <= r; ++j)
		{
			v = min(v, fall_(h, i, i - 1, j) + j - i);
		}

		for(int j = i - 2; j >= l; --j)
		{
			v = min(v, fall_(h, i, j, i + 1) + i - j);
		}
	}

	return v;
}

int main(int argc, char** argv)
{
	in.open(argv[1]);
	out.open(argv[2]);

	int T;
	in >> T;
	for(int it = 1; it <= T; ++it)
	{
		cout << "Case #" << it << endl;
		memset(mem, 0, sizeof(mem));
		in >> R >> C >> F;
		char cell;
		for(int r = 0; r < R; ++r)
		{
			cave[r] = 0;
			cave[r] |= 1;
			cave[r] |= (1ULL << (C + 1));
			for(int c = 0; c < C; ++c)
			{
				in >> skipws >> cell;
				if(cell == '#')
					cave[r] |= 1ULL << (c + 1);
			}
		}

		int r = go(0, 1, 0, 2);
		if(r >= INF)
			out << "Case #" << it << ": No" << endl;
		else
			out << "Case #" << it << ": Yes " << r << endl;
	}

	return 0;
}
