#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
char board[50][50];
bool judge(int s, int t) {
	char c = board[s][t];
	int find = 0;
	for (int i = 0;i < 4;++i) {
		if(board[i][t] != c && board[i][t] != 'T') {
			find = 1;
		}
	}
	if(!find)return true;
	find = 0;
	for (int i = 0;i < 4;++i) {
		if(board[s][i] != c && board[s][i] != 'T') {
			find = 1;
		}
	}
	if(!find)return true;
	if(s == t){
		find = 0;
		for (int i = 0;i < 4;++i) {
			if(board[i][i] != c && board[i][i] != 'T') {
				find = 1;
			}
		}
		if(!find)return true;
	} else if((s + t) == 3) {
		find = 0;
		for (int i = 0;i < 4;++i) {
			if(board[3 - i][i] != c && board[3 - i][i] != 'T') {
				find = 1;
			}
		}
		if(!find)return true;
	}
	
	return false;
}
void solve()
{
	for (int i = 0;i < 4;++i) {
		scanf("%s", board[i]);
	}
	int find = 0;
	for (int i = 0;i < 4;++i) {
		for (int j = 0;j < 4;++j) {
			if(board[i][j] == '.') {
				find = 1;
				continue;
			}
			if(board[i][j] == 'T')continue;
			if(judge(i, j)) {
				if(board[i][j] == 'X') {
					cout<<"X won"<<endl;
				} else {
					cout<<"O won"<<endl;
				}
				return;
			}
		}
	}
	if(find == 0) {
		cout<<"Draw"<<endl;
	} else {
		cout<<"Game has not completed"<<endl;
	}	
}
int main()
{
	freopen("data.txt", "r", stdin);
	//freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int n;
	scanf("%d", &n);
	for (int i = 1;i <= n;++i) {
		cout<<"Case #"<<i<<": ";
		solve();
	}
	return 0;
}