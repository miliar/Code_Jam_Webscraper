#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iomanip>
#include <cmath>
#include <string>
#include <cstdio>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <iostream>
#include <sstream>
#include <cctype>
#include <ctime>
#include <float.h>
#include <bitset>
#include <set>
#include <utility>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <vector>

using namespace std;

#define swap(a,b) {a^=b;b^a=;a^=b;}
#define For(i,a,b) for (int i(a),_b(b); i <= _b ; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b ; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n ; ++i)
#define Repd(i,n) for (int i((n)-1); i>=0 ; --i)
inline int min(int a,int b){return a<b?a:b;}
inline int max(int a,int b){return a>b?a:b;}

string board[5];

bool win(char c){
	int countRow, countCol, countDiag, countAntiDiag;
	Rep(i,4){
		countRow = countCol = 0;
		Rep(j,4){ 
			if (board[i][j] == c || board[i][j] == 'T')
				countRow ++;
			if (board[j][i] == c || board[j][i] == 'T')
				countCol ++;
		}
		if (countRow == 4 || countCol == 4) return true;
	}
	countDiag = countAntiDiag = 0;
	Rep(i,4){
		if (board[i][i] == c || board[i][i] == 'T') countDiag ++;
		if (board[3-i][i] == c || board[3-i][i] == 'T') countAntiDiag ++;
	}
	if (countDiag == 4 || countAntiDiag == 4) return true;
	return false;
}

bool finished(){
	Rep(i,4) Rep(j,4) if (board[i][j] == '.') return false;
	return true;
}

string check(){
	if (win('X')) return "X won";
	if (win('O')) return "O won";
	if (finished()) return "Draw";
	return "Game has not completed";
}

int main(){
    freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
    int T;
    cin >> T;
    Rep(i, T){
        printf("Case #%d: ", i+1);
        Rep(j, 4) cin >> board[j];
        cout << check() << endl;
    }
    return 0;
}