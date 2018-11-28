#include <stdio.h>
#include <algorithm>
#include <memory.h>
#include <queue>
#include <math.h>
#include <vector>
#include <map>
#include <stack>
#include <string.h>
#include <string>
#include <iostream>
#include <deque>
#include <stdlib.h>
#include <stack>
using namespace std;
int _T;

int go(int& x, int y) {
	if (x < y) x++;
	else if (x > y) x--;
}

int main() {
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	scanf("%d",&_T);
	for (int _t=1;_t<=_T;_t++) {
		int n; 
		int cx=1,cy=1;
		vector<int> X,Y;
		vector<string> turn;
		
		cin >> n;
		while (n--) {
			string t; cin >> t;
			int pos; cin >> pos;
			
			if (t == "O") X.push_back(pos);
			else Y.push_back(pos);
			turn.push_back(t);
		}
		X.push_back(1e9);
		Y.push_back(1e9);
		
		int ans = 0;
		while (turn.size() > 0) {
			if (turn[0] == "O") {
				if (cx == X[0]) {
					turn.erase(turn.begin());
					X.erase(X.begin());
				} else go(cx,X[0]);
				go(cy,Y[0]);
			} else {
				if (cy == Y[0]) {
					turn.erase(turn.begin());
					Y.erase(Y.begin());
				} else go(cy,Y[0]);
				go(cx,X[0]);
			}
			ans++;
		}
		
		printf("Case #%d: %d\n",_t,ans);
	}
	
	return 0;
}
