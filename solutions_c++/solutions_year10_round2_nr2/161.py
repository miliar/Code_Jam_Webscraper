#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int MaxN = 110;

int x[MaxN], v[MaxN];
int N, K, L, T;

int solve()
{
	int cnt = 0, notreach = 0;
	for(int i=N-1; i>=0 && K; i--)
	{
		if((L-x[i]+v[i]-1)/v[i] > T)	notreach ++;
		else	cnt += notreach, K --;	
	}
	if(K)	return -1;
	return cnt;	
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.out", "w", stdout);
	
	int cases;	cin >> cases;
	for(int cas=1; cas<=cases; cas++)
	{
		cin >> N >> K >> L >> T;
		for(int i=0; i<N; i++)	cin >> x[i];
		for(int i=0; i<N; i++)	cin >> v[i];
		int ans = solve();
		printf("Case #%d: ", cas);
		if(ans != -1)	cout << ans << endl;
		else	puts("IMPOSSIBLE");	
	}
	
	
	return 0;	
}
