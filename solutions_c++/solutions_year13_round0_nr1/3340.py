#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;
const int N = 100005;
typedef long long LL;

char mat[5][5];
bool judge(char ch){
	int cnt;
	for (int i = 0 ; i < 4; ++i){
		cnt = 0;
		for (int j = 0; j < 4; ++j)
			if (mat[i][j] == ch || mat[i][j] == 'T')
				cnt++;
		if (cnt == 4) return true;
		cnt = 0;
		for (int j = 0; j < 4; ++j)
			if (mat[j][i] == ch || mat[j][i] == 'T')
				cnt++;
		if (cnt == 4) return true;
	}
	cnt = 0;
	for (int i = 0; i < 4; ++i)
		if (mat[i][i] == ch || mat[i][i] == 'T')
			cnt++;
	if (cnt == 4) return true;
	cnt = 0;
	for (int i = 0,j = 3; i < 4; ++i,--j)
		if (mat[i][j] == ch || mat[i][j] == 'T')
			cnt++;
	if (cnt == 4) return true;
	return false;
}
int main(){
	int T;
	scanf("%d", &T);
	for (int cs = 1; cs <= T; ++cs){
		int emp = 0;
		for (int i = 0; i < 4; ++i){
			scanf("%s", mat[i]);
			for (int j = 0; j < 4; ++j)
				if (mat[i][j] == '.')
					emp++;
		}
		printf("Case #%d: ", cs);
		bool x = judge('X');
		bool o = judge('O');
		if (x && !o) puts("X won");
		else if (!x && o) puts("O won");
		else if (!x && !o){
			if (emp > 0) puts("Game has not completed");
			else puts("Draw");
		}
	}
	return 0;
}