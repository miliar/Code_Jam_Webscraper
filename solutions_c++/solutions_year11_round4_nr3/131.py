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

vector<int> isPrime(1000100, true);

void FillIsPrime() {

	for (int i = 2; i * i < isPrime.size(); i++)
		if (isPrime[i]) {
			for (int j = i * i; j < isPrime.size(); j += i)
				isPrime[j] = false;
		}
}

template <class AnswerType>
AnswerType SolveTestCase() {
	long long n;
	cin >> n;
	long long ans = 1;

	if (n == 1)
		return 0;

	for (long long i = 2; i * i <= n; i++) 
		if (isPrime[i]) {
			long long t = i * i;
			for (; t <= n; t *= i) ans++;
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

	FillIsPrime();

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++)
		PrintAnswerToTestCase(caseNumber, SolveTestCase<long long>() );

	return 0;
}