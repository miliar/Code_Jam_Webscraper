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

void PrintAnswerToTestCase(size_t caseNumber, vector<int> ans)
{
	int different = 0;
	for (int i = 0; i < ans.size(); i++)
		if (ans[i] > 0) different++;
	cout << "Case #" << caseNumber << ": " << different << endl;
	for (int i = ans.size() - 1; i > -1; i--)
		if (ans[i] > 0) {
			cout << i + 1 << " " << ans[i] << endl;
 		}
}

template <class AnswerType>
AnswerType SolveTestCase(const vector< vector<bool> > & grid) {
	vector< vector<int> > goodH(grid.size(), vector<int>(grid[0].size(), 0) );
	vector< vector<int> > goodV(grid.size(), vector<int>(grid[0].size(), 0) );

	for (size_t i = 0; i < grid.size(); i++) {
		for (size_t j = 1; j < grid[i].size(); j++)
			if (grid[i][j] == grid[i][j - 1]) {
				goodH[i][j] = j;
			} else {
				goodH[i][j] = goodH[i][j - 1];
			}
	}

	for (size_t j = 0; j < grid[0].size(); j++) {
		for (size_t i = 1; i < grid.size(); i++)
			if (grid[i][j] == grid[i - 1][j]) {
				goodV[i][j] = i;
			} else {
				goodV[i][j] = goodV[i - 1][j];
			}
	}

	vector< vector<int> > maxChess( grid.size(), vector<int>(grid[0].size(), 0) );
	for (size_t i = 0; i < maxChess.size(); i++)
		for (size_t j = 0; j < maxChess[i].size(); j++) {
			size_t maxLength = min(maxChess.size() - i, maxChess[i].size() - j);
			for (size_t length = 0; length < maxLength; length++)
				if (goodV[i + length][j + length] <= i && goodH[i + length][j + length] <= j
					&& goodV[i + length][j] <= i && goodH[i][j + length] <= j) 
				{
					maxChess[i][j] = length;
				} else {
					break;
				}
			}

	vector< vector<bool> > covered(grid.size(), vector<bool>(grid[0].size(), false) );
	vector<int> ans(min(maxChess.size(), maxChess[0].size()) + 1);
	for (int length = ans.size() - 1; length > -1; length--) {
		for (size_t i = 0; i < maxChess.size(); i++)
			for (size_t j = 0; j < maxChess[i].size(); j++)
				if (maxChess[i][j] == length) {
					if (covered[i][j] || covered[i + length][j + length] ||
						covered[i][j + length] || covered[i + length][j])
					{
						maxChess[i][j]--;
					} else {
						ans[length]++;
						for (size_t ii = i; ii <= i + length; ii++)
							for (size_t jj = j; jj <= j + length; jj++)
								covered[ii][jj] = true;
					}
				}
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

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++) {
		int m, n;
		cin >> m >> n;
		vector< vector<bool> > grid(m, vector<bool>(n, false) );
		string str;
		getline(cin, str);
		for (int i = 0; i < m; i++) {
			getline(cin, str);
			for (int j = 0; j < str.size(); j++) {
				int num = 0;
				if (str[j] <= '9' && str[j] >= '0') {
					num = str[j] - '0';
				} else {
					num = 10 + str[j] - 'A';
				}
				for (int h = 0; h < 4; h++) {
					if (num & (1 << h))
						grid[i][4 * j + 3 - h] = true;
				}
			}
		}
		PrintAnswerToTestCase(caseNumber, SolveTestCase< vector<int> >(grid) );
	}

	return 0;
}