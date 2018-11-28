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

int nt, n, res;
int a[1 << 10];
int f[1 << 21];
int g[1 << 21];

int main()
{  
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	scanf("%d", &nt);

	int lim = (1 << 21);
	for (int tn = 1; tn <= nt; ++tn)
	{
		res = -1;

		int sum = 0, fsum = 0;
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
		{
			scanf("%d", &a[i]);
			sum ^= a[i];
			fsum += a[i];
		}

		memset(f, -1, sizeof f);
		f[0] = 0;
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < lim; ++j)
				g[j] = f[j];

			if (i + 1 < n)
			{
				for (int j = 0; j < lim; ++j)
				{
					if (f[j] == -1) continue;
					int nj = (j ^ a[i]);
					g[nj] = max(g[nj], f[j] + a[i]);
				}
			} else {
				int cur;
				for (int j = 0; j < lim; ++j)
				{
					if (f[j] == -1) continue;
					cur = f[j] + a[i];
					if (cur == fsum) continue;
					int nj = (j ^ a[i]);
					g[nj] = max(g[nj], cur);
				}
			}

			for (int j = 0; j < lim; ++j)
				f[j] = g[j];
		}

		for (int i = 0; i < lim; ++i)
		{
			if (f[i] == -1) continue;
			if ((sum ^ i) == i) res = max(res, f[i]);
		}

		if (res == -1)
			printf("Case #%d: NO\n", tn, res);
		else
			printf("Case #%d: %d\n", tn, res);
	}

    return 0;  
}