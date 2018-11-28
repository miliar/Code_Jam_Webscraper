#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <set>

using namespace std;

int main()
{
	freopen("C:\\Projects\\gcj\\input.txt", "r", stdin);
	freopen("C:\\Projects\\gcj\\output.txt", "w", stdout);
	int z;
	cin >> z;
	for (int q=0;q<z;q++) {
		int r, c;
		cin >> r >> c;

		vector<string> board;
		for (int i=0;i<r;i++) {
			string str;
			cin >> str;
			board.push_back(str);
		}

		bool flag = true;
		for (int i=0;i<r;i++) {
			for (int j=0;j<c;j++) {
				if (board[i][j] == '#') {
					if (i+1 >= r || j+1 >=c || board[i+1][j] != '#' || board[i][j+1] != '#' || board[i+1][j+1] != '#') {
						flag = false;
						break;
					}
					board[i][j] = '/';
					board[i+1][j] = '\\';
					board[i][j+1] = '\\';
					board[i+1][j+1] = '/';
				}
			}
			if (!flag) break;
		}

		cout << "Case #" << (q+1) << ":" << endl;

		if (flag) {
			for (int i=0;i<r;i++) {
				cout << board[i] << endl;
			}
		}
		else {
			cout << "Impossible" << endl;
		}
	}

	fclose(stdout);
	fclose(stdin);
	return 0;
}
