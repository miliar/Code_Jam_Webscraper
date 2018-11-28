#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <fstream>
#include <algorithm>
#include <functional>
#include <queue>
#include <map>
#include <climits>
#include <cstring>
#include <list>
#include <ctime>
#include <sstream>
#include <set>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
typedef pair<int, LL> PIL;
typedef pair<PII, PII> SEG;

#define lowbit(a) ((a) & (-a))
#define two(a) (1 << (a))
#define contain(a, b) (((a) & two(b)) != 0)
#define left(a) (((a) <<1) + 1)
#define right(a) (left(a) + 1)

int D, I, M, N;
vector<int> p;

void getData()
{
	cin >> D >> I >> M >> N;
	p.clear();
	for(int i = 0; i < N; i++)
	{
		int a;
		cin >> a;
		p.push_back(a);
	}
}

LL opt[128][256];

LL go(int a, int b)
{
	if(opt[a][b] != -1) return opt[a][b];
	if(a == 0) return opt[a][b] = min(D, abs(p[0] - b));
	LL &rt = opt[a][b];
	rt = INT_MAX;
	
	rt = min(rt, go(a - 1, b) + min(D, abs(p[a] - b)));
	if(!M) rt = min(rt, go(a - 1, b) + abs(p[a] - b));
	else
	{
		int x = min(D + I, abs(p[a] - b));
		for(int i = 0; i < 256; i++)
		{
			if(abs(b - i) > M) rt = min(rt, go(a - 1, i) + x + ((abs(b - i) + M - 1) / M - 1) * I);
			else rt = min(rt, go(a - 1, i) + x);
		}
	}
	return rt;
}

int solve()
{
	memset(opt, -1, sizeof(opt));
	LL rt = _I64_MAX;
	for(int i = 0; i < 256; i++)
		rt = min(go(N - 1, i), rt);
	return rt;
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);

	int t;
	cin >> t;
	for(int nc = 1; nc <= t; nc++)
	{
		getData();
		cout << "Case #" << nc << ": " << solve() << endl;
	}
	return 0;
}
