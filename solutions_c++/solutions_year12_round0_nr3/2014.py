#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<cmath>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<sstream>
#include<algorithm>
#include<complex>
#include<set>
using namespace std;
#define MP make_pair
#define F first
#define S second
#define PB push_back
bool used[2000111];
long long Cal(int lowBound, int highBound) {
	long long Ret = 0;
	memset(used, 0, sizeof(used));
	for(int num = lowBound; num <= highBound; num ++) {
		if (used[num]) continue;
		vector<int> digit;
		int tmp = num;
		while (tmp > 0) {
			digit.PB(tmp % 10);
			tmp /= 10;
		}
		reverse(digit.begin(), digit.end());
		set<int> box;
		for(int i = 0; i < digit.size(); i ++) {
			int cur = 0;
			if (digit[i] == 0) continue;
			cur = digit[i];
			for(int j = (i + 1) % digit.size(); j != i; j = (j + 1) % digit.size()) cur = cur * 10 + digit[j];
			if (cur <= highBound && cur >= lowBound) {
				box.insert(cur);
				used[cur] = true;
			}
		}
		int nb = box.size();
		Ret += 1LL * nb * (nb - 1) / 2;
	}
	return Ret;
}
void process(int test)  {
	int a, b;
	scanf("%d", &a);
	scanf("%d", &b);
	long long Count1 = Cal(a, b);
	printf("Case #%d: %I64d\n", test, Count1);
}
int main() {
	freopen("C.inp", "r", stdin);
	freopen("C.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int test = 0; test < t; test ++) process(test + 1);
	return 0;
}
