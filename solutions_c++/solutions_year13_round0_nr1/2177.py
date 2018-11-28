#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>

using namespace std;

int main()
{
	int t;
	scanf("%d", &t);
	getchar();

	for(int i = 1;  i <= t; i++) {
		int flag = 0;
		int ctr = 0;
		char c[4][4];
		int b[10] = {0};
		for(int j = 0; j < 4; j++) {
			for(int k = 0; k < 4; k++) {
				scanf("%c", &c[j][k]);
				if(c[j][k] == '.') ctr++;
				if(j == k) b[4] += (int)c[j][k];
				else if(j == 3-k) b[5] += (int)c[j][k];
				b[j] += (int)c[j][k];
			}
			getchar();
		}
		for(int j = 0; j < 4; j++) 
			for(int k = 0; k  < 4; k++) b[6+j] += c[k][j];

		int ans[4] = {0};
		ans[0] = (int)(4*'X');
		ans[1] = (int)(4*'O');
		ans[2] = (int)(3*'X' + 'T');
		ans[3] = (int)(3*'O' + 'T');

		for(int j = 0; j < 10; j++) {
			for(int k = 0; k < 4; k++) {
				if(b[j] == ans[k]) {
					if(k == 0 || k == 2) printf("Case #%d: X won\n", i);
					else if(k == 1 || k == 3) printf("Case #%d: O won\n", i);
					flag = 1;
					break;
				}
			}
			if(flag == 1) break;
		}
		if(flag == 0 && ctr != 0)printf("Case #%d: Game has not completed\n", i);
		else if(flag == 0 && ctr == 0) printf("Case #%d: Draw\n", i);
		getchar();
	}
	return 0;
}




