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

int caker;
int cakec;
int startr;
int startc;

int cur_dist;
stack<int> stacks[2];
int curp;
#define cur (stacks[curp])
#define next (stacks[!curp])
int mark[64 * 1024 * 1024];
char maze[16][16];
char lportal[16][16];
char rportal[16][16];
char uportal[16][16];
char dportal[16][16];

static inline void cur_visit(int k)
{
	if(mark[k] > cur_dist)
	{
		mark[k] = cur_dist;
		cur.push(k);
	}
}

static inline void next_visit(int k)
{
	if(mark[k] > (cur_dist + 1))
	{
		mark[k] = cur_dist + 1;
		next.push(k);
	}
}


#define INV 15

#define MAKE(x, y, px, py, pd, qx, qy, qd) ((x) | ((y) << 4) | ((px) << 8) | ((py) << 12) | ((qx) << 16) | ((qy) << 20) | ((pd) << 24) | ((qd) << 25))

void solve_case(int casen)
{
	int R, C;
	in >> R;
	in >> C;
	memset(maze, 0, sizeof(maze));
	for(int r = 0; r < R; ++r)
	{
		for(int c = 0; c < C; ++c)
		{
			char sym;
			in >> sym;

			if(sym == '#')
			{
				maze[r][c] = 1;
			}
			else if(sym == 'X')
			{
				caker = r;
				cakec = c;
			}
			else if(sym == 'O')
			{
				startr = r;
				startc = c;
			}
			else if(sym != '.')
				abort();
		}
	}
	
	for(int y = 0; y < R; ++y)
	{
		for(int x = 0; x < C; ++x)
		{
			if(maze[y][x])
				continue;

			lportal[y][x] = 0;
			for(int x1 = x - 1; x1 >= 0; --x1)
			{
				if(maze[y][x1])
				{
					lportal[y][x] = x1 + 1;
					break;
				}
			}
			
			rportal[y][x] = C;
			for(int x1 = x + 1; x1 < C; ++x1)
			{
				if(maze[y][x1])
				{
					rportal[y][x] = x1;
					break;
				}
			}
			
			uportal[y][x] = 0;
			for(int y1 = y - 1; y1 >= 0; --y1)
			{
				if(maze[y1][x])
				{
					uportal[y][x] = y1 + 1;
					break;
				}
			}
			
			dportal[y][x] = R;
			for(int y1 = y + 1; y1 < R; ++y1)
			{
				if(maze[y1][x])
				{
					dportal[y][x] = y1;
					break;
				}
			}
		}
	}
	
	curp = 0;
	cur_dist = 0;
	int start = MAKE(startc, startr, lportal[startr][startc], startr, 0, rportal[startr][startc], startr, 0);
	memset(mark, 0x7f, sizeof(mark));
	while(!cur.empty())
		cur.pop();
	while(!next.empty())
		next.pop();
	cur.push(start);
	mark[start] = 0;
	
	while(!cur.empty())
	{
		while(!cur.empty())
		{
			int v = cur.top();
			cur.pop();
			
			if(mark[v] < cur_dist)
				continue;
			
			int x = v & 15;
			int y = (v >> 4) & 15;
			int px = (v >> 8) & 15;
			int py = (v >> 12) & 15;
			int qx = (v >> 16) & 15;
			int qy = (v >> 20) & 15;
			int pd = (v >> 24) & 1;
			int qd = (v >> 25) & 1;
			
			if(x == cakec && y == caker)
			{
				out << "Case #" << (casen + 1) << ": " << cur_dist << endl;
				return;
			}
			
			if(px == qx && py == qy && pd == qd) // invalid
				continue;
			
			//cerr << cur_dist << ' ' << x << ' ' << y << ' ' << px << ' ' << py << ' ' << pd << ' ' << qx << ' ' << qy << ' ' << qd << endl;
			
			// swap portals
			cur_visit(MAKE(x, y, qx, qy, qd, px, py, pd));
			
			// shoot portals
			cur_visit(MAKE(x, y, rportal[y][x], y, 0, qx, qy, qd));
//			cur_visit(MAKE(x, y, px, py, pd, rportal[y][x], y, 0));
			cur_visit(MAKE(x, y, lportal[y][x], y, 0, qx, qy, qd));
//			cur_visit(MAKE(x, y, px, py, pd, lportal[y][x], y, 0));
			cur_visit(MAKE(x, y, x, uportal[y][x], 1, qx, qy, qd));
//			cur_visit(MAKE(x, y, px, py, pd, x, uportal[y][x], 1));
			cur_visit(MAKE(x, y, x, dportal[y][x], 1, qx, qy, qd));
//			cur_visit(MAKE(x, y, px, py, pd, x, dportal[y][x], 1));
			
			if(x < (C - 1) && !maze[y][x + 1])
				next_visit(MAKE(x + 1, y, px, py, pd, qx, qy, qd));
			if(x > 0 && !maze[y][x - 1])
				next_visit(MAKE(x - 1, y, px, py, pd, qx, qy, qd));
			if(y < (R - 1) && !maze[y + 1][x])
				next_visit(MAKE(x, y + 1, px, py, pd, qx, qy, qd));
			if(y > 0 && !maze[y - 1][x])
				next_visit(MAKE(x, y - 1, px, py, pd, qx, qy, qd));
			
			if((py == y && px == x)
			|| (pd == 0 && py == y && px == (x + 1))
			|| (pd == 1 && py == (y + 1) && px == x))
			{
				if(qd == 1)
					next_visit(MAKE(qx, qy + ((qy == 0 || maze[qy - 1][qx]) ? 0 : -1), px, py, pd, qx, qy, qd));
				else
					next_visit(MAKE(qx + ((qx == 0 || maze[qy][qx - 1]) ? 0 : -1), qy, px, py, pd, qx, qy, qd));
			}
		}
		
		++cur_dist;
		curp = !curp;
	}
	
	out << "Case #" << (casen + 1) << ": " << "THE CAKE IS A LIE" << endl;
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

