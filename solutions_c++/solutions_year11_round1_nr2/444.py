/*
 * =========================================================
 *       Filename:  B.cpp
 *    Description:  
 *        Created:  2011/5/21 9:45:50
 *         Author:  rocket323
 * =========================================================
 */
#include <stdio.h>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
#define maxl 10010

char word[maxl][100], ord[maxl];
int ans[maxl];
int len[maxl], list[maxl], top, n, m, cnt[30];

bool check(int c, int a, int b) {
	if(len[a] != len[b]) return 0;
	char x = 'a' + c;
	for(int i=0; word[a][i] && word[b][i]; ++i) {
		if((word[a][i] == x && word[b][i] != x) || (word[a][i] != x && word[b][i] == x)) return 0;
	}
	return 1;
}

bool check2(int c, int a, int b) {
	if(len[a] != len[b]) return 0;
	char x = 'a' + c;
	for(int i=0; word[a][i]; ++i) {
		if(word[a][i] == x) return 0;
	}
	return 1;
}

int calc(int x) {
	int ans = 0;
	memset(cnt, 0, sizeof cnt);

	top = 0;
	for(int i=0; i<n; ++i) {
		if(len[i] != len[x]) continue;
		for(int j=0; word[i][j]; ++j)
			cnt[word[i][j] - 'a']++;
		list[top++] = i;
	}

	for(int i=0; ord[i]; ++i) {
		if(x == 1) {
			//printf("here %c ", ord[i]);
			//for(int j=0; j<top; ++j) printf("%d ", list[j]);
			//printf("%d \n", ans);
			//puts("");
			//for(int j=0; j<26; ++j) printf("%d ", cnt[j]);
			//puts("");
		}
		//if(top < 2) break;

		int flag = 0;
		int c = ord[i] - 'a';
		if(cnt[c] <= 0) continue;

		for(int j=0; word[x][j]; ++j) if(word[x][j] - 'a' == c) flag = 1;
		if(!flag) {
			ans++;
			for(int j=0; j<top; ++j) {
				if(!check2(c, list[j], x)) {

					for(int k=0; word[list[j]][k]; ++k) cnt[word[list[j]][k] - 'a']--;

					list[j] = list[--top];
					--j;
				}
			}
		}
		else {
			for(int j=0; j<top; ++j) {
				if(!check(c, x, list[j])) {

					for(int k=0; word[list[j]][k]; ++k) cnt[word[list[j]][k] - 'a']--;

					list[j] = list[--top];
					--j;
				}
			}
		}
	}
	return ans;
}

int main() {
	int t;
	scanf("%d", &t);
	for(int q=1; q<=t; ++q) {
		scanf("%d%d", &n, &m);
		for(int i=0; i<n; ++i) {
			scanf("%s", word[i]);
			len[i] = strlen(word[i]);
		}
		for(int x=0; x<m; ++x) {
			scanf("%s", ord);

			int idx = -1, point = -1;
			for(int i=0; i<n; ++i) {
				int k = calc(i);
				if(k > point) {
					point = k;
					idx = i;
				}
				//printf("%d %d\n", i, k);
			}
			//printf("%d %d %d\n", x, idx, point);
			ans[x] = idx;
		}
		printf("Case #%d:", q);
		for(int i=0; i<m; ++i) printf(" %s", word[ans[i]]);
		puts("");
	}
	return 0;
}

