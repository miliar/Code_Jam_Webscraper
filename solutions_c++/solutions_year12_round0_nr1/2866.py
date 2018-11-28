#include <iostream>
#include <cstdio>
#include <string.h>
#include <string>
#include <algorithm>
using namespace std;

string a[3] = {
"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"};
string b[3] = {
"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"};

const int maxL = 1001;
char s[maxL];
int t[256];

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	memset(t, 0, sizeof(t));
	for (int c = 0; c != 3; c++)
		for (int i = 0; i != a[c].length(); i++)
			t[a[c][i]] = b[c][i];
	t['z'] = 'q';
	t['q'] = 'z';
	int TextN, TT = 0;
	scanf("%d", &TextN);
	getchar();
	while (TextN--) {
		gets(s);
		printf("Case #%d: ", ++TT);
		for (int i = 0; i != strlen(s); i++)
			printf("%c", t[s[i]]);
		printf("\n");
	}
	return 0;
}