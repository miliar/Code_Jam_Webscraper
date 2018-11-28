#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;
#define INF 0x7fffffff;
char s[100][100];
int last[100], a[100], n;

int solve(){
	for(int i = 1; i <= n; ++i)
		if(last[i] > a[i]) return -1;
	int total = 0;
	for(int i = 1; i <= n; ++i)
		for(int j = 1; j <= n; ++j){
			if(i == j) continue;
			if(j < i && a[j] > a[i]) ++total;
			else if(j > i && a[j] < a[i]) ++total;
		}
	return total;
}

int main(){
	int cases;
	freopen("D:\\A-small-attempt0.in", "r", stdin);
	freopen("D:\\out.txt", "w", stdout);
	scanf("%d", &cases);
	for(int case_t = 1; case_t <= cases; ++case_t){
		int res = INF;
		scanf("%d", &n);
		for(int i = 1; i <= n; ++i){
			scanf("%s", s[i] + 1);
			last[i] = 0;
			for(int j = 1; j <= n; ++j) if(s[i][j] == '1') last[i] = j;
		}
		for(int i = 1; i <= n; ++i) a[i] = i;
		do{
			int t = solve();
			if(t >= 0 && t <= res) res = t;
		}while(next_permutation(a + 1, a + 1 + n));
		printf("Case #%d: %d\n", case_t, res / 2);
	}
	return 0;
}