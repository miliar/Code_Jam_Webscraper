#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

const int MAX = 100;

struct Node
{
	int c, s, t;	
};
Node rest[MAX];
int N, M;

bool operator < (const Node &a, const Node &b)
{
	if(a.t != b.t)	return a.t < b.t;
	if(a.c != b.c)	return a.c < b.c;	
	return a.s < b.s;
}

int cal(int cnt, priority_queue <Node> pQ)
{
	vector <int> v;
	while(!pQ.empty())	
	{
		v.push_back(pQ.top().s);
		pQ.pop();	
	}
	sort(v.begin(), v.end());
	reverse(v.begin(), v.end());
	int ret = 0;
	for(int i=0; i<v.size() && i<cnt; i++)
	{
		ret += v[i];	
	}
	return ret;
}

int solve(int cnt, priority_queue <Node> pQ)
{
	int turn = 1, score = 0, idx = 0, sum = 0;
	while(!pQ.empty() && turn --)
	{
		sum ++;
		if(sum > cnt)
		{
			return score + cal(turn+1, pQ);	
		}
		Node p = pQ.top();
		pQ.pop();
		score += p.s;
		turn += p.t;
		while(idx < M && p.c --)
		{
			pQ.push(rest[idx ++]);	
		}
	}
	return score;	
}

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);

	
	
	int T;	cin >> T;
	for(int cas=1; cas<=T; cas++)
	{
		cin >> N;
		priority_queue <Node> pQ;
		for(int i=0; i<N; i++)
		{
			Node p;
			scanf("%d %d %d", &p.c, &p.s, &p.t);
			pQ.push(p);	
		}
		
		cin >> M;
		for(int i=0; i<M; i++)
		{
			Node p;
			scanf("%d %d %d", &p.c, &p.s, &p.t);
			rest[i] = p;	
		}
		
		int ans = 0;
		for(int i=0; i<=N+M; i++)
		{
			ans = max(ans, solve(i, pQ));	
		}
		printf("Case #%d: %d\n", cas, ans);
	}
	
	
	return 0;	
}
