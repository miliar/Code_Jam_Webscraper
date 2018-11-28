#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <utility>

using namespace std;

void Output(const char *str)
{
	static int x = 0;
	x++;
	printf("Case #%d: %s\n", x, str);
}

void Output(long long ans)
{
	static int x = 0;
	x++;
	printf("Case #%d: %I64d\n", x, ans);
}

void Output(int ans)
{
	static int x = 0;
	x++;
	printf("Case #%d: %d\n", x, ans);
}

void solve()
{
	int N;
	scanf("%d", &N);
	int A[1000];
	int B[1000];
	for(int i = 0; i < N; i++) {
		scanf("%d%d", A+i, B+i);
	}
	int ans = 0;
	for(int i = 0; i < N; i++) {
		for(int j = i+1; j < N; j++) {
			if( (A[i] > A[j] && B[i] < B[j])
			 || (A[i] < A[j] && B[i] > B[j]) ) {
				ans++;
			}
		}
	}
	Output(ans);
}

void GCJ2010_R1C_A()
{
	int T;
	scanf("%d", &T);
	while(T--) {
		solve();
	}
}

int main()
{
	GCJ2010_R1C_A();
	return 0;
}

