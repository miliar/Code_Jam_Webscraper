//Sat May  7 14:27:19 CDT 2011
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int solve(int N) {
	int opos = 1;
	int bpos = 1;
	int sum = 0;
	int sliceA = 0;
	int sliceB = 0;
	char c;
	int number;
	for (int i = 0; i < N; i++) {
		cin >> c >> number;
		if (c == 'O') {
			int tmp = abs(number - opos);
			if (tmp >= sliceB) {
				sum += tmp - sliceB + 1;
				sliceA += tmp - sliceB + 1;
				sliceB = 0;
			} else {
				sum += 1;
				sliceB = 0;
				sliceA = 1;
			}
			opos = number;
		} else {
			int tmp = abs(number - bpos);
			if (tmp >= sliceA) {
				sum += tmp - sliceA + 1;
				sliceB += tmp - sliceA + 1;
				sliceA = 0;
			} else {
				sum += 1;
				sliceA = 0;
				sliceB = 1;
			}
			bpos = number;
		}
//		cout << opos << ", " << bpos << endl;
//		cout << sliceA << ", " << sliceB << endl;
	}
	return sum;
}

int main(int argc, const char* argv[]) {
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N;
		cin >> N;
		cout << "Case #" << t << ": " << solve(N) << endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
