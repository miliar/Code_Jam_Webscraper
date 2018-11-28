#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
#include <string>
using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
typedef unsigned int uint;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

#ifndef NOMINMAX
  #ifndef max
    #define max(a,b) (((a) > (b)) ? (a) : (b))
  #endif
  #ifndef min
    #define min(a,b) (((a) < (b)) ? (a) : (b))
  #endif
#endif 

#define read(a) { scanf("%d", &(a)); }
#define swap(a, b) { (a) ^= (b); (b) ^= (a); (a) ^= (b); }

#define MAX 5001
#define MAXL 16

int N, L, D;
string words[MAX];
int cnum = 0;
string c[MAXL];

void getstring(string s)
{
	int i = 0;
	int j = 0;
	For(ii, 0, MAXL-1)
		c[ii] = "";

	while(i < s.size())
	{
		while (i < s.size() &&  s[i] != '(')
			c[j++] = s[i++];

		i++;

	/*	if(s[i] == '(')
			continue;*/

		while (i < s.size() &&  s[i] != ')')
			c[j] += s[i++];
		i++;
		j++;
	}
	cnum = j;
}

void do_case(int cases, string s)
{
	int count = 0;
	getstring(s);

	For(i, 0, D-1)
	{
		bool good = true;
		For(j, 0, L-1)
		{
			bool good2 = false;
			For(k, 0, c[j].size()-1)
				if (c[j][k] == words[i][j])
				{
					good2 = true;
					continue;
				}
			if (!good2)
			{
				good = false;
				break;
			}
		}
		if (good)
			count++;
	}

	printf("Case #%d: %d\n", cases+1, count);
}

int main()
{
	read(L); read(D); read(N);
	cin.ignore();
	Rep(i, D)
		getline(cin, words[i]);

	Rep(i, N)
	{
		string line;
		getline(cin, line);
		do_case(i, line);
	}

	return 0;
}