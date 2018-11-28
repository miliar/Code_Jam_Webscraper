#include <cstdio>
#include <string>

using namespace std;

const int h = 333;

int a[h];
char w[h];

int main() {
	string s = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	s += " rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	s += " de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string r = "our language is impossible to understand";
	r += " there are twenty six factorial possibilities";
	r += " so it is okay if you want to just give up";
	a['y'] = 'a'; a['e'] = 'o'; a['q'] = 'z'; // The hint
	a['z'] = 'q'; // The hardest part
	for (int i = 0; i < s.length(); i++)
		a[s[i]] = r[i];
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int tests;
	scanf("%d", &tests);
	gets(w);
	for (int test = 0; test < tests; test++) {
		gets(w);
		for (int i = 0; w[i]; i++)
			w[i] = a[w[i]];
		printf("Case #%d: ", test+1);
		puts(w);
	}
	return 0;
}