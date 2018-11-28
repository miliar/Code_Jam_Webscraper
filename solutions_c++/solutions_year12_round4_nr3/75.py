#include<iostream>
#include<cstdio>

using namespace std;

#define MAXN 2010
const int inf = 1000000000;

int N;
int x[MAXN];
int H[MAXN];

void get_height(int l, int r, int k){
	if (x[l] < r){
		get_height(x[l], r, k);
		get_height(l, x[l], k);
	}
	else {
		H[l] = H[r] - k * (r - l);
		if (l + 1 < r) get_height(l + 1, r, k + 1);
	}
}

void solve(int casen)
{
	scanf( "%d", &N );
	for (int i = 1; i < N; i++ )
		scanf( "%d", &x[i] );
	bool imposs = false;
	for (int i = 1; i <= N; i++ )
		for (int j = i + 1; j < x[i]; j++ )
			if (x[j] > x[i]) imposs = true;
	if ( imposs ) printf( "Case #%d: Impossible\n", casen );
	else {
		H[N] = inf;
		get_height(1, N, 1);
		printf( "Case #%d: ", casen );
		for (int i = 1; i <= N; i++ ) printf( "%d%c", H[i], (i == N ? '\n' : ' ') );
	}
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

 