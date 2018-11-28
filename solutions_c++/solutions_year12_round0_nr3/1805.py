#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>

using namespace std;

int main() {
	int T;
	cin >> T;
	for(int c = 1; c <= T; ++c) {
		int a, b;
		cin >> a >> b;
		int keta = 1;
		for(int i = a; i >= 10; i /= 10) keta *= 10;
		int res = 0;
		for(int i = a; i < b; ++i) {
			for(int j = i / 10 + keta * (i % 10); j != i; j = j / 10 + keta * (j % 10)) {
				if(i < j && j <= b) ++ res;
			}
		}
		printf("Case #%d: %d\n", c, res);
	}
	return 0;
}
