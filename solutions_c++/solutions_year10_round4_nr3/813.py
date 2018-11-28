#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <utility>
#include <string>
#include <cstring>
using namespace std;

int field[2][101][101];

string calc()
{
	stringstream S;
	int i, j, k;

	memset(field, 0, sizeof(field));

	int R;
	cin >> R;
	int x1, y1, x2, y2;
	for (i=0; i<R; ++i) {
		cin >> x1 >> y1 >> x2 >> y2;
		for (j=x1; j<=x2; ++j) for (k=y1; k<=y2; ++k) {
			field[0][k][j] = 1;
		}
	}

	int ans = 0;
	int pre = 0;
	int cur = 1;
	while (1) {
		bool found = false;
		for (i=1; i<101; ++i) {
			for (j=1; j<101; ++j) {
				//cout << field[pre][i][j];
				if (field[pre][i][j]) {
					found = true;
					//break;
				}
			}
			//cout << endl;
		}
		if (!found) break;
		//cout << endl;

		//memset(&field[cur][0][0], 0, sizeof(field)/2);

		for (i=1; i<101; ++i) for (j=1; j<101; ++j) {
			if (field[pre][i-1][j] && field[pre][i][j-1]) {
				field[cur][i][j] = 1;
			} else if (!field[pre][i-1][j] && !field[pre][i][j-1]) {
				field[cur][i][j] = 0;
			} else {
				field[cur][i][j] = field[pre][i][j];
			}
		}

		ans++;
		pre = 1-pre;
		cur = 1-cur;
	}


	S << ans;
	return S.str();
}

int main(void)
{
	int caseNum;
	cin >> caseNum;
	//string line;
	//getline(cin, line);
	for (int c=1; c<=caseNum; ++c) {
		cout << "Case #" << c << ": " << calc() << endl;
	}

	return 0;
}

