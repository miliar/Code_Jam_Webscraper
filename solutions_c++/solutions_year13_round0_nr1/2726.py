#include <iostream>
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>

using namespace std;

#define FOR(i,a,b) for(int i = a ; i < b ; i++)
#define pb push_back
#define FOREACH(x,y) for(typeof(y.begin()) x = y.begin() ; x != y.end() ; x++)

#define LL long long

LL MOD = 1000000007;

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tc;
	cin >> tc;
	for(int t = 1 ; t <= tc ; t++) {
		bool xwin, owin, draw;
		xwin = owin = draw = false;
		int xn,on,tn;
		char arr[4][4];
		bool flag = false;
		for(int i = 0 ; i < 4 ; i++) {
			xn = on = tn = 0;
			for(int j = 0 ; j < 4 ; j++) {
				cin >> arr[i][j];
				if(arr[i][j] == '.') {
					flag = true;
				} else if(arr[i][j] == 'X') {
					xn++;
				} else if(arr[i][j] == 'O') {
					on++;
				} else if(arr[i][j] == 'T') {
					tn++;
				}
			}
			if(xn == 4 || xn + tn == 4) xwin = true;
			if(on == 4 || on + tn == 4) owin = true;
		}
		scanf("%*c");
		for(int i = 0 ; i < 4 ; i++) {
			xn = on = tn = 0;
			for(int j = 0 ; j < 4 ; j++) {
				if(arr[j][i] == 'X') {
					xn++;
				} else if(arr[j][i] == 'O') {
					on++;
				} else if(arr[j][i] == 'T') {
					tn++;
				}
			}
			if(xn == 4 || xn + tn == 4) xwin = true;
			if(on == 4 || on + tn == 4) owin = true;
		}
		xn = on = tn = 0;
		for(int i = 0 ; i < 4 ; i++) {
			if(arr[i][i] == 'X') {
				xn++;
			} else if(arr[i][i] == 'O') {
				on++;
			} else if(arr[i][i] == 'T') {
				tn++;
			}
		}
		if(xn == 4 || xn + tn == 4) xwin = true;
		if(on == 4 || on + tn == 4) owin = true;
		xn = on = tn = 0;
		for(int i = 0 ; i < 4 ; i++) {
			if(arr[i][3-i] == 'X') {
				xn++;
			} else if(arr[i][3-i] == 'O') {
				on++;
			} else if(arr[i][3-i] == 'T') {
				tn++;
			}
		}
		if(xn == 4 || xn + tn == 4) xwin = true;
		if(on == 4 || on + tn == 4) owin = true;
		cout << "Case #" << t << ": ";
		if(xwin && !owin) cout << "X won" << endl;
		if(owin && !xwin) cout << "O won" << endl;
		if(xwin && owin) {
			if(!flag) {
				cout << "Draw" << endl;
			} else {
				cout << "Game has not completed" << endl;
			}
		}
		if(!xwin && !owin) {
			if(!flag) {
				cout << "Draw" << endl;
			} else {
				cout << "Game has not completed" << endl;
			}
		}
	}
	return (0);
}