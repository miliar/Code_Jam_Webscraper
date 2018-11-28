#include <stdio.h>
#include <iostream>

using namespace std;

int t, test, sol, sol2, lastPos[2], last[2], nr, n, sol3;
char ch;
int a[110], b[110];
int s[110];


void write();

void read() {

	freopen("bottrust.in", "r", stdin);
	freopen("bottrust.out", "w", stdout);

	scanf("%d ", &t);

}


void solve() {

	for (test = 1; test <=t; ++test) {

		scanf("%d ", &n);
		for (int i=0; i<n; ++i) {
			scanf("%c %d ", &ch, &nr);
			a[i] = (ch == 'O' ? 1 : 0);
			b[i] = nr;
		}

		//lastPos = 1;
		//last = 0;
		//sol = 0;
		s[0] = b[0];
		lastPos[a[0]] = b[0];
		last[a[0]] = 0;
		lastPos[!a[0]] = 1;
		last[!a[0]] = -1;
		for (int i=1; i<n; ++i) {
			//if (a[i] == 0) {
				s[i] = s[i-1] + (abs(b[i] - lastPos[a[i]]) <= (s[i-1] - (last[a[i]] >=0 ? s[last[a[i]]] : 0)) 
									? 1 : abs(b[i]-lastPos[a[i]])-(s[i-1]-(last[a[i]] >=0 ? s[last[a[i]]] : 0))+1);
				last[a[i]] = i;
				lastPos[a[i]] = b[i];
			//} else {
				
			//}
		}

	/*	lastPos = 1;
		last = 0;
		sol2 = 0;
		for (int i=0; i<n; ++i) {
			if (a[i] == 1) {
				sol2 += abs(b[i] - lastPos) + (i-last-1);
				last = i;
				lastPos = b[i];
			}
		}
*/
		//sol3 = (sol > sol2 ? sol : sol2) + n;
		sol3 = s[n-1];
		write();
	}

}


void write() {

	

	printf("Case #%d: %d\n", test, sol3);

}

int main() {

	read();
	solve();

	fclose(stdin);
	fclose(stdout);

	return 0;
}

