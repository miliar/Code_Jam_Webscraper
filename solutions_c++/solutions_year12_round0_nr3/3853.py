#include <iostream>
#include <string.h>
#include <stdio.h>

using namespace std;

int flag[3000000] = {0};

int highest(int x) {
	int res = 1;
	while (x) {
		res *= 10;
		x /= 10;
	}
	return res / 10;
}

int main() {
	//printf("%d\n", highest(1));	return -2;
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int a, b;
		scanf("%d%d", &a, &b);
		int res = 0;
		for (int num = a; num <= b; num++) {
			//printf("check %d: ", num);
			int high = highest(num);
			int newnum = num;
			do {
				int h = newnum / high;
				newnum -= h * high;
				newnum *= 10;
				newnum += h;
				//printf("%d ", newnum);
				if (newnum > num && newnum <= b && flag[newnum] != num) {
					flag[newnum] = t;
					res++;
					//printf("(*) ");
				}
			} while (newnum != num);
			//putchar(10);
		}
		printf("Case #%d: %d\n", t, res);
	
	}
	
}

