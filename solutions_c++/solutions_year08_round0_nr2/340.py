#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
using namespace std; 

#define DEBUG(x) fout << '>' << #x << ':' << x << endl;
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define FOR2(i, a, b) for (int i = (a); i > (b); --i)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }
const int INF = 1 << 29;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
#ifdef WIN32
typedef __int64 ll;
#else
typedef long long ll;
#endif

/////////////////////////////////////////////////////////////////////////////////////////////////////////////// 

ofstream fout("output.out");
ifstream fin("input.in");

struct rec
{
	int city;
	int time;
	bool add;

	bool operator<(const rec & r) const { return time < r.time || (time == r.time && add && !r.add); }
} events[600];

char input[150];
int main()
{
	int T;
	fin >> T;

	FOR(step, 0, T)
	{
		int time, na, nb;
		fin >> time >> na >> nb;

		int N = 0;
		fin.get();
		FOR(i, 0, na)
		{
			fin.getline(input, 150);
			int h1, m1, h2, m2;
			sscanf(input, "%d:%d %d:%d", &h1, &m1, &h2, &m2);
			
			events[N].city = 0;
			events[N].time = h1*60+m1;
			events[N].add = false;
			++N;

			events[N].city = 1;
			events[N].time = h2*60+m2+time;
			events[N].add = true;
			++N;
		}

		FOR(i, 0, nb)
		{
			fin.getline(input, 150);
			int h1, m1, h2, m2;
			sscanf(input, "%d:%d %d:%d", &h1, &m1, &h2, &m2);
			
			events[N].city = 1;
			events[N].time = h1*60+m1;
			events[N].add = false;
			++N;

			events[N].city = 0;
			events[N].time = h2*60+m2+time;
			events[N].add = true;
			++N;
		}

		sort(events, events+N);
		int resA = 0, resB = 0;
		int inA = 0, inB = 0;
		FOR(i, 0, N)
		{
			if (events[i].city == 0)
			{
				if (events[i].add) ++inA;
				else
				{
					if (!inA) ++resA;
					else --inA;
				}
			}
			else
			{
				if (events[i].add) ++inB;
				else
				{
					if (!inB) ++resB;
					else --inB;
				}
			}
		}

		fout << "Case #" << step+1 << ": " << resA << " " << resB << endl;
	}

	return 0;
}
