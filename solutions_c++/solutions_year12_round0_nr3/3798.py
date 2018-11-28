#include<iostream>
#include<cmath>
#include<algorithm>
#include<cstring>
#include<set>
using namespace std;

int A, B;
char buf[100];

void solve()
{	
	set<int> ts;
	scanf("%d %d", &A, &B);	
	int ans = 0;
	for (int i = A; i < B; i++) {
		ts.clear();
		sprintf(buf, "%d", i);
		int len = strlen(buf);
		for (int j = 1; buf[j]; j++) {
			int flag = 0;
			for (int k = 0; k < len; k++) {
				flag = buf[(j + k) % len] - buf[k];
				if (flag != 0) break;
			}
			if (flag > 0) {
				int tmp = 0;
				for (int k = 0; k < len; k++)
					tmp = tmp * 10 + (buf[(j + k) % len] - '0');
				if (tmp <= B && ts.find(tmp) == ts.end()) {
					ans++;
					ts.insert(tmp);
				}
			}
		}
	}
	printf("%d\n", ans);
}

int main()
{	
	int T, t;
	for (scanf("%d\n", &T), t = 1; t <= T; t++) {
		printf("Case #%d: ", t);		
		solve();
	}
}
