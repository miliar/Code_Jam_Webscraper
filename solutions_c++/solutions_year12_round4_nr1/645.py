#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#define MP make_pair
#define PB push_back

using namespace std;

const int MAXN = 10010;

int d[MAXN], l[MAXN], N, D;
int pre[MAXN];

bool solve(int id)
{
	if(pre[id] == -1)	return 0;
	
	if(2*d[id] - pre[id] >= D)	return 1;
	
	for(int i = id+1; i < N && 2*d[id] - pre[id] >= d[i]; ++ i)
	{
		if(pre[i] == -1 && l[i] >= d[i] - d[id])	pre[i] = d[id];	
		
		else if(pre[i] == -1)	pre[i] = d[i] - l[i];
	}	
	return 0;
}

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	
	
	int T;	cin >> T;
	
	for(int cas = 1; cas <= T; ++ cas)
	{
		cin >> N;
		for(int i = 0; i < N; ++ i)
		{
			scanf("%d %d", &d[i], &l[i]);
			pre[i] = -1;	
		}	
		cin >> D;
		pre[0] = 0;
		
		bool flag = 0;
		for(int i = 0; i < N && !flag; ++ i)
		{
			if(solve(i))	
			{
				flag = 1;
				break;	
			}
		}
		
		printf("Case #%d: %s\n", cas, flag ? "YES" : "NO");
	}
	
	
	return 0;	
}

