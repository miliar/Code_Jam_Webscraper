#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<algorithm>

using namespace std;

void submit() {
	freopen("D:\\Codejam\\problem\\problem\\input.in", "r", stdin);
    freopen("D:\\Codejam\\problem\\problem\\output.out", "w", stdout);
}

//code here

char buf[100];
typedef long long ll;

int main() {
	submit();
	int T;
	scanf("%d", &T);
	for (int tid=1; tid<=T; ++tid) {
		scanf("%s", buf);
		int len = strlen(buf);
		map<char, int> dic;
		dic[buf[0]] = 1;
		int start = 0;
		for (int i=1; i<len; ++i) {
			if (!dic.count(buf[i]) ) {
				dic[buf[i]] = start++;
				if (start == 1) start++;
			}
		}
		int base = 2;
		if (start > 2) base = start;
		
		ll res = 0;
		for (int i=0; i<len; ++i) {
			res = res * base + dic[buf[i]];
		}

		printf("Case #%d: %lld\n", tid, res);
	}
	return 0;
}