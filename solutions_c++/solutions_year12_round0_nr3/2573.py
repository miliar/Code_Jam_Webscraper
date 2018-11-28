#include <cstdio>
#include <cstdlib>
#include <ctype.h>
#include <deque>
#include <set>
using namespace std;

int t, T, a, b, i, nrc, rez;
int p10[10];
set<int> s;

int nrcifre(int n) {
	int nr = 0;
	if(n == 0) return 1;
	while(n) {
		n /= 10;
		nr++;
	}
	return nr;
}

void rot(int &n) {
	int aux = n % 10;
	n = (n / 10) + aux * p10[nrc - 1];
}

int main() {
	freopen("c.in", "r", stdin);
	freopen("c.out","w", stdout);
	
	p10[0] = 1;
	for(i = 1; i < 9; i++)
		p10[i] = p10[i - 1] * 10;
	
	scanf("%d", &T);
	
	for(t = 1; t <= T; t++) {
		scanf("%d %d", &a, &b);
		
		nrc = nrcifre(a);
		rez = 0;
		for(i = a; i <= b; i++) {
			s.clear();
			int v = i;
			for(int d = 0; d < nrc - 1; d++) {
				rot(v);
				if(i < v && a <= v && v <= b) s.insert(v);
			}
			rez += (int)s.size();
		}
		
		printf("Case #%d: %d\n", t, rez);
	}
	
	return 0;
}
