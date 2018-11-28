#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

char board[100][100];

int dx[] = {1, 1, 1, 0, -1, -1, -1, 0};
int dy[] = {1, 0, -1, -1, -1, 0, 1, 1};

void gravity(int s){
	for (int i=0; i<s; i++){
		bool good = true;
		int pos = s-1;
		for (int j=s-1; j+1; j--){
			if (board[j][i] != '.'){
				swap(board[pos][i], board[j][i]);
				pos--;
			}
		}
	}
}

int parse(char c, int dx, int dy, int n, int sz){
	for (int i=0; i<n; i++){
		for (int j=0; j<n; j++){
			if (board[i][j] == c){
				bool good = true;
				int x = i;
				int y = j;
				for (int k=0; k<sz; k++, x += dx, y += dy){
					if (x >= n || x < 0 || y >= n || y < 0 || board[x][y] != c){
						good = false;
						break;
					}
				}
				if (good)
					return 1;
			}
		}
	}
	return 0;
}

int main(){
	int t;
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	cin >> t;
	char buf[100];
	for (int I=0; I<t; I++){
		cout << "Case #" << I+1 << ": ";
		int n, k;
		cin >> n >> k;
		for (int i=0; i<n; i++){
			cin >> buf;
			for (int j=0; j<n; j++){
				board[j][n-i-1] = buf[j];
			}
		}
		gravity(n);
		int ret = 0;
		for (int j=0; j<8; j++){
			ret |= parse('R', dx[j], dy[j], n, k);
			ret |= parse('B', dx[j], dy[j], n, k)*2;
		}
		if (ret == 3){
			cout << "Both\n";
		} else if (ret == 2){
			cout << "Blue\n";
		} else if (ret == 1){
			cout << "Red\n";
		} else {
			cout << "Neither\n";
		}
	}
	
	return 0;
}