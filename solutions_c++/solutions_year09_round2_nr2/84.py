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

string SolveTestCase()
{
	string number;
	cin >> number;
	int n = number.length();
	vector<int> perm(n);
	for (int i = 0; i < n; i++)
		perm[i] = number[i] - '0';

	if (!next_permutation(perm.begin(), perm.end() ) )
	{
		perm.push_back(0);
		sort(perm.begin(), perm.end() );
		int p = 0;
		while (perm[p] == 0) p++;
		swap(perm[0], perm[p]);
	}

	string answer( perm.size(), ' ');
	for (int i = 0; i < perm.size(); i++)
		answer[i] = '0' + perm[i];

	return answer;
	
}

void PrintAnswerToTestCase(int caseNumber, string answer )
{
	cout << "Case #" << caseNumber << ": "  << answer << endl;

}

int main()
{
	freopen("large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int numCases;
	cin >> numCases;

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++)
		PrintAnswerToTestCase(caseNumber, SolveTestCase() );

	return 0;
}