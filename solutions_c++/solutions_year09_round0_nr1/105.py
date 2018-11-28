#include <iostream>
#include <cstring>

using namespace std;

int L, D, N;
bool okay[20][30];
char word[5050][20];
char pattern[1000];

void input () {
	scanf ("%d%d%d", &L, &D, &N);
	for (int i=0;i<D;i++)
		scanf ("%s", &word[i]);
}

void solve () {
	int num, len, pos, good;
	for (int i=1;i<=N;i++) {
		memset (okay, 0, sizeof(okay));
		num = 0;
		scanf ("%s", &pattern);
		len = strlen(pattern);
		pos = 0;
		for (int j=0;j<len;j++) {
			if (pattern[j]=='(') {
				j++;
				while (pattern[j]!=')') {
					okay[pos][pattern[j]-'a'] = true;
					j++;
				}
			}
			else
				okay[pos][pattern[j]-'a'] = true;
			pos++;
		}
		for (int j=0;j<D;j++) {
			good = 1;
			for (int k=0;k<L;k++)
				if (!okay[k][word[j][k]-'a']) {
					good = 0;
					break;
				}
			num += good;
		}
		printf ("Case #%d: %d\n", i, num);
	}
}

void output () {

}

int main () {
	freopen ("prog.in", "r", stdin);
	freopen ("prog.out", "w", stdout);
	input ();
	solve ();
	output ();
	return 0;
}
