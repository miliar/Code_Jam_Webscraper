#include <cstdio>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <iostream>
#include <cmath>
using namespace std;

char mp[27] = "yhesocvxduiglbkrztnwjpfmaq";
char in[10000], out[10000];

int main() {
	int test;
	scanf("%d ", &test);
	for (int cas = 1; cas <= test; ++cas) {
		gets(in);
		printf("Case #%d: ", cas);
		for (int i = 0; in[i]; ++i)
			if (isspace(in[i])) putchar(in[i]);
			else putchar(mp[in[i] - 'a']);
		puts("");
	}
	return 0;
}
