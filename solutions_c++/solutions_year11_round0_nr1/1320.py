


/*
	Prob: (Google code jam 2011 - Qualification Round - A)
	Author: peanut
	Time: 07/05/11 19:23
	Description: ^_^
*/

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

int T, N, O, B, O_T, B_T, c, s;

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	
	scanf("%d", &T);
	for (int cs = 1; cs <= T; ++ cs) {
		scanf("%d", &N);
		s = 0;
		O = B = 1;
		O_T = B_T = 0;
		for (int k = 1; k <= N; ++ k) {
			char ch;
			scanf(" %c %d", &ch, &c);
			if (ch == 'O') {
				s = max(s, abs(O - c) + O_T);
				O_T = ++ s;
				O = c;
			}
			else {
				s = max(s, abs(B - c) + B_T);
				B_T = ++ s;
				B = c;
			}
		}
		printf("Case #%d: %d\n", cs, s);
	}
	
	return 0;
}
