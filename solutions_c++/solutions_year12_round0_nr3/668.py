/*
 * Author: Fish@UESTC_Oblivion
 * Created Time:  2012/04/14 09:31:52
 * Project: 
 *    Type: 
 */
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;

const int MaxN = 10000000;

int ch[MaxN][10], cur;
int DP[MaxN];
long long ret;
char temp[20];

void get_sub_string(char* s, int n) {
	int ret, i = 0, j = 1, k = 0;
	int tmp;

	while (i < n && j < n && k < n) {
		tmp = s[i + k] - s[j + k];
		if (tmp == 0)
			k++;
		else {
			if (tmp > 0)
				i += k + 1;
			else
				j += k + 1;
			if (i == j)
				j++;
			k = 0;
		}
	}

	ret = min(i, j);
	s[ret + n] = 0;
	strcpy(temp, s + ret);
}

void insert(const char* s) {
	int idx, p = 0;
	
	while (*s) {
		idx = *s++ - '0';
		if (ch[p][idx] == 0) ch[p][idx] = cur++;
		p = ch[p][idx];
	}
	
	ret += DP[p];
	DP[p]++;
}

void sol(int x) {
	char buf[20];
	int N;
	
	sprintf(buf, "%d", x);
	N = strlen(buf);
	for (int i = 0; i < N; i++)
		buf[i + N] = buf[i];
	
	get_sub_string(buf, N);
	insert(temp);
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, cas = 1;
	int L, R;
	
	scanf("%d", &T);
	while (T--) {
		scanf("%d%d", &L, &R);
		memset(ch, 0, sizeof(ch));
		memset(DP, 0, sizeof(DP));
		cur = 1;
		ret = 0;
		for (int i = L; i <= R; i++)
			sol(i);
		printf("Case #%d: %I64d\n", cas++, ret);
	}
	
	return 0;
}
