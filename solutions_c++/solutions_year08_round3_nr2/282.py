#include <string>
#include <stdio.h>
#include <iostream>

using namespace std;

int n;

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	scanf("%i", &n);
	string st;
	for (int t = 0; t<n; t++) {
		cin >> st;
		int len = st.size();
		int m = 1;
		for (int i = 1; i<len; i++)
			m *= 3;
		int res = 0, cc, ii;

		long long temp, cur;
		bool plus;
		for (int i = 0; i<m; i++) {
			cur = 0;
			temp = st[0] - '0';
			plus = true;
			ii = i;
			for (int j = 1; j<len; j++) {
				cc = ii % 3;
				switch (cc) {
					case 0: {temp = temp * 10 + st[j] - '0'; break;}
					case 1: {
						if (plus)
							cur += temp; 
						else
							cur -= temp;
						plus = true;
						temp = st[j] - '0'; break;
					}
					case 2: {
						if (plus)
							cur += temp; 
						else
							cur -= temp;
						plus = false;
						temp = st[j] - '0'; break;
					}
				}
				ii /= 3;
			}
			if (plus)
				cur += temp; 
			else
				cur -= temp;
			if (cur % 2 == 0 || cur % 3 == 0 || cur % 5 == 0 || cur % 7 == 0) {
				res++;
			}
		}
		printf("Case #%i: %i\n", t+1, res);
	}


}