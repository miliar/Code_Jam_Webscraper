#include <iostream>
#include <stdio.h>
using namespace std;  

void solve(int);

int main() {
	int testCases;
	scanf("%d",&testCases);
	for(int i = 0; i <= testCases; ++i) {
		solve(i);
	}
	return 0;
}

void solve(int testCase) {
	int i;
	char g[101], s[101], translate[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	gets(g);
	if(testCase == 0) { return; }
	for(i = 0; i < 101; ++i) {
		if(g[i] == '\0') { break; }
		if(g[i] == ' ') {
			s[i] = ' ';
		} else {
			s[i] = translate[g[i]-'a'];
		}
	}
	s[i] = '\0';
	printf("Case #%d: %s\n", testCase, s);
}