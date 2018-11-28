#include <cstdlib>
#include <iostream>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
using namespace std;

int T;

int solve()
{
	int N;
	int A[1000], B[1000];
	cin >> N;
	int ret = 0;
	for (int i = 0; i < N; ++i) {
		cin >> A[i] >> B[i];
		for (int j = 0; j < i; ++j) {
			if (A[j] > A[i] && B[j] < B[i]) ++ret;
			else if (A[j] < A[i] && B[j] > B[i]) ++ret;
		}
	}
	return ret;
}

int main(int argc, char *argv[])
{
	cin >> T;
	
	int ans;
	
	for (int i = 0; i < T; ++i) {
		ans = solve();
		printf("Case #%d: %d\n", i + 1, ans);
	}
	
    return EXIT_SUCCESS;
}
