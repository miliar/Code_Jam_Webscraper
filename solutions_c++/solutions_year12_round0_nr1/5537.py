#include <cstdio>
#include <iostream>
#include <cctype>
#include <cstring>
using namespace std;
int fim[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char st[100];
int main(void) {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int n; scanf("%d\n", &n);
	for (int i = 1; i <= n; i++) {
		printf("Case #%d: ", i);
		scanf("%[a-z ]\n", st);
		for (int i = 0; i < (int)strlen(st); i++) 
			if (st[i] == ' ') putchar(' '); else putchar(fim[st[i] - 'a']);
		puts("");
	}
	return 0;
}

