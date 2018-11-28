#include <string>
#include <string.h>
#include <vector>
#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>

using namespace std;

int main() {
	int T;

	scanf("%d", &T);

	for (int C = 1; C <= T; C++) {
		int n, m;
		int answer = 0;
		int a, b, c, d;

		scanf("%d %d", &n, &m);

		if (n >= 10 && n <= 99) { // 2 digits: ab
			for (int i = n; i < m; i++) {
				a = i/10;
				b = i%10;
				// ab < ba
				if (b > a
				&& b*10 + a <= m)
					answer++;
			}
		}
		else if (n <= 999) { // 3 digits: abc
			for (int i = n; i < m; i++) {
				a = i/100;
				b = (i/10)%10;
				c = i%10;
				// abc < cab
				if ((c > a || c == a && a > b)
				&& c*100 + a*10 + b <= m)
					answer++;
				// abc < bca
				if ((b > a || b == a && c > b)
				&& b*100 + c*10 + a <= m)
					answer++;
			}
		}
		/*else if (n <= 9999) { // 4 digits: abcd
			for (int i = n; i < m; i++) {
				a = i/1000;
				b = (i/100)%10;
				c = (i/10)%10;
				d = i%10;
				// abcd < dabc
				if ((d > a || d == a && (a > b || a == b && b > c))
				&& d*1000 + a*100 + b*10 + c <= m){
					answer++;printf("%d - %d\n",i, d*1000 + a*100 + b*10 + c);}
				// abcd < cdab
				if ((c > a || c == a && d > b)
				&& c*1000 + d*100 + a*10 + b <= m){
					answer++;printf("%d - %d\n",i, c*1000 + d*100 + a*10 + b);}
				// abcd < bcda
				if ((b > a || b == a && (c > b || c == b && d > c))
				&& b*1000 + c*100 + d*10 + a <= m){
					answer++;printf("%d - %d\n",i, b*1000 + c*100 + d*10 + a);}
			}
		}*/

		printf("Case #%d: %d\n", C, answer);
	}

	return 0;
}

