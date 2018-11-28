#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <ctype.h>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <list>
#include <stack>
using namespace std;
#define PB			push_back
#define ALL(v)			(v).begin() , (v).end()
#define SZ(v)			( (int) v.size() )
#define Set(v,x)		memset(  v , x , sizeof(v))
#define two(n)			( 1 << (n) )
#define contain(S,i)		( (S) & two(i) ) 
#define SQR(v)			( (v) * (v) )
#define ABS(x)			( ( (x) >= 0 ) ? (x) : -(x) )
#define foreach(v,it)		for( typeof((v).begin()) it = (v).begin() ; it != (v).end() ; it++ )

void solve() {
	int res = 0 , N , i , j;
	string color;

	vector<int> blue, red, b;
	vector<char> robot;
	
	cin >> N;
	for (i = 0 ; i < N ; i++) {
		cin>> color >> j;
		robot.PB(color[0]);
		b.PB(j);
		if (color[0] == 'B') 	blue.PB(j);
		else			red.PB(j);
	}
	int curBlue = 1 , curRed = 1 , vb = 0,vr = 0 , d;
	for (i = 0 ; i < N ; i++) {
		if (robot[i] == 'B') {
			d = abs(curBlue - b[i])+1;
			curBlue = b[i];
			res += d;
			vb++;
			if (vr < (int)red.size()) {
				j = abs(curRed - red[vr]);
				if (j <= d ) {
					curRed = red[vr];
				}
				else {
					if (curRed > red[vr])
						curRed -= d;
					else
						curRed += d;
				}
			}
		}
		else {
			d = abs(curRed - b[i])+1;
			curRed = b[i];
			res += d;
			vr++;
			if ( vb < (int)blue.size()) {
				j = abs(curBlue - blue[vb]);
				if (j <= d ) {
					curBlue = blue[vb];
				}
				else {
					if (curBlue > blue[vb])
						curBlue -= d;
					else
						curBlue += d;
				}
			}
		}
	}
	cout << res << endl;
}

int main() {
	int C , nc;
	
	scanf("%d\n", &C);
	for ( nc = 1 ; nc <= C ; nc++) {
		cout << "Case #" << nc << ": ";
		solve();
	}	
	return 0;
}
