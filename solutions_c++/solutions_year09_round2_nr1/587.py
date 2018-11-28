#include <cstdio>
#include <string>
#include <iostream>
#define maxn 10100

using namespace std;

double arb[maxn], sol;
int q, tt, nra;
string ar[maxn];
int n, i, j, m;
string p[maxn], ss;


void get_tree(int nod, int left, int right) {
	int i, j, nrp;
	double nr = 0, sup = 1;
	string str;
	
	i = left + 3;
	while (ss[i] >= '0' && ss[i] <= '9') {
		nr = nr * 10 + (ss[i] - 48);
		sup *= 10;
		i++;
	}
	
	nr /= sup;
	arb[nod] = nr;
	
	if (i == right) {
		return;
		ar[nod] = "-1";
	}
	
	str.clear();
	while (ss[i] >= 'a' && ss[i] <= 'z') {
		str = str + ss[i];
		i++;
	}
	
	ar[nod] = str;
	
	nrp = 0;
	for (j = i; j <= right; j++) {
		if (ss[j] == '(')
			nrp++;
		if (ss[j] == ')')
			nrp--;
		if (nrp == 0) {
			get_tree(2 * nod, i, j);
			break;
		}
	}
	
	i = j + 1;
	nrp = 0;
	for (j = i; j <= right; j++) {
		if (ss[j] == '(')
			nrp++;
		if (ss[j] == ')')
			nrp--;
		if (nrp == 0) {
			get_tree(2 * nod + 1, i, j);
			break;
		}
	}
	
	
}

void read() {
	int i;
	char s[1000];
	
	ss.clear();
	memset(arb, 0, sizeof(arb));
	
	scanf("%d ", &m);
	for (i = 1; i <= m; i++) {
		fgets(s, 999, stdin);
		for (j = 0; s[j] != 0; j++)
			if (s[j] != ' ' && s[j] != '\n')
				ss += s[j];
		//ss = ss + s;
	}
	
	//cout<<ss;
	get_tree(1, 0, ss.size() - 1);
}

inline double probab() {
	int nod = 1, i, j;
	double psol = 1;
	double ok;
	
	while (arb[nod] > 0) {
		psol *= arb[nod];
		ok = false;
		if (ar[nod] == "-1")
			break;
		for (i = 1; i <= nra; i++)
			if (ar[nod] == p[i]) {
				ok = true;
				break;
			}
		if (ok)
			nod = nod * 2;
		else
			nod = nod * 2 + 1;
	}
	
	return psol;
}

void solve() {
	int i;
	scanf("%d", &n);
	for (i = 1; i <= n; i++) {
		cin>>ss>>nra;
		for (j = 1; j <= nra; j++)
			cin>>p[j];
		
		printf("%.7lf\n", probab());
	}
	
}

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	scanf("%d", &tt);
	for (q = 1; q <= tt; q++) {
		read();
		printf("Case #%d:\n", q);
		solve();
	}
	
	
	return 0;
}
