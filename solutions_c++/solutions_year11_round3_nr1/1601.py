#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void solveCase(int caseNum) {
    int r, c;
    vector<string> pic;
    bool possible = true;

    cin >> r >> c;
    pic.resize(r);
    for (int i = 0; i < r; ++i)
	cin >> pic[i];

    for (int i = 0; i < r && possible; ++i)
	for (int j = 0; j < c && possible; ++j)
	    if (pic[i][j] == '#') {
		if (i + 1 < r && j + 1 < c &&
		    pic[i][j + 1] == '#' && pic[i + 1][j] == '#' &&
		    pic[i + 1][j + 1] == '#') {
		    pic[i][j] = pic[i + 1][j + 1] = '/';
		    pic[i + 1][j] = pic[i][j + 1] = '\\';
		}
		else
		    possible = false;
	    }
    
    cout << "Case #" << caseNum << ":" << endl;

    if (possible)
        for (int i = 0; i < r; ++i)
	    cout << pic[i] << endl;
    else
	cout << "Impossible" << endl;
}

int main() {
    int t;

    cin >> t;
    for (int i = 1; i <= t; ++i)
	solveCase(i);

    return EXIT_SUCCESS;
}

