#include<iostream>
#include<cstring>
using namespace std;

int a[26][26], c[100 + 10];
bool b[26][26];
char s[100 + 10];
int n, m, C, D, p;

void solve()
{	
	memset(a, 0xff, sizeof(a));
	memset(b, 0, sizeof(b));
	scanf("%d", &C);	
	for (int i = 0; i < C; i++) {
		scanf("%s", s);
		a[s[0] - 'A'][s[1] - 'A'] = s[2] - 'A';
		a[s[1] - 'A'][s[0] - 'A'] = s[2] - 'A';				
	}
	scanf("%d", &D);
	for (int i = 0; i < D; i++) {
		scanf("%s", s);
		b[s[0] - 'A'][s[1] - 'A'] = b[s[1] - 'A'][s[0] - 'A'] = true;
	}
	scanf("%d %s\n", &n, s);
	p = 0;
	for (int i = 0; i < n; i++) {
		int cur = s[i] - 'A';
		if (p > 0 && a[cur][c[p - 1]] >= 0)
			c[p - 1] = a[cur][c[p - 1]];
		else {
			c[p++] = cur;	
			if (p >= 2) {
				bool flag = false;
				for (int j = 0; j + 1< p; j++)
					flag = flag || b[c[j]][c[p - 1]];
				if (flag) p = 0;
			}
		}					
	}
	printf("[");
	for (int i = 0; i < p; i++) {
		if (i > 0) printf(", ");
		printf("%c", char(c[i] + 'A'));
	}
	printf("]\n");
}
 
int main()
{
	int T, t;
	for (scanf("%d\n", &T), t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		solve();
	}
}
