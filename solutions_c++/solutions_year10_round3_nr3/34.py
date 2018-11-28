#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define N 520

int ans[N];
int anscount;

char table[N][N];
int n, m;

char *t[]={
"0000",//0
"0001",//1
"0010",//2
"0011",
"0100",//4
"0101",
"0110",//6
"0111",
"1000",//8
"1001",
"1010",//10
"1011",
"1100",//12
"1101",
"1110",
"1111"//15
};

void insert(char *str, int idx)
{
	int i;
	int v;
	int len = strlen(str);
	for(i = 0; i < len; i++) {
		if(str[i] >= '0' && str[i] <= '9') v = str[i] - '0';
		else v = str[i] - 'A' + 10;
		strcat(table[idx], t[v]);
	}
}

int check(int fri, int frj, int len)
{
	int i, j;
	char pre;
	if(fri + len > m || frj + len > n) return 0;
	pre = table[fri][frj];
	if(pre == '2') return 0;
	for(j = frj + 1; j < frj + len; j++) {
		if(pre == table[fri][j] || table[fri][j] == '2') return 0;
		pre = table[fri][j];
	}
	pre = table[fri][frj];
	for(i = fri + 1; i < fri + len; i++) {
		if(pre == table[i][frj] || table[i][frj] == '2') return 0;
		pre = table[i][frj];
	}
	for(i = fri + 1; i < fri + len; i++) {
		pre = table[i][frj];
		if(pre == '2') return 0;
		for(j = frj + 1; j < frj + len; j++) {
			if(pre == table[i][j] || table[i][j]=='2')return 0;
			pre = table[i][j];
		}
	}
	ans[len]++;
	for(i = fri; i < fri + len; i++) {
		for(j = frj; j < frj + len; j++)table[i][j] = '2';
	}
}

void smallsearch(int len)
{
	int i, j;
	for(i = 0; i < m; i++) {
		for(j = 0; j < n; j++)
			check(i, j, len);
	}
}

void sovlesmall()
{
	int maxv;
	int i;
	memset(&ans, 0, sizeof(ans));
	maxv = m > n ? n : m;
	for(i = maxv; i > 0; i--) {
		smallsearch(i);
	}
}

void solvebig()
{
	;
}

int main()
{
	int t;
	int i, j, k;
	char str[N];
	int minv;
	freopen("in","r",stdin);freopen("out","w",stdout);

	scanf("%d", &t);
	for(i = 1; i <= t; i++) {
		memset(&table, 0, sizeof(table));
		scanf("%d %d", &m, &n);
		for(j = 0; j < m; j++) {
			scanf("%s", &str);
			insert(str, j);
		}
//		for(j  = 0; j < m; j++)printf("%s\n", table[j]);
		sovlesmall();
		anscount = 0; 
		minv = n > m ? m : n;
		for(j = minv; j >= 1; j--)if(ans[j])anscount++;
		printf("Case #%d: %d\n", i, anscount);
		for(j = minv; j>= 1; j--)if(ans[j])printf("%d %d\n", j, ans[j]);
	}
	return 0;
}