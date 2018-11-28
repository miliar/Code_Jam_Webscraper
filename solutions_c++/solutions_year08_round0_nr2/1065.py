#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <fstream>
using namespace std;
template<class T> inline const T& max(const T& a, const T& b){return a > b ? a : b;}
template<class T> inline const T& min(const T& a, const T& b){return a < b ? a : b;}
template<class T> inline T sqr(const T a) {return a * a;}
const double PI = acos(-1);
ofstream fout("out.txt");

struct Car
{
	int station;
	int times;
};
Car cars[210];
int numOfCars;
struct Table
{
	int start;
	int end;
	int station;
};
//Table timess[210];
int T;
int numOfTables;
int ans[2];

int cmp(const Table A, const Table B)
{
	if (A.start != B.start) return A.start - B.start;
	else if (A.end != B.end) return A.end - B.end;
	else return A.station - B.station;
}

vector<Table> times;

void input()
{
	int nA, nB;
	times.clear();
	scanf("%d", &T);
	scanf("%d%d", &nA, &nB);
	memset(ans, 0, sizeof ans);
	int i, j;
	int h, m;
	Table tim;
	char tmp;
	for (i=0; i<nA; ++i) 
	{
		scanf("%d%c%d", &h, &tmp, &m);
		tim.start = h * 60 + m;
		scanf("%d%c%d", &h, &tmp, &m);
		tim.end = h * 60 + m;
		tim.station = 0;
		times.push_back(tim);
	}
	for (j=0; j<nB; ++j)
	{
		scanf("%d%c%d", &h, &tmp, &m);
		tim.start = h * 60 + m;
		scanf("%d%c%d", &h, &tmp, &m);
		tim.end = h * 60 + m;
		tim.station = 1;
		times.push_back(tim);
	}
	numOfTables = times.size();
	for (i=0; i<numOfTables-1; ++i)
	{
		for (j=numOfTables-1; j>i; --j)
			if (cmp(times[j], times[j-1]) < 0)
				swap(times[j], times[j-1]);
	}
	numOfCars = 0;
}

void calculate()
{
	int s, c;
	for (s=0; s<numOfTables; ++s) {
		for (c=0; c<numOfCars; ++c) {
			if (times[s].start >= cars[c].times && times[s].station == cars[c].station) {
				cars[c].times = times[s].end + T;
				cars[c].station = 1 - times[s].station;
				break;
			}
		}
		if (c == numOfCars)
		{
			cars[numOfCars].station = 1 - times[s].station;
			cars[numOfCars].times = times[s].end + T;
			++numOfCars;
			++ans[times[s].station];
		}
	}
}

int main()
{
	int test;
	scanf("%d", &test);
	int t;
	for (t=1; t<=test; ++t) 
	{
		input();
		calculate();
		fout << "Case #" << t << ": " << ans[0] << " " << ans[1] << endl;
	}

	return 0;
}