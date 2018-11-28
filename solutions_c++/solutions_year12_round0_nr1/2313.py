#include <cstdio>
#include <cstring>
#include <cctype>

const char mp[] = "yhesocvxduiglbkrztnwjpfmaq";

int main() {
	int testCases;
	char word[128];
	fgets(word, 128, stdin);
	sscanf(word, "%d", &testCases);
	for (int t = 1; t <= testCases; ++ t) {
		fgets(word, 128, stdin);
		word[strlen(word) - 1] = '\0';
		for (size_t i = 0; i < strlen(word); ++ i) {
			word[i] = islower(word[i]) ? mp[word[i] - 'a'] : word[i];
		}
		printf("Case #%d: %s\n", t, word);
	}
	return 0;
}
