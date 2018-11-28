/* 
 * SOUR:gcj Qulification A
 * ALGO:search
 * DATE: 2009年 09月 03日 星期四 07:40:55 CST
 * COMM:
 * */
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<map>
#include<algorithm>
using namespace std;
const int maxint = 0x7fffffff;
const long long max64 = 0x7fffffffffffffffll;
#define debug 1
const int N = 800;
char dict[N*N][N];
int n, res;
int len[N];
int choice[N][N];

char s[N];
bool search(int idx)
{
	int i,j;
	for(i = 0;i < n;i++) {
		/*
		bool flag = false;
		for(j = 0;j < len[i];j++) {
			if(choice[i][j] == dict[idx][i]) {
				flag = true;
				break;
			}
		}
		if(flag == false)
			return false;
		*/
		if(!binary_search(choice[i],choice[i] + len[i],dict[idx][i])) {
			return false;
		}
	}
	return true;
}

int main()
{
	int i, j, k, m, C;
	scanf("%d%d%d", &n, &m, &C);
	for (i = 0; i < m; i++) {
		scanf("%s", dict[i]);
	}

	for (int c = 1; c <= C; c++) {
		scanf("%s", s);
		int l = strlen(s);
		int cnt = 0;
		for (j = 0; j < l; j++) {
			if (s[j] == '(') {
				for (k = j + 1; s[k] != ')'; k++) {
					choice[cnt][k - j - 1] = s[k];
				}
				len[cnt] = k - j - 1;
				j = k;
			} else {
				choice[cnt][0] = s[j];
				len[cnt] = 1;
			}
			sort(choice[cnt],choice[cnt] + len[cnt]);
			cnt++;
		}
		/*
		   for(j = 0;j < n;j++) {
		   printf("len[%d]:%d\n",j,len[j]);
		   }
		   */
		res = 0;
		for(j = 0;j < m;j++) {
			if(search(j)) {
				res ++;
			}
		}
		printf("Case #%d: %d\n", c, res);
	}
	return 0;
}
