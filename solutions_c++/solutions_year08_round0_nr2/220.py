#include <iostream>

using namespace std;

int test;

int na, nb, T;
int sa[100], fa[100], sb[100], fb[100];
int wa[100], wb[100];

char getCHAR() {
	char c = 0;
	while (!(c >= '0' && c <= '9')) c = getchar();
	return c;
}

int get() {
	int res = 60*(10*(getCHAR() - '0') + getCHAR() - '0') + 10*(getCHAR() - '0') + getCHAR() - '0';
	return res;
}

int finda(int t) {
	int res = -1;
	for (int i = 0; i < na; i++) if (wa[i] == 0 && sa[i] >= t) {
		if (res == -1 || sa[res] > sa[i]) res = i;
	}
	return res;
}

int findb(int t) {
	int res = -1;
	for (int i = 0; i < nb; i++) if (wb[i] == 0 && sb[i] >= t) {
		if (res == -1 || sb[res] > sb[i]) res = i;
	}
	return res;
}

void seta(int);
void setb(int);

void seta(int ta) {
	wa[ta] = 1;
	int t = T + fa[ta];
	int tb = findb(t);
	if (tb == -1) return;
	setb(tb);
}

void setb(int tb) {
	wb[tb] = 1;
	int t = T + fb[tb];
	int ta = finda(t);
	if (ta == -1) return;
	seta(ta);
}

void solve() {
	cin >> T >> na >> nb;
	for (int i = 0; i < na; i++) {
		sa[i] = get();
		fa[i] = get();
	}
	for (int i= 0; i < nb; i++) {
		sb[i] = get();
		fb[i] = get();
	}
	memset(wa, 0, sizeof(wa));
	memset(wb, 0, sizeof(wb));
	int ra = 0, rb = 0;
	while (true) {
		int ta = finda(0);
		int tb = findb(0);
		if (ta == -1 && tb == -1) break;
		if (ta == -1) {
			rb++; setb(tb); continue;
		}
		if (tb == -1 || sa[ta] <= sb[tb]) {
			ra++; 
			seta(ta);
		} else {
			rb++;
			setb(tb);
		}
	}
	cout << "Case #" << test << ": " << ra << ' ' << rb << endl; 
}

int main() {
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int N; cin >> N;
	for (test = 1; test <= N; test++) 
		solve();
	fclose(stdin);
	fclose(stdout);
	return 0;
}