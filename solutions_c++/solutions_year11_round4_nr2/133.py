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
	if (ans == 0) {
		cout << "Case #" << caseNumber << ": IMPOSSIBLE" << endl;
	} else {
		cout << "Case #" << caseNumber << ": " << ans << endl;
	}
}

void GetSums(vector< vector<long long > >& sums,  const vector< vector<long long> > & field, int type) {
	int n = field.size();
	int m = field[0].size();
	sums = vector< vector<long long > > (n + 1, vector<long long>(m + 1, 0));
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++) {
			int factor = 0;
			if (type == 1)
				factor = 1;
			if (type == 2)
				factor = i - 1;
			if (type == 3)
				factor = j - 1;
			sums[i][j] = sums[i][j - 1] + sums[i - 1][j] - sums[i - 1][j - 1] + factor * field[i - 1][j - 1];
		}
}

long long GetBladeWeight(const vector< vector<long long > >& sums,  const vector< vector<long long> >& field, int i, int j, int k, int type) {
	long long squareSum = sums[i + k][j + k] - sums[i][j + k] - sums[i + k][j] + sums[i][j];
	if (type == 1)
		squareSum -= field[i][j] + field[i + k - 1][j + k - 1] + field[i][j + k - 1] + field[i + k - 1][j];
	if (type == 2)
		squareSum -= i * field[i][j] + (i + k - 1) * field[i + k - 1][j + k - 1] +  i * field[i][j + k - 1] +  (i + k - 1) * field[i + k - 1][j];
	if (type == 3)
		squareSum -= j * field[i][j] + (j + k - 1) * field[i + k - 1][j + k - 1] +  (j + k - 1) * field[i][j + k - 1] +  j * field[i + k - 1][j];
		
	return squareSum;
}

template <class AnswerType>
AnswerType SolveTestCase() {
	int n, m, d;
	cin >> n >> m >> d;
	vector< vector<long long> > field(n, vector<long long>(m, 0) );
	for (int i = 0; i < n; i++) {
		string s;
		cin >> s;
		for (int j = 0; j < m; j++)
			field[i][j] = d + (s[j] - '0');
	}
	vector< vector<long long > > sumX;
	vector< vector<long long > > mass;
	vector< vector<long long > > sumY;
	GetSums(mass, field, 1);
	GetSums(sumY, field, 2);
	GetSums(sumX, field, 3);


	for (int k = min(m, n); k > 2; k--) {
		for (int i = 0; i <= n - k; i++)
			for (int j = 0; j <= m - k; j++) {
				long long curMass = GetBladeWeight(mass, field, i, j, k, 1);
				long long curY = GetBladeWeight(sumY, field, i, j, k, 2);
				long long curX = GetBladeWeight(sumX, field, i, j, k, 3);
				if (curMass * (2 * i + k - 1) == 2 * curY && curMass * (2 * j + k - 1) == 2 * curX)
					return k;
			}

	}

	return 0;
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