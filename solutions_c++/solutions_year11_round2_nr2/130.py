#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

template<class AnswerType>
void PrintAnswerToTestCase(size_t caseNumber, AnswerType ans)
{
	cout.precision(18);
	cout << "Case #" << caseNumber << ": " << 0.5 * ans << endl;
}

template <class AnswerType>
AnswerType SolveTestCase() {
	int n;
	long long d;
	cin >> n >> d;
	vector<int> p(n, 0);
	vector<int> v(n, 0);
	
	for (int i = 0; i < n; i++) {
		cin >> p[i] >> v[i];
	}
	
	vector<long long > sum(n + 1, 0);
	sum[0] = v[0];
	for (int i = 1; i <= n; i++)
		sum[i] = sum[i - 1] + v[i - 1];

	long long ans = 0;
	for (int i = 0; i < n; i++) {
		for (int j = i; j < n; j++)
			ans = max(ans, (sum[j + 1] - sum[i] - 1) * d - (p[j] - p[i]));
	}
	return ans;
}

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("small.in", "r", stdin);
	freopen("large.in", "r", stdin);

	freopen("output.txt", "w", stdout);

	int numCases;
	cin >> numCases;

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++)
		PrintAnswerToTestCase(caseNumber, SolveTestCase<long long>() );

	return 0;
}