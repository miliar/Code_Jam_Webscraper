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
	cout.precision(12);
	cout << "Case #" << caseNumber << ":" << endl;
	for (int i = 0; i < ans.size(); i++)
		cout << ans[i] << endl;
}

template <class AnswerType>
AnswerType SolveTestCase() {
	int n;
	cin >> n;
	vector<string> field(n);
	for (int i = 0; i < n; i++)
		cin >> field[i];

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) 
			if (field[i][j] == '0' && field[j][i] != '1') {
				cerr << "Error!!!" << endl;
				exit(0);
			}
	}

	vector<double> ans(n, 0);
	vector<double> wins(n, 0);
	vector<double> owp(n, 0);
	vector<int> games(n, 0);

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (field[i][j] != '.')
				games[i]++;
			if (field[i][j] == '1')
				wins[i]++;
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (field[i][j] != '.') {
				owp[i] += (wins[j] - (field[j][i] - '0')) / (games[j] - 1);
			}
		}
		owp[i] /= games[i];
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (field[i][j] != '.') {
				ans[i] += owp[j];
			}
		}
		ans[i] = 0.25 * ans[i] /games[i] +  0.5 * owp[i] + 0.25 * wins[i] / games[i];
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
		PrintAnswerToTestCase(caseNumber, SolveTestCase< vector<double> >() );

	return 0;
}