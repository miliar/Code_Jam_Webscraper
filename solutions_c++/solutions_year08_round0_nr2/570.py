#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <cmath>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

struct train {
	int t;
	int out; 
}tmp;

int cases, h, m, na, nb, T;
char s[100];

bool comp(const train& a, const train& b) {
	if (a.t < b.t)
		return true;
	else if (a.t > b.t)
		return false;
	else return a.out < b.out;
}
int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	vector<train> A, B;
	scanf("%d", &cases);
	for (int cas = 1; cas <= cases; ++cas) {
		A.clear();
		B.clear();
		scanf("%d", &T);
		scanf("%d %d", &na, &nb);
		for (int i = 0; i < na; ++i) {
			scanf("%s", s);
			h = (s[0]-'0') * 10 + (s[1]-'0');
			m = (s[3]-'0') * 10 + (s[4]-'0');
			tmp.t = h * 60 + m;
			tmp.out = 1;
			A.push_back(tmp);

			scanf("%s",s);
			h = (s[0]-'0') * 10 + (s[1]-'0');
			m = (s[3]-'0') * 10 + (s[4]-'0');
			tmp.t = h * 60 + m + T;
			tmp.out = 0;
			B.push_back(tmp);
		}
		for (int i = 0; i < nb; ++i) {
			scanf("%s", s);
			h = (s[0]-'0') * 10 + (s[1]-'0');
			m = (s[3]-'0') * 10 + (s[4]-'0');
			tmp.t = h * 60 + m;
			tmp.out = 1;
			B.push_back(tmp);

			scanf("%s",s);
			h = (s[0]-'0') * 10 + (s[1]-'0');
			m = (s[3]-'0') * 10 + (s[4]-'0');
			tmp.t = h * 60 + m + T;
			tmp.out = 0;
			A.push_back(tmp);
		}
		sort(A.begin(), A.end(), comp);
		sort(B.begin(), B.end(), comp);
		int numa = 0, numb = 0, ansa = 0, ansb = 0;
		for (int i = 0; i < A.size(); ++i) {
			if (A[i].out == 0) numa++;
			else {
				if (numa > 0) numa--;
				else ansa++;
			}
		}
		for (int i = 0; i < B.size(); ++i) {
			if (B[i].out == 0) numb++;
			else {
				if (numb > 0) numb--;
				else ansb++;
			}
		}
		printf("Case #%d: %d %d\n", cas, ansa, ansb);
	}
	return 0;
}


