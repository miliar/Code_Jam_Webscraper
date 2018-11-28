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
AnswerType SolveTestCase(vector< vector<bool> > grid) {
	int ans = 0;
	while (true) {
		vector< vector<bool> > newgrid(grid.size(), vector<bool> (grid[0].size(), false) ); 
		bool live = false;
		for (int i = 0; i < grid.size(); i++)
			for (int j = 0; j < grid.size(); j++) {
				if (grid[i][j]) {
					live = true;
					newgrid[i][j] = (grid[i - 1][j] || grid[i][j - 1]);
				} else if (i > 0 && j > 0 && grid[i - 1][j] && grid[i][j - 1]) {
					newgrid[i][j] = true;
				}
			}
		grid = newgrid;
		if (!live) break;
		ans++;
	}
	return ans;
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
		vector< vector<bool> > grid(300, vector<bool>(300, false));
		int r;
		int x1, y1, x2, y2;
		cin >> r;
		for (int i = 0; i < r; i++) {
			cin >> x1 >> y1 >> x2>> y2;
			for (int i = y1; i <= y2; i++)
				for (int j = x1; j <= x2; j++)
					grid[i][j] = true; 
		}
		PrintAnswerToTestCase(caseNumber, SolveTestCase<int>(grid) );
	}

	return 0;
}