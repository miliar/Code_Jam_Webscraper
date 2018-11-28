#include <iostream>
#include<cstring>
#include<cstdio>
#include<string>
#include<algorithm>
using namespace std;
int main(int argc, char *argv[]) {
	int T, t = 1;
	freopen("B-large.in.txt", "r", stdin);
	freopen("B1.out", "w", stdout);
	scanf("%d", &T);
	while (T--) {
		int n, s, p, ret = 0;
		scanf("%d %d %d", &n, &s, &p);
		for (int i=0; i<n; i++) {
			int tmp, mret, dret;
			scanf("%d", &tmp);
			mret = tmp % 3;
			dret = tmp / 3;
			if (dret >= p || (mret >= 1 && dret + 1 >= p))
				ret++;
			else {
				if (mret == 0 && dret + 1 >= p && s > 0 && dret != 0) {
					ret++;
					s--;
				}else if (mret == 2 && dret + 2 >= p && s > 0) {
					ret++;
					s--;
				}
			}
		}
		printf("Case #%d: %d\n", t++, ret);
	}
	return 0;
}