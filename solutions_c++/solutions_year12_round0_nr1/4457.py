#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

#pragma comment(linker, "/STACK:16000000")

typedef long long ll;
typedef pair<int, int> pii;

const int INF = 1e9;
const double EPS = 1e-8;
const double PI = 2 * acos(0.);

char t[] = "yhesocvxduiglbkrztnwjpfmaq";
char s[200];

int main() {
#ifdef _DBG1
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int n;
	scanf("%d", &n);
	gets(s);
	for (int i = 0; i < n; ++i) {
		gets(s);
		printf("Case #%d: ", i + 1);
		for (int j = 0; s[j] != 0; ++j) {
			if (s[j] >= 'a' && s[j] <= 'z')
				printf("%c", t[s[j] - 'a']);
			else
				printf("%c", s[j]);
		}
		printf("\n");
	}
	return 0;
}

