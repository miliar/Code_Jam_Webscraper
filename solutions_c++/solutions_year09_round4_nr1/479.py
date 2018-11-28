#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

bool verify(const vector<int>& A) {
	for (int i=0;i<A.size();++i) if (A[i] > i) return 0;
	return 1;
}

int last_one(const string& s) {
	for (int i=s.length()-1;i>=0;--i) if (s[i]=='1') return i;
	return -1;
}

int main() {
	int NCASES;
	cin >> NCASES;
	for (int z=1;z<=NCASES;++z) {
		int n;
		cin >> n;
		vector<int> A;
		for (int i=0;i<n;++i) {
			string s;
			cin >> s;
			A.push_back(last_one(s));
		}
		int ans = 0;

		for (int i=0;i<n;++i) {
			int our_row = A[i];
			if (our_row <= i) continue;
			int pick = -1;
			for (int j = i+1; j < n; ++j) {
				if (A[j] <= i) {
					pick = j;
					break;
				}
			}
			assert(pick != -1);
			ans += pick-i;
			for (int j=pick;j-1>=i;--j)
				swap(A[j],A[j-1]);
		}
		printf("Case #%d: %d\n", z, ans);
		//assert(verify(A));
	}
}
