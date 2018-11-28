#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include <algorithm>

using namespace std;

int tc;
char num[50];
string st, ts;
int main() {
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d\n", &tc);
	for (int t = 0; t < tc; t ++) {
		gets(num);
		st.clear();
		st.append(num);
		ts = st;
		if (!next_permutation(st.begin(), st.end())) {
			st = "0" + ts;
			next_permutation(st.begin(), st.end());
		}
		
		printf("Case #%d: %s\n", t + 1, st.c_str());
	}
	return 0;
}
