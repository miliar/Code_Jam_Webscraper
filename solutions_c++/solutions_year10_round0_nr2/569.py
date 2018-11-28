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
	cout << "Case #" << caseNumber << ": " << ans << endl;
}

int GCD(int a, int b) {
	if (b == 0)
		return a;
	return GCD(b, a % b);
}

template <class AnswerType>
AnswerType SolveTestCase(vector<int> times) {
	sort(times.rbegin(), times.rend());
	int maxDivisor = times[0] - times.back();
	for (size_t i = 1; i < times.size() - 1; i++)
		maxDivisor = GCD(maxDivisor, times[i] - times[i + 1]);
	if (times[0] % maxDivisor == 0)
		return 0;
	return  maxDivisor - times[0] % maxDivisor;

}

int main()
{
	//freopen("input.txt", "r", stdin);
	freopen("small.in", "r", stdin);
	//freopen("large.in", "r", stdin);

	freopen("output.txt", "w", stdout);

	int numCases;
	cin >> numCases;

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++) {
		int n;
		cin >> n;
		vector<int> times(n);
		for (size_t i = 0; i < times.size(); i++)
			cin >> times[i];
		PrintAnswerToTestCase(caseNumber, SolveTestCase<int>(times) );
	}

	return 0;
}