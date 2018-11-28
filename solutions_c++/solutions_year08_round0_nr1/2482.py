#include <cstdio>
#include <string>
#include <map>
#include <algorithm>
#include <iostream>

using namespace std;

#define FOR(i, lo, hi) for(int i = (lo); i < (hi); ++i)

#define MAX_LINE_LEN 128

#define INF 1000000

string readLine()
{
	char s[MAX_LINE_LEN + 1];
	memset(s, 0, sizeof(s));
	
	FOR(pos, 0, MAX_LINE_LEN)
	{
		char ch = getchar();
		if(ch == '\n' || ch == EOF) break;
		s[pos] = ch;
	}

	return string(s);
}

int S, Q;
int a[1024];		// a[i] is the id of the search engine corresponding to the i-th query
int memo[128][1024];

int rec(int sid, int qid)
{
	int &ret = memo[sid][qid];
	if(ret != -1) return ret;

	if(qid == Q - 1) return ret = 0;
	
	if(sid != a[qid + 1]) return ret = rec(sid, qid + 1);

	int ans = INF;
	FOR(i, 1, S + 1)
	{
		if(i == sid) continue;
		ans = min(ans, rec(i, qid + 1));
	}

	return ret = ans + 1;
}

int main()
{
	int N;
	scanf("%d", &N);
	FOR(tc, 1, N + 1)
	{
		map<string, int> id;
		scanf("%d", &S);
		readLine();	// read to the end of the line containing S
		FOR(i, 0, S)
		{
			string s = readLine();
			id[s] = i + 1;
		}

		scanf("%d", &Q);
		readLine();	// read to the end of the line containing Q
		FOR(i, 0, Q)
		{
			string q = readLine();
			a[i] = id[q];
		}

		if(Q == 0)
		{
			printf("Case #%d: %d\n", tc, 0);
			continue;
		}

		memset(memo, -1, sizeof(memo));

		int ans = INF;
		FOR(i, 1, S + 1)
		{
			if(a[0] == i) continue;
			ans = min(ans, rec(i, 0));
		}

		printf("Case #%d: %d\n", tc, ans);
	}

	return 0;
}
