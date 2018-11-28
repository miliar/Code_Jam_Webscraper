#define _USE_MATH_DEFINES  
#define _CRT_SECURE_NO_DEPRECATE  
  
#include <algorithm>  
#include <bitset>  
#include <cassert>  
#include <cmath>  
#include <cstdio>  
#include <cstdlib>  
#include <cstring>   
#include <deque>  
#include <functional>  
#include <iomanip>  
#include <iostream>  
#include <list>  
#include <map>  
#include <numeric>  
#include <queue>  
#include <set>  
#include <sstream>  
#include <stack>  
#include <string>  
#include <utility>  
#include <vector>  
  
using namespace std;  
  
#pragma comment(linker, "/STACK:64000000")  
  
#define problem "Khaustov"  

typedef long long int64;  
typedef unsigned long long ull;
typedef unsigned char byte;  
typedef pair<int, int> pii;
typedef pair<char, int> pci;
typedef pair<int, pii> piii;
typedef pair<int, piii> piiii;
typedef pair<pii, pii> edge;
typedef pair<int64, int64> pii64;
typedef pair<int64, pii64> shit;
typedef pair<pii64, int> piii64;
typedef pair<double, int> pdi;
typedef pair<pdi, int> pdii;
typedef pair<int, string> pis;
typedef vector<int> vi;  
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<pii> vpii;  
typedef vector<vpii> vvpii;  
typedef vector<string> vs;  
typedef vector<vs> vvs;  
typedef list<int> li;   
  
#define y1 _dsfdsfkn
#define left _dsfdsf
#define right _dfjdsj
#define link _tsu_sux
#define prime 1103
#define eps 1e-6
#define inf 123456789
#define toMod 1000000007LL

inline piii make(int x, int y, int z)
{
	return piii(x, pii(y, z));
}

int nt, n;
char c;
int x;
int lastA, lastB;
priority_queue < pii, vector<pii>, greater<pii> > QA, QB;

int main()
{  
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	cin >> nt;

	for (int tn = 1; tn <= nt; ++tn)
	{
		cin >> n;

		lastA = 0;
		lastB = 0;
		for (int i = 0; i < n; ++i)
		{
			cin >> c >> x;
			--x;
			if (c == 'O')
			{
				int from = min(lastA, x);
				int to = max(lastA, x);
				for (int j = from; j < to; ++j)
					QA.push(pii(i, 0));
				QA.push(pii(i, 1));
				lastA = x;
			} else {
				int from = min(lastB, x);
				int to = max(lastB, x);
				for (int j = from; j < to; ++j)
					QB.push(pii(i, 0));
				QB.push(pii(i, 1));
				lastB = x;
			}
		}

		int res = 0;

		for (int t = 0; ; ++t)
		{
			if (QA.empty() && QB.empty())
			{
				res = t;
				break;
			}
			if (QA.empty())
			{
				QB.pop();
				continue;
			}
			if (QB.empty())
			{
				QA.pop();
				continue;
			}
			if (QA.top().second && QB.top().second)
			{
				if (QA.top().first < QB.top().first)
					QA.pop();
				else
					QB.pop();
				continue;
			}
			if (QA.top().second)
			{
				if (QA.top().first < QB.top().first)
					QA.pop();
				QB.pop();
				continue;
			}
			if (QB.top().second)
			{
				if (QB.top().first < QA.top().first)
					QB.pop();
				QA.pop();
				continue;
			}
			QA.pop();
			QB.pop();
		}

		printf("Case #%d: %d\n", tn, res);
	}

    return 0;  
}