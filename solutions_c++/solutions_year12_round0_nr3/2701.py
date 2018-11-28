#define _USE_MATH_DEFINES 
#define _CRT_SECURE_NO_DEPRECATE
#include <cmath> 
#include <iostream> 
#include <algorithm> 
#include <cstdio> 
#include <ctime> 
#include <map> 
#include <string> 
#include <vector> 
#include <set> 
#include <stack> 
#include <queue> 
#include <deque> 
#include <iomanip>
#include <sstream>

using namespace std; 

#pragma comment(linker, "/STACK:64000000") 
typedef long long int64; 
typedef unsigned long long uint64; 
template<class T> inline T sqr(T a) {return a * a;} 
#define prime 1103 
#define INF 123456789
#define TASK "C-large"
#define MOD 1000000007


int mult(int n, int &l)
{
	int k = 1;
	l = 0;
	for(;;)
	{
		++l;
		if(k * 10 <= n)
		{
			k *= 10;
			continue;
		}
		return k;
	}
}

vector<vector<int> > table(2000001);
void calc(int n, int a, int b)
{
	if(n < 10) return;
	int l = 0;
	int k = mult(n, l);
	int m = n;
	set<int> was;
	for(int i = 0; i < l - 1; ++i)
	{
		int tmp = m;
		m = m / 10 + k * (m % 10);
		if(!(tmp % 10) || m > b ||
			m < a || m <= n || was.find(m) != was.end()) continue;
		was.insert(m);
		table[n].push_back(m);
	}
}


int main()
{
	freopen(TASK ".in", "r", stdin); 
	freopen(TASK ".out", "w", stdout); 
	for(int i = 1; i <= 2000000; ++i)
		calc(i, 1, 2000000);
	int t;
	scanf("%d", &t);
	for(int test = 0; test < t; ++test)
	{
		int a, b;
		scanf("%d%d", &a, &b);
		int res = 0;
		for(int i = a; i <= b; ++i)
		{
			for(int j = 0; j < (int)table[i].size(); ++j)
			{
				if(table[i][j] <= i || table[i][j] > b) continue;
				++res;
			}
		}
		printf("Case #%d: %d\n", test + 1, res);
	}

	return 0; 
}