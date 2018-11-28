#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <set>
#include <algorithm>
#include <queue>
#include <cassert>
#include <fstream>
#include <sstream>
#include <bitset>
#include <stack>
#include <list>
using namespace std;
#define debug1(x) cout << #x" = " << x << endl;
#define debug2(x, y) cout << #x" = " << x << " " << #y" = " << y << endl;
#define debug3(x, y, z) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << endl;
#define debug4(x, y, z, w) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << " " << #w" = " << w << endl;

template <class T>
ostream & operator << (ostream & out, const vector<T> & t)
{	out << t.size() << " {";	for (int i = 0; i < t.size(); ++i) 		out << t[i] << " ";	out << "}";	return out;}

template <class T>
ostream & operator << (ostream & out, const set<T> & t)
{	out << "{";	for (set<T>::iterator itr = t.begin(); itr != t.end(); ++itr)		out << *itr << " ";	out << "}";	return out;}

/////////////////////////
// template finished
/////////////////////////
int T, testid;
string line;

bool isSquare(long long x)
{
	if (x == 1) return true;
	long long sx = (sqrt(x * 1.0) + 1e-6);
	return sx * sx == x || (sx + 1) * (sx + 1) == x || (sx - 1) * (sx - 1) == x;
}

void init()
{
	cin >> line;
	int q = 0;
	for (int i = 0; i < line.length(); ++i)
		if (line[i] == '?') q++;

	int upper = (1 << q);
	for (int s = 0; s < upper; ++s)
	{
		long long now = 0;
		int nowoff = 0;
		for (int i = 0; i < line.length(); ++i)
		{
			now = now << 1;
			if (line[i] == '1') now = now + 1;
			if (line[i] == '?')
			{
				if ((s & (1 << nowoff)) > 0) now = now + 1;
				nowoff++;
			}
		}
		if (isSquare(now))
		{
			//debug1(now);
			nowoff = 0;
			for (int i = 0; i < line.length(); ++i)
			{
				if (line[i] == '1') printf("1");
				if (line[i] == '0') printf("0");
				if (line[i] == '?')
				{
					if ((s & (1 << nowoff)) > 0) printf("1");
					else printf("0");
					nowoff++;
				}
			}
			printf("\n");
			return;
		}
	}
}

void york()
{
}

int main()
{
	cin >> T;
	for (testid = 1; testid <= T; ++testid)
	{
		printf("Case #%d: ", testid);
		init();
		york();
	}
	return 0;
}