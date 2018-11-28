#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

using namespace std;

void solveCase(int caseNum) {
    vector<string> M;
    vector<int> rowsum, rownum;
    vector<double> wp, owp, oowp;
    int n;

    cin >> n;
    M.resize(n);
    rowsum.resize(n, 0);
    rownum.resize(n, 0);
    wp.resize(n);
    owp.resize(n, 0.0);
    oowp.resize(n, 0.0);

    cout << "Case #" << caseNum << ":" << endl;

    for (int i = 0; i < n; ++i) {
	cin >> M[i];
	for (int j = 0; j < n; ++j) {
	    switch (M[i][j]) {
	    case '1':
		++rowsum[i];
	    case '0':
		++rownum[i];
		break;
	    default:
		;
	    }
	    wp[i] = static_cast<double>(rowsum[i]) / static_cast<double>(rownum[i]);
	}
    }
    for (int i = 0; i < n; ++i) {
	for (int j = 0; j < n; ++j) {
	    if (M[i][j] == '.')
		continue;
	    owp[i] += static_cast<double>(rowsum[j] - (M[i][j] == '0' ? 1 : 0))
		/ static_cast<double>(rownum[j] - 1);
	}
	owp[i] /= static_cast<double>(rownum[i]);
    }
    for (int i = 0; i < n; ++i) {
	for (int j = 0; j < n; ++j) {
	    if (M[i][j] == '.')
		continue;
	    oowp[i] += owp[j];
	}
	oowp[i] /= static_cast<double>(rownum[i]);

	cout << setprecision(12)
	    << (0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]) << endl;
    }
}

int main() {
    int t;
    cin >> t;

    for (int i = 1; i <= t; ++i)
	solveCase(i);

    return EXIT_SUCCESS;
}

