#include <cstdio>
#include <string>

using namespace std;
const int MAXN = 200;
const char tran [26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int t;
char s [MAXN];

int main () {
	freopen ("2012a.in", "r", stdin);
	freopen ("2012a.out", "w", stdout);
	
	scanf ("%d\n", &t);
	for (int c = 1; c <= t; ++c) {
		scanf ("%[^\n]\n", s);
		printf ("Case #%d: ", c);
		for (int i = 0; i < strlen (s); ++i) {
			char c = s [i];
			if (c != ' ') c = tran [c - 'a'];
			printf ("%c", c);
		}
		printf ("\n");
	}
	
	fclose (stdin);
	fclose (stdout);
	return 0;
}
