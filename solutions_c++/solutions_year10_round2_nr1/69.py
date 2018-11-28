#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <cctype>
#include <memory>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

typedef long long Int;
typedef long double Double;
typedef vector<int> VInt;
typedef vector< vector<int> > VVInt;
typedef pair<int,int> PII;

#define FOR(i,n,m) for(i=(n); i<(m); ++i)
#define RFOR(i,n,m) for(i=(n)-1; i>=(m); --i)
#define CLEAR(x,y) memset((x), (y), sizeof(x))
#define COPY(x,y) memcpy((x),(y),sizeof(x))
#define PB push_back
#define MP make_pair
#define SIZE(v) ((int)((v).size()))
#define ALL(v) (v).begin(), (v).end()

char buf[1000];

vector<string> split(string s)
{
	vector<string> res;
	int i, p = 0;
	for (i = 1; i < s.size(); ++i)
	{
		if (s[i] == '/')
		{
			buf[p] = 0;
			res.PB(buf);
			p = 0;
		}
		else
			buf[p++] = s[i];
	}
	buf[p] = 0;
	res.PB(buf);
	return res;
}

int main()
{
//	freopen("A-small.in", "r", stdin);
//	freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T, t;
	scanf("%d", &T);
	for (t = 0; t < T; ++t)
	{
		vector<vector<string> > v;
		int N, M;
		scanf("%d%d", &N, &M);
		int i;
		for (i = 0; i < N; ++i)
		{
			scanf("%s", buf);
			v.PB(split(buf));
		}
		int res = 0;
		for (i = 0; i < M; ++i)
		{
			scanf("%s", buf);
			vector<string> s = split(buf);
			int j;
			int p = 0;
			for (j = 0; j < v.size(); ++j)
			{
				int k = 0;
				for (k = 0; k < s.size() && k < v[j].size(); ++k)
					if (s[k] != v[j][k])
						break;
				p = max(p, k);
			}
			res += s.size() - p;
			v.PB(s);
		}
		printf("Case #%d: %d\n", t+1, res);
	}
	return 0;
}