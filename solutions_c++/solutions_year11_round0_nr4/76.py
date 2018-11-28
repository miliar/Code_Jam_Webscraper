#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define sz(a) int((a).size())
#define all(X) (X).begin(), (X).end()
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;

double dp[1024];

double wrong[1024];

void initial()
{
	dp[0] = 0;
	dp[1] = 0;
	for (int i = 2; i <= 1000; ++i) {
		double arr[1024];
		arr[0] = 1;
		int flag = -1;
		double down = 1;
		double how = 1;
		for (int j = 1; j <= i; ++j) {
			how /= down;
			arr[j] = arr[j - 1] + flag * how;
			down += 1;
			flag = -flag;
		}
		double fact = 1;
		double sum = 0;
		for (int j = 1; j <= i; ++j) {
			sum += dp[i - j] * arr[i - j] * fact;
			fact /= (j + 1);
		}
		double div = 1 - arr[i];
		dp[i] = (sum + 1) / div;
	}
}

double run()
{
	int n;
	scanf("%d", &n);
	int sum = 0;
	for (int i = 1; i <= n; ++i) {
		int num;
		scanf("%d", &num);
		if (num != i) {
			++sum;
		}
	}
	return dp[sum];
}

int main()
{
	freopen("D0.in", "r", stdin);
	freopen("D0.out", "w", stdout);
	initial();
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: %.10f\n", i, run());
	}
	return 0;
}