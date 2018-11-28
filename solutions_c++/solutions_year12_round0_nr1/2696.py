
#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
using namespace std;

char dict[] = "yhesocvxduiglbkrztnwjpfmaq";

int main() {
	int n;
	scanf("%d\n", &n);
	string str;
	for (int i = 0; i < n; i++) {
		getline(cin, str);
		printf("Case #%d: ", i + 1);
		for (int j = 0; j < (int)str.size(); j++) {
			if (str[j] >= 'a' && str[j] <= 'z')
				printf("%c", dict[str[j] - 'a']);
			else printf("%c", str[j]);
		}
		printf("\n");
	}
}