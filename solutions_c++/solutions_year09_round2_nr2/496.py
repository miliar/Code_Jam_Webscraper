#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int T, num;
char li[50], nxt[50];

void input () {
	gets (li);
}

void solve () {
	int len = strlen (li);
	for (int i=0;i<=len;i++)
		nxt[i] = li[i];
	if (!next_permutation(nxt, nxt+len)) {
		char mi = '9';
		int mp = -1;
		for (int i=0;i<len;i++)
			if (nxt[i]<=mi&&nxt[i]!='0')
				mi = nxt[i], mp = i;
		swap (nxt[0], nxt[mp]);
		sort (nxt+1, nxt+len);
		for (int i=len+1;i>=2;i--)
			nxt[i] = nxt[i-1];
		nxt[1] = '0';
	}
}

void output () {
	printf ("Case #%d: %s\n", num, nxt);
}

int main () {
	freopen ("prog.in", "r", stdin);
	freopen ("prog.out", "w", stdout);
	scanf ("%d", &T);
	gets (li), num = 1;
	while (num<=T) {
		input ();
		solve ();
		output ();
		num++;
	}
	return 0;
}
