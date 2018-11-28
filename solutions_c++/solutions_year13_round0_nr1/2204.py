#include <functional>
#include <algorithm>
#include <iostream>
#include <memory.h>
#include <utility>
#include <numeric>
#include <iomanip>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <vector>
#include <bitset>
#include <cstdio>
#include <queue>
#include <cmath>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>
using namespace std;
char b[5][5];
bool win(char c){
	char w = 'X' + 'O' - c;
	for (int i = 0;i < 4;++i){
		bool ok = true;
		for (int j = 0;j < 4;++j)
			if (b[i][j] == w || b[i][j] == '.')
				ok = false;
		if (ok) return true;
 	}
	for (int i = 0;i < 4;++i){
		bool ok = true;
		for (int j = 0;j < 4;++j)
			if (b[j][i] == w || b[j][i] == '.')
				ok = false;
		if (ok) return true;
 	}
	
	bool ok = true;
	if (b[0][0] == w || b[0][0] == '.') ok = false;
	if (b[1][1] == w || b[1][1] == '.') ok = false;
	if (b[2][2] == w || b[2][2] == '.') ok = false;
	if (b[3][3] == w || b[3][3] == '.') ok = false;
	if (ok) return true;
	
	ok = true;
	if (b[3][0] == w || b[3][0] == '.') ok = false;
	if (b[2][1] == w || b[2][1] == '.') ok = false;
	if (b[1][2] == w || b[1][2] == '.') ok = false;
	if (b[0][3] == w || b[0][3] == '.') ok = false;
	if (ok) return true;
	return false;
}
bool end(){
	bool ok = true;
	for (int i = 0;i < 4;++i)
		for (int j = 0;j < 4;++j)
			if (b[i][j] == '.')
				ok = false;
	return ok;
}
int main(){
	int t, cnt = 1;
	cin >> t;
	while (t--){
		for (int i = 0;i < 4;++i)
			for (int j = 0;j < 4;++j)
				cin >> b[i][j];
		cout << "Case #" << cnt++ << ": ";
		if (win('O')) cout << "O won" << endl;
		else if (win('X')) cout << "X won" << endl;
		else if (end()) cout << "Draw" << endl;
		else cout << "Game has not completed" << endl;
	}
	return 0;
}