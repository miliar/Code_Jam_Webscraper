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
#include <list>
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

struct Train
{
	int time, end;
	int st;
	bool operator < (const Train & T) const
	{
		return time < T.time;
	}
};

Train A[300];

char buf[100];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T, t;
	scanf("%d", &T);
	for (t = 0; t < T; ++t)
	{
		int tt;
		scanf("%d", &tt);
		priority_queue<int, VInt, greater<int> > Q[2];
		int N[2];
		scanf("%d%d", &N[0], &N[1]);
		int i, j;
		int K = 0;
		for (i = 0; i < 2; ++i)
			for (j = 0; j < N[i]; ++j)
			{
				scanf("%s", buf);
				A[K].time = ((buf[0]-'0')*(int)10 + buf[1]-'0')*60 + (buf[3]-'0')*(int)10 + buf[4]-'0';
				scanf("%s", buf);
				A[K].end = ((buf[0]-'0')*(int)10 + buf[1]-'0')*60 + (buf[3]-'0')*(int)10 + buf[4]-'0';
				A[K].st = i;
				++K;
			}
		sort(A, A+K);
		int R[2] = {0};
		for (i = 0; i < K; ++i)
		{
			if (Q[A[i].st].empty() || Q[A[i].st].top() > A[i].time)
			{
				++R[A[i].st];
			}
			else
			{
				Q[A[i].st].pop();
			}
			Q[1-A[i].st].push(A[i].end + tt);
		}
		printf("Case #%d: %d %d\n", t+1, R[0], R[1]);
	}

	return 0;
}