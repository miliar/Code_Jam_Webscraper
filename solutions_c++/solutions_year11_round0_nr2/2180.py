#include <iostream>
#include <string>
#include <queue>

using namespace std;

int sp;
char form[255][255], a[105];
bool opposed[255][255];

bool cleared(char c) {
	for(int i = 0; i < sp; ++i)
		if (opposed[c][a[i]]) {
			sp = 0;
			return true;
		}
	return false;
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int tk;
    scanf("%d\n", &tk);

    for (int tc = 1; tc <= tk; ++tc) {
    	printf("Case #%d: ", tc);

    	memset(form, 0, sizeof form);
    	memset(opposed, false, sizeof opposed);

    	int n;
    	string s;
    	cin >> n;
    	while (n --> 0) {
    		cin >> s;
    		form[s[0]][s[1]] = form[s[1]][s[0]] = s[2];
    	}

    	cin >> n;
    	while (n --> 0) {
    		cin >> s;
    		opposed[s[0]][s[1]] = opposed[s[1]][s[0]] = true;
    	}

    	sp = 0;
    	cin >> n >> s;

    	for(size_t i = 0; i < s.length(); ++i) {
    		char c = s[i];
    		while (sp > 0 && form[c][a[sp - 1]]) {
    			c = form[c][a[sp - 1]];
    			--sp;
    		}

    		if (!cleared(c)) {
    			a[sp++] = c;
    		}
    	}

    	printf("[");
    	for (int i = 0; i < sp; ++i) {
    		if (i) printf(", ");
    		printf("%c", a[i]);
    	}
    	printf("]\n");

    }
	
	return 0;
}