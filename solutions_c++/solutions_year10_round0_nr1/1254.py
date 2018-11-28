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

template <class AnswerType>
AnswerType SolveTestCase(int n, int k) {
	int num = 1 << n;
	if (k < num - 1)
		return false;
	return (k - num + 1) %  num == 0;
}
int main()
{
	freopen("input.txt", "r", stdin);
	//freopen("small.in", "r", stdin);
	freopen("large.in", "r", stdin);

	freopen("output.txt", "w", stdout);

	size_t numCases;
	cin >> numCases;
	
	for (size_t caseNumber = 1; caseNumber <= numCases; caseNumber++) {
		int n, k;
		cin >> n >> k;
		PrintAnswerToTestCase(caseNumber, (SolveTestCase<bool>(n, k)) ? "ON" : "OFF" );
	}

	return 0;
}