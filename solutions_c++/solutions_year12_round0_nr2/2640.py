#include <iostream>
#include <sstream>
#include <vector>
#include <stdlib.h>
#include <queue>
#include <cmath>
#include <cstdio>

using namespace std;

int N, S, p;
int t[30];

void solve()
{
	int ans = 0;
	int s = 0;
	for (int i=0; i<N; i++) {
		int av = t[i] / 3;
		int is_a = 0;
		int is_s = 0;
		if (av > 0) av--;	
		if (av > 0) av--;	
		for (int a=av; a<av+6; a++)
		for (int b=av; b<av+6; b++)
		for (int c=av; c<av+6; c++) {
			if (a+b+c == t[i]) {
				int M = 0;
				int m = 9999999;
				M = max(M, a);
				M = max(M, b);
				M = max(M, c);
				m = min(m, a);
				m = min(m, b);
				m = min(m, c);
				if (M >= p) {
					if (M-m<=1) is_a = 1;
					if (M-m<=2) is_s = 1;
				}
			}
		}	
		if (is_a) ans++;
		else if (is_s) s++;
	}
	ans += min(s, S);
	cout << ans << endl;
}


int main()
{
	int case_num;
	cin >> case_num;

	for (int ca=1; ca<=case_num; ca++) {
		// initialization, IO
		cin >> N >> S >> p;
		for (int i=0; i<N; i++) cin >> t[i];

		cout << "Case #" << ca << ": ";
		solve();

	}
}
