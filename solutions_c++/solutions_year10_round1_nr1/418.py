#include <iostream>
#include <stack>
using namespace std;

//char grid[50][50];
struct cell {
	char c;
	bool dright, dleft, h, v;
} grid[50][50];
//stack<char> rows[50];

int main() {
	int t;
	cin >> t;
	for(int kase = 1; kase <= t; kase++) {
		int n, k;
		bool wins[2] = {false};
		cin >> n >> k;
		for(int i = 0 ; i < n; i++) {
			for(int j = 0 ; j < n; j++) {
				grid[i][j].c = '.';
				grid[i][j].dright = true;
				grid[i][j].dleft = true;
				grid[i][j].h = true;
				grid[i][j].v = true;
			}
		}
		for(int i = 0 ; i < n; i++) {
			int count = 0;
			char temp[50] = {'\0'};
			for(int j = 0 ; j < n; j++) {
				/*char c;
				cin >> c;
				rows[i].push(c);*/
				cin >> temp[count];
				if(temp[count] != '.') count++;
			}
			for(int j = count - 1 ; j >= 0; j--) {
				grid[i][n-(count - j)].c = temp[j];
			}
		}
		/*cout << "K = " << k << ", N = " << n << endl;
		for(int i = 0 ; i < n; i++) {
			for(int j = 0 ; j < n; j++) {
				cout << grid[i][j].c << ' ';
			}
			cout << endl;
		}
		cout << endl;*/
		
		for(int i = 0 ; i < n && !(wins[0] && wins[1]); i++) {
			for(int j = 0 ; j < n && !(wins[0] && wins[1]); j++) {
				//cout << grid[i][j].c << ' ';
				if(grid[i][j].c != '.') {
					if(grid[i][j].h && j + k <= n) {
						int match = 1;
						for(int x = 1; x < k && grid[i][j].c == grid[i][j+x].c; x++) {
							match++;
						}
						if(match == k) {
							if(grid[i][j].c == 'R') wins[0] = true;
							else wins[1] = true;
						}
					}
					if(grid[i][j].v && i + k <= n) {
						int match = 1;
						for(int x = 1; x < k && grid[i][j].c == grid[i+x][j].c; x++) {
							match++;
						}
						if(match == k) {
							if(grid[i][j].c == 'R') wins[0] = true;
							else wins[1] = true;
						}
					}
					if(grid[i][j].dright && j + k <= n && i + k <= n) {
						int match = 1;
						for(int x = 1; x < k && grid[i][j].c == grid[i+x][j+x].c; x++) {
							match++;
						}
						if(match == k) {
							if(grid[i][j].c == 'R') wins[0] = true;
							else wins[1] = true;
						}
					}
					if(grid[i][j].dleft && j - k >= -1 && i + k <= n) {
						int match = 1;
						for(int x = 1; x < k && grid[i][j].c == grid[i+x][j-x].c; x++) {
							match++;
						}
						if(match == k) {
							if(grid[i][j].c == 'R') wins[0] = true;
							else wins[1] = true;
						}
					}
				}
			}
			//cout << endl;
		}
		//cout << endl;
		cout << "Case #" << kase << ": ";
		if(wins[0] && wins[1]) cout << "Both" << endl;
		else if(wins[0]) cout << "Red" << endl;
		else if(wins[1]) cout << "Blue" << endl;
		else cout << "Neither" << endl;
	}
}
