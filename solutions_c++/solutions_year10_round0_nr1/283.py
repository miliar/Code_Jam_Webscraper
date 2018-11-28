#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define all(a) a.begin(), a.end()
#define sz(a) a.size()

typedef pair<int, int> pii;
typedef long long lint;
typedef vector<int> vi;
typedef vector<vi> vvi;

const int Size = 10000;
char buffer[Size];

const int inf = 0x0fffffff;
const int white = 0, gray = 1, black = 2;

const double eps = 10e-6;

lint dp[50];

int Solution(int nTest)
{
	int k, n;
	scanf("%d%d", &n, &k);
	if(k == 0)
	{
		printf("Case #%d: OFF\n", nTest);
		return 1;
	}
	n--;
	if(k % (dp[n]+1) == dp[n])
		printf("Case #%d: ON\n", nTest);
	else
		printf("Case #%d: OFF\n", nTest);
	
	

	return 1;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	dp[0] = 1;
	for(int i = 1; i <= 30; i++)
	{
		dp[i] = dp[i - 1] * 2 + 1;
	}
	

	int i = 0, n = 9999;

	scanf("%d", &n);

	while(i < n && Solution(i+1))
		i++;

	return 0;
}