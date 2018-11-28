/* 
 * SOUR:
 * ALGO:
 * DATE: Sun, 13 Sep 2009 00:01:20 +0800
 * COMM:
 * */
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;
typedef long long LL;
const int maxint = 0x7fffffff;
const long long max64 = 0x7fffffffffffffffll;

char s[31];
int main()
{
	int i,j,k,C;
	scanf("%d\n",&C);
	for(int c = 1;c <= C;c++) {
		fgets(s+1,30,stdin);
		int n = strlen(s+1) - 1;
		s[0] = '0';
		s[++n] = 0;
		next_permutation(s,s+ n);
		printf("Case #%d: ",c);
		if(s[0] != '0')
			putchar(s[0]);
		for(i = 1;i < n;i++) {
			putchar(s[i]);
		}
		putchar(10);
	}
	return 0;
}

