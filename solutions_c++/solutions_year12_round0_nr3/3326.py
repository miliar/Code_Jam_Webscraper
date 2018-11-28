#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <map>

using namespace std;


map<int, int> delDou;
int T, A, B;
int tmp;
int lenVal;
char chA[10];
int chg[10];


int main() {
	freopen("C.in", "r", stdin);
	freopen("Ans.txt", "w", stdout);
	scanf("%d", &T);
	for(int ca = 1; ca <= T; ++ca) {
		scanf("%d %d", &A, &B);
		long long ans = 0;
		for(int tt = A; tt < B; ++tt) {
			delDou.clear();
			sprintf(chA, "%d", tt);
			lenVal = strlen(chA);
			for(int i = 1; i < lenVal; ++i) {
				int val = 0;
				for(int j = lenVal - i; j < lenVal; ++j) {
					val = val * 10 + chA[j] - '0';
				}
				for(int j = 0; j < lenVal - i; ++j) {
					val = val * 10 + chA[j] - '0';
				}
				if(val > tt && val <= B) delDou[val] = 1;
			}
			ans += delDou.size();
		}
		printf("Case #%d: %lld\n", ca, ans);
	}
	return 0;
}
