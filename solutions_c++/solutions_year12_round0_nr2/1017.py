#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int readInt() {int N; cin >> N; return N;}

#define BUG(x) cout << #x << " = " << x << endl

map <int, vector < vector <int> > > surprisingTriplets;
map <int, vector < vector <int> > > nonSurprisingTriplets;
vector < vector <bool> > seen;
vector < vector <int> > memoized;

bool isValidTriplet(int a, int b, int c) {
	return max(a, max(b, c)) - min(a, min(b, c)) <= 2;
}

bool isSurprising(int a, int b, int c) {
	return (max(a, max(b, c)) - min(a, min(b, c)) == 2);
}

vector <int> makeVector(int a, int b, int c) {
	vector <int> result;
	result.push_back(a); result.push_back(b); result.push_back(c);
	return result;
}

void initialize() {
	for (int i = 0; i <= 10; ++i)
		for (int j = i; j <= 10; ++j)
			for (int k = j; k <= 10; ++k)
				if (isSurprising(i, j, k))
					surprisingTriplets[i + j + k].push_back(makeVector(i, j, k));
				else if (isValidTriplet(i, j, k))
					nonSurprisingTriplets[i + j + k].push_back(makeVector(i, j, k));
}

void initializeVariables(int N, int S) {
	seen.clear(); seen.resize(N + 1, vector <bool> (S + 1, false));
	memoized.clear(); memoized.resize(N + 1, vector <int> (S + 1, 0));
}

bool hasElement(vector < vector <int> >& vec, int p) {
	for (int i = 0; i < vec.size(); ++i)
		for (int j = 0; j < vec[i].size(); ++j)
			if (vec[i][j] >= p)
				return true;
	return false;
}

int calculateMaximalGooglers(int N, int S, int p, vector <int>& totalScore) {
	if (N == 0) return 0;
	else if (seen[N][S]) return memoized[N][S];
	seen[N][S] = true;
	int score = 0;
	if (S > 0 && hasElement(surprisingTriplets[totalScore[N - 1]], p))
		score = 1 + calculateMaximalGooglers(N - 1, S - 1, p, totalScore);
	if (hasElement(nonSurprisingTriplets[totalScore[N - 1]], p))
		score = max(score, 1 + calculateMaximalGooglers(N - 1, S, p, totalScore));
	score = max(score, calculateMaximalGooglers(N - 1, S, p, totalScore));
	return memoized[N][S] = score;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int nTestCases = readInt();
	initialize();
	for (int testCase = 1; testCase <= nTestCases; ++testCase) {
		int N = readInt(), S = readInt(), p = readInt();
		vector <int> totalScore(N, 0);
		for (int i = 0; i < totalScore.size(); ++i)
			totalScore[i] = readInt();
		initializeVariables(N, S);
		int maximalGooglers = calculateMaximalGooglers(N, S, p, totalScore);
		printf("Case #%d: %d\n", testCase, maximalGooglers);
	}
	return 0;
}
