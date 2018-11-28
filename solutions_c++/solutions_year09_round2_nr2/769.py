#pragma comment(linker, "/STACK:100777216")
#include <stdio.h>
#include <string>
#include <iostream>
#include <string.h>
#include <algorithm>

using namespace std;
string s;
const int maxn = 30;
int a[maxn];
int t;

int main()
{
	freopen("input.txt" , "r" , stdin);
	freopen("output.txt" , "w" , stdout);
	scanf("%d\n" , &t);
	int st = 0;
	for (int k = 1; k <= t; k++)
	{
		cin >> s;
		memset(a, 0 , sizeof(a));
		for (int i = 0; i < s.length(); i++)
			a[1 + i] = s[i] - '0';
		next_permutation(a, a + s.length() + 1);
		if (a[0] == 0)
		   st = 1;
		else st = 0;
		printf("Case #%d: ", k);
		for (int i = st; i <= s.length(); i++)
			printf("%d", a[i]);
		printf("\n");
	}
	return 0;
}