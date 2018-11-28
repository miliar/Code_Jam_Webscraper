#include <iostream>

using namespace std;

#define MAXD 5005
#define MAXN 505
#define MAXL 20

string dict[MAXD];
bool gal[MAXN][MAXL][30];
char buf[MAXD];
int l, d, n;

void read() {
	freopen("a-large.in", "r", stdin);
	scanf("%d %d %d", &l, &d, &n);
	for (int i = 0; i < d; i++) {
		scanf(" %s", &buf);
		dict[i] = buf;
	}
	for (int i = 0; i < n; i++) {
		scanf(" %s", &buf);
		int kel = -1;
		bool open = false;
		for (int j = 0; buf[j] != '\0'; j++) {
			if (buf[j] == '(') {
				open = true;
				kel++;
			}
			if (buf[j] == ')') open = false;
			if (buf[j] == '(' || buf[j] == ')') continue;
			if (!open) kel++;
			gal[i][kel][buf[j] - 'a'] = true;
		}
	}
}
		
void solve() {
	freopen("a-large.out", "w", stdout);
	for (int i = 1; i <= n; i++) {
		int kiek = 0;
		for (int j = 0; j < d; j++) {
			bool tinka = true;
			for (int z = 0; z < dict[j].size() && tinka; z++)
				if (!gal[i - 1][z][dict[j][z] - 'a']) tinka = false;
			kiek += tinka;
		}
		printf("Case #%d: %d\n", i, kiek);
	}
}		

int main() {
	read();
	solve();
	return 0;
}
