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
	string outStr  = "NO";;
	if (ans != -1) {
		cout << "Case #" << caseNumber << ": " << ans << endl;
	} else {
		cout << "Case #" << caseNumber << ": " << outStr << endl;
	}

}

template <class AnswerType>
AnswerType SolveTestCase() {
	int n;
	cin >> n;
	int minVal = 1<<28;
	int xorSum = 0;
	int sum = 0;
	for (int i = 0; i < n; i++) {
		int val;
		cin >> val;
		minVal = min(val, minVal);
		sum += val;
		xorSum = xorSum ^ val;
	}
	if (xorSum == 0)
		return sum - minVal;
	return -1;
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
		PrintAnswerToTestCase(caseNumber, SolveTestCase<int>() );

	return 0;
}