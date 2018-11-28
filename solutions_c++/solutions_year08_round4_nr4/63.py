#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<map>
#include<iostream>
using namespace std;

int const oo = 2000000000;
int len;
map<int, int> memo[20][20];
int Solve(int head, int tail, int zt, int tot);
int totCases, k, ans;
int delta1[20][20], delta2[20][20];
char s[60000];
int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	scanf("%d", &totCases);
	for (int cases(0); cases != totCases; ++cases) {
		printf("Case #%d: ", cases + 1);
		for (int i(0); i < 20; ++i)
		    for (int j(0); j < 20; ++j) memo[i][j].clear();
		scanf("%d%s", &k, s);
		memset(delta1, 0, sizeof(delta1));
		memset(delta2, 0, sizeof(delta2));
		len = strlen(s);
		for (int i(0); i < k; ++i)
		    for (int j(0); j < k; ++j)
		        if (i != j) {
					int now = 0;
					while (now < len) {
						if (s[i + now] != s[j + now]) ++delta1[i][j];
						now += k;
					}
					
					now = 0;
					while (now + k < len) {
						if (s[j + now] == s[i + k + now]) ++delta2[i][j];
						now += k;
					}
				}
		ans = oo;
		for (int i(0); i < k; ++i)
		    for (int j(0); j < k; ++j)
		        if (i != j)
		        	ans <?= Solve(i, j, (1 << k) - 1, k);
		printf("%d\n", ans);
	}
}
int Solve(int head, int tail, int zt, int tot)
{
	if (memo[head][tail].find(zt) != memo[head][tail].end()) return memo[head][tail][zt];
	if (tot == 1) {
		memo[head][tail][zt] = len / k;
//		cout << head << " " << tail << " " << zt << endl;
		return len / k;
	}
	int tem = oo;
	for (int i(0); i < k; ++i)
	    if (zt & (1 << i))
	        if (i != tail && ((i != head && tot != 2) || (tot == 2 && i == head))) {
                if (tot == k) tem <?= Solve(head, i, zt - (1 << tail), tot - 1) + delta1[i][tail] - delta2[head][tail];
                else tem <?= Solve(head, i, zt - (1 << tail), tot - 1) + delta1[i][tail];
			}
	memo[head][tail][zt] = tem;
	return tem;
}
