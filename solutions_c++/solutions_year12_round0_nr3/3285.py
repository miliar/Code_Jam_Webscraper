#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
using namespace std;

int get_recycled_pairs(int x, int A) {
	vector <int> ret;
	char X[8];
	char Y[8];
	sprintf(X, "%d", x);
	int l = strlen(X);
	Y[l] = 0;
	
	for (int i = 1; i < l; i++) {
		for (int j = i; j < l; j++)
			Y[j - i] = X[j];
		for (int j = 0; j < i; j++)
			Y[l - i + j] = X[j];
		
		if (Y[0] != '0') {
			int y;
			sscanf(Y, "%d", &y);
			if (A <= y && y < x)
				ret.push_back(y);
		}
	}	
	return (unique(ret.begin(), ret.end()) - ret.begin());
}

int main(void) {
	int testnum;
	scanf("%d\n", &testnum);

	for (int testcase = 1; testcase <= testnum; testcase++) {
		int ans = 0;
		int A, B;
		scanf("%d %d", &A, &B);
		
		for (int i = A; i <= B; i++) {
			ans += get_recycled_pairs(i, A);
		}
		printf("Case #%d: %d\n", testcase, ans);
	}
	return 0;
}

