#include <cstdio>
#include <bitset>
#include <cstring>
#include <string>

#define MAXN 200
using namespace std;

char matC[MAXN][MAXN], S[MAXN], D[MAXN], s[MAXN];
bitset <MAXN> ok;
int A, i, T, j, C, d, N;
int main ()
{


	freopen ("magicka.in", "r", stdin);
	freopen ("magicka.out", "w", stdout);


	scanf ("%d\n", &T);

	for (int t = 1; t <= T; t++) {

		memset (matC, 0, sizeof (matC));
		memset (D, 0, sizeof (D));
		memset (S, 0, sizeof (S));
		ok.reset (); // clear ok
		A = 0;
		
		scanf ("%d", &C);

		for (i = 1; i <= C; i++) {
		       scanf ("%s", s);
		       matC[s[0]][s[1]] = matC[s[1]][s[0]] = s[2];
		}
		scanf ("%d", &d);
		for (i = 1; i <= d; i++) {
		       scanf ("%s", s);
		       D[s[0]] = s[1];
		       D[s[1]] = s[0];
	        }
		
		scanf ("%d", &N);
		scanf ("%s\n", s);
		
		int stk = 0;
		for (i = 0; i < N; i++) {
			
			if (matC[s[i]][S[stk]] != 0 && stk >= 1) {
				S[stk] = matC[s[i]][S[stk]];
			}

			else if (D[s[i]] != 0 && stk >= 1) {
				bool ok = 0;
				for (j = stk; j >= 1; j--)
					if (D[s[i]] == S[j]) {
						stk = 0;
						ok = 1;
						break;
					}
				if (!ok) S[++stk] = s[i];
			}
			else S[++stk] = s[i];
		}
		printf ("Case #%d: [", t);
		for (i = 1; i < stk; i++)
			printf ("%c, ", S[i]);
		if (stk) printf ("%c", S[stk]);
		printf ("]\n");
	}
	return 0;
}	
