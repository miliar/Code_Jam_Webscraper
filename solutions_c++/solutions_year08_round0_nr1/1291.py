
#include <stdio.h>
#include <string>

using namespace std;

int prob, N, S, Q;
string name[100], search[1000];
int nameh[100], searchh[1000];
int v[1000];
int f[110];


int hash(const string &s) {
	int num = 0;
	for (int i = 0; i < s.length(); i++) {
		num = (num << 4) + s[i];
		int g = num & 0xF0000000;
		num = (num ^ (g >> 24)) & ~g;
	}
	return num;
}

int main() {
//	freopen("a.in", "r", stdin);
//	freopen("a.out", "w", stdout);

	scanf("%d ", &N);
	while(N--) {
		char buf[110];

		scanf("%d\n", &S);
		for (int i = 0; i < S; i++) {
			gets(buf); name[i] = buf; nameh[i] = hash(name[i]);
		}

		scanf("%d\n", &Q);
		for (int i = 0; i < Q; i++) {
			gets(buf); search[i] = buf; searchh[i] = hash(search[i]);
		}

		if (Q == 0) {
			printf("Case #%d: 0\n", ++prob);
			continue;
		}

		for (int i = 0; i <	Q; i++) {
			for (int j = 0; j < S; j++)
				if (searchh[i] == nameh[j] && search[i] == name[j]) {
					v[i] = j; break;
				}
		}

		for (int i = 0; i < S; i++) f[i] = 0;

		int p = 0, k;
		for (int i = 0; i < Q; ) {
			p++; k = 0;
			int i1;
			for (i1 = i; i1 < Q; i1++) {
				if (f[v[i1]] != p) {
					f[v[i1]] = p; k++;
					if (k == S) break;
				}
			}
			i = i1;
		}

		printf("Case #%d: %d\n", ++prob, p-1);
	}

	return 0;
}

