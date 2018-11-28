#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>

using namespace std;

#define Eo(x) { cerr << #x << " = " << x << endl; }

typedef long long int64;
typedef double real;

#define inf 0x3f3f3f3f
#define maxn (1 << 7)
#define maxk (1 << 4)
#define P 10009

char buf[1 << 20];

string poly;
int k, n;

string wrd[maxn];
int ind[maxk], d, cnt[26] = {0};

int calc() {
	int i, j, ans = 0;
	int cur = 1;
	for(i = 0; i < poly.length(); i++) {
		if(poly[i] == '+') {
			ans = (ans+cur) % P;
			cur = 1;
		} else
			cur = (cur * cnt[poly[i]-'a']) % P;
	}
	ans = (ans+cur) % P;
	//Eo(ans);
	return ans;
}

int go(int i) {
	if(i == 0)
		return calc();
	int ans = 0;
	for(int j = 0; j < n; j++) {
		for(int k = 0; k < wrd[j].length(); k++)
			cnt[wrd[j][k]-'a']++;
		ans = (ans + go(i-1)) % P;
		for(int k = 0; k < wrd[j].length(); k++)
			cnt[wrd[j][k]-'a']--;
	}
	return ans;
}

int main() {
	int t = 1, tc;
	for(scanf("%d", &tc); t <= tc; t++) {
		printf("Case #%d:", t);
		gets(buf);
		gets(buf);
		stringstream ss(buf);
		ss >> poly >> k;
		scanf("%d", &n);
		for(int i = 0; i < n; i++) {
			scanf(" %s", buf);
			wrd[i] = buf;
			Eo(wrd[i]);
		}
		Eo(t);
		for(d = 1; d <= k; d++)
			printf(" %d", go(d));
		puts("");
		fflush(stdout);
	}
	return 0;
}
