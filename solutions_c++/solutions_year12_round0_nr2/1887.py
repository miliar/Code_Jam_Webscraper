#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <string.h>
#include <algorithm>
#include <boost/lexical_cast.hpp>
#define FOREACH(it, C) for(typeof((C).begin()) it = (C).begin(); it != (C).end(); ++it)
using namespace std;
typedef long long int ll;

vector<int> best_surprising;
vector<int> best_standard;

void preprocessing(const int min_score, const int max_score) {
    best_surprising.resize(max_score * 3, 0);
    best_standard.resize(max_score * 3, 0);
    for(int i = 0; i <= max_score; ++i) {
        for(int j = i; j <= min(max_score, i + 2); ++j) {
            for(int k = j; k <= min(max_score, i + 2); ++k) {
                best_surprising[i + j + k] = max(best_surprising[i + j + k], k);
                if(k - i <= 1)
                    best_standard[i + j + k] = max(best_standard[i + j + k], k);
            }
        }
    }
}

int solve(const int n, const int s, const int p, const vector<int>& scores) {
    vector<vector<int> > result(n + 1, vector<int>(s + 1, 0));
    for(int i = 1; i <= n; ++i) {
        for(int j = 0; j <= s; ++j) {
            result[i][j] = result[i - 1][j] + (best_standard[scores[i - 1]] >= p);
            if(j > 0) {
                result[i][j] = max(result[i][j], result[i - 1][j - 1] + (best_surprising[scores[i - 1]] >= p));
            }
        }
    }
    return result[n][s];
}

int main() {
    preprocessing(0, 10);
    int numberOfCases;
	cin >> numberOfCases;
	for(int testCase = 1; testCase <= numberOfCases; ++testCase) {
        int n, s, p;
        cin >> n >> s >> p;
        vector<int> scores(n);
        for(int i = 0; i < n; ++i) {
            cin >> scores[i];
        }
		cout << "Case #" << testCase << ": " << solve(n, s, p, scores) << endl;
	}
}
/*
2
2
 1
2 3
 4
*/
