#if 1
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <stack>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <functional>
#include <algorithm>
#include <cmath>
#include <bitset>
#include <cstdio>
using namespace std;

typedef long long LL;
typedef long double LD;
const LD eps = 1e-9;

typedef pair<int, int> pii;
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) cerr << #x << " = " << x << endl;



int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t; scanf("%d", &t);
	for(int z = 0; z < t; ++z)
	{
		int r, k, n;
		scanf("%d%d%d", &r, &k, &n);
		vector<int> g(n);
		for(int i = 0; i < n; ++i)
			scanf("%d", &g[i]);

		vector<int> ex(n, -1);
		vector<int> next(n, -1);
		vector<LL> get(n);
		int pos = 0;
		int cyc = -1;
		int start;
		LL cost = 0;
		for(int i = 0; i < r; ++i)
		{			
			ex[pos] = i;
			LL sum = 0;
			int npos = pos;
			while(sum <= k)
			{
				sum += g[npos];
				npos = (npos + 1) % n;
				if(pos == npos)
					break;
			}
			if(sum > k)
			{
				npos = (npos + n - 1) % n;
				sum -= g[npos];
			}
			next[pos] = npos;
			get[pos] = sum;
			if(ex[npos] != -1)
			{
				start = npos;
				cyc = (i + 1) - ex[npos];
				break;
			}
			
			pos = npos;
			cost += sum;
		}

		
		if(cyc != -1)
		{
			cost = 0;
			LL cycCost = 0;
			int cur = 0;
			while(cur != start)
			{
				cost += get[cur];
				cur = next[cur];
			}
			do
			{
				cycCost += get[cur];
				cur = next[cur];
			} while(cur != start);
			r -= ex[start];
			cost += cycCost * (r / cyc);
			int rem = r % cyc;
			cur = start;
			while(rem)
			{
				cost += get[cur];
				cur = next[cur];
				rem--;
			}
		}

		printf("Case #%d: ", z + 1);
		cout << cost << endl;
		
	}
	return 0;
}
#endif