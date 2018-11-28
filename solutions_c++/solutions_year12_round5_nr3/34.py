#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>

using namespace std;

#define MAXN 1010
#define MAXM 2000010
const int inf = 1000000000;

struct Food{
	int P, S;
} Fd[MAXN];

int M, F, N;
int cost[MAXM];

bool operator<(const Food &A, const Food &B)
{
	if ( A.P != B.P ) return A.P < B.P;
	return A.S > B.S;
}

void solve(int casen)
{
	scanf( "%d %d %d", &M, &F, &N );
	for (int i = 0; i < N; i++ )
		scanf( "%d %d", &Fd[i].P, &Fd[i].S );
	sort(Fd, Fd + N);
	printf( "Case #%d: ", casen );
	for (int i = 0; i <= M; i++ ) cost[i] = inf;
	cost[0] = 0;
	int ans;
	for (int i = 0; i < M; i++ )
	if ( cost[i] <= M )
	{
		int k = i + 1, sel = 0, tcost = cost[i] + F, failed = 0;
		while (tcost <= M && sel < N){
			if (Fd[sel].S < k - i - 1) sel ++;
			else {
				tcost += Fd[sel].P;
				if ( cost[k] <= tcost ) failed ++;
				cost[k] = min(cost[k], tcost);
				k ++;
			}
			if ( failed > 200 ) break;
			if (tcost - cost[i] > cost[(k - i) / 2] + cost[(k - i + 1) / 2]) break;
		}
		ans = i;
	}
	cout << ans << endl;
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

 