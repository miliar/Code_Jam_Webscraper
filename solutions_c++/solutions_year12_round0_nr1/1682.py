#include <iostream>
#include <cstdlib>
#include <cstdio>
using namespace std;
char a[] = "yhesocvxduiglbkrztnwjpfmaq";
string s;
int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int test;
	scanf("%d\n", &test);
	for (int i = 1; i <= test; ++i) {
		getline(cin,s);
		printf("Case #%d: ", i);
		for (int j = 0 ; j < s.size(); ++j) 
		if (s[j] == ' ') printf(" ");
		else printf("%c", a[s[j] - 'a']);
		printf("\n");
	}
	return 0;
}