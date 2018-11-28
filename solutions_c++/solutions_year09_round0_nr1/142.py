#include <cstdio>
#include <set>
#include <string>

using namespace std;

set<string> dictionary, words, er;
set<char> letter[15];
int l, d, n;

int process() {
	words.clear();
	words = dictionary;
	
	int i = 0;
	while (i < l) {
		letter[i].clear();
		char c = getchar();
		if (c == '(')
			while (true) {
				c = getchar();
				if (c == ')')
					break;
				letter[i].insert(c);
			}
		else
			letter[i].insert(c);
		i++;
	}
	
	i = 0;
	while (!words.empty() && i < l) {
		set<string>::iterator it;
		er.clear();
		for (it = words.begin(); it != words.end(); it++) {
			if (letter[i].find( (*it)[i] ) == letter[i].end()) {
				er.insert(*it);
			}
		}
		for (it = er.begin(); it != er.end(); it++)
			words.erase(*it);
		i++;
	}
	
	while (getchar() != '\n');
	
	return words.size();
}

int main() {
	char w[16];

	scanf("%d %d %d", &l, &d, &n);
	for (int i = 0; i < d; i++) {
		scanf("%s\n", w);
		dictionary.insert(w);
	}
	
	for (int i = 1; i <= n; i++) {
		printf("Case #%d: %d\n", i, process());
	}
	
	return 0;
}

