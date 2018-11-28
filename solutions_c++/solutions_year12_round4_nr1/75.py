#include<iostream>
#include<cstdio>

using namespace std;

#define MAXN 10010

int len[MAXN];
int N, D;
int d[MAXN], I[MAXN];

void dfs(int i, int l)
{
	if (l <= len[i]) return;
	len[i] = l;
	for (int j = 0; j < N; j++ )
		if (abs(d[i] - d[j]) <= l)
			dfs(j, min(abs(d[i] - d[j]), I[j]));
}

void solve(int casen)
{
	scanf( "%d", &N );
	for (int i = 0; i < N; i++ )
		scanf( "%d %d", &d[i], &I[i] );
	scanf( "%d", &D );
	memset( len, 0xff, sizeof( len ) );
	dfs(0, d[0]);
	bool ok = false;
	for (int i = 0; i < N; i++ )
		if (d[i] + len[i] >= D) ok = true;
	if ( ok ) printf( "Case #%d: YES\n", casen );
	else printf( "Case #%d: NO\n", casen ); 
}

int main()
{
	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int test_cases;
	scanf( "%d", &test_cases );
	for (int i = 1; i <= test_cases; i++ )
		solve(i);
}

 