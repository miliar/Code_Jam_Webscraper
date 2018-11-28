#include <stdio.h>
#include <vector>

using namespace std;

int main() {

	int n;
	scanf("%d",&n);

	for (int k=1;k<=n;k++) {

		int orb[110][2];
		int brb[110][2];
		int ob = 0;
		int bb = 0;

		int m,i;
		scanf("%d", &m);

		for (i=0;i<110;i++) {
			orb[i][0] = 0;
			orb[i][1] = 0;
			brb[i][0] = 0;
			orb[i][1] = 0;
		}
		for (i=0;i<m;i++) {
			char a;
			int b;
			scanf(" %c %d", &a, &b);
			if (a=='O') {
				ob++;
				orb[ob][0] = b;
				orb[ob][1] = i;
			}
			if (a=='B') {
				bb++;
				brb[bb][0] = b;
				brb[bb][1] = i;
			}
		}
		orb[0][0] = 1;
		brb[0][0] = 1;

		int op = 1;
		int bp = 1;
		int ans = 0;
		if (ob == 0) orb[1][1] = -1;
		for (i=0; i<m;i++) {
			if((bp > bb && op < ob)|| orb[op][1] == i) {
				int tmp = orb[op][0] - orb[0][0];
				if (tmp < 0) tmp *= -1;
				orb[0][0] = orb[op][0];
				op++;
				ans += tmp + 1;

				int tmp2 = brb[bp][0] - brb[0][0];
				int temp2 = (tmp2<0)? -1*tmp2:tmp2;
				if (temp2 <= tmp+1) brb[0][0] = brb[bp][0];
				else brb[0][0] += ((tmp2<0)? -1:1) * (tmp+1);
			}
			else {
				int tmp = brb[bp][0] - brb[0][0];
				if (tmp < 0) tmp *= -1;
				brb[0][0] = brb[bp][0];
				bp++;
				ans += tmp + 1;

				int tmp2 = orb[op][0] - orb[0][0];
				int temp2 = (tmp2<0)? -1*tmp2:tmp2;
				if (temp2 <= tmp+1) orb[0][0] = orb[op][0];
				else orb[0][0] += ((tmp2<0)? -1:1) * (tmp+1);
			}
		}	
		printf("Case #%d: %d\n",k,ans);
	}

	return 0;
}