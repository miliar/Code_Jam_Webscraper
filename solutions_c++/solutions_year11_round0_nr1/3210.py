#include <cstdio>
#include <vector>

#define MAXN 110

using namespace std;

vector <int> G, V;
int T, N, button[MAXN];
char col[MAXN];

inline int abs (int x) {
	if (x < 0) return -x;
	return x;
}
int main ()
{


	freopen ("bot.in", "r", stdin);
	freopen ("bot.out", "w", stdout);

	scanf ("%d", &T);
	
	G.resize (110);
	V.resize (110);

	for (int tests = 1; tests <= T; tests++) {
		scanf ("%d ", &N);
		
		int t = 0, tmp, Or, Bl, IOr, IBl;
		int i;
		G.clear ();
		V.clear ();
		for (i = 1; i <= N; i++) {
			scanf ("%c %d ", &col[i], &button[i]);
			if (col[i] == 'O') G.push_back (button[i]);
			if (col[i] == 'B') V.push_back (button[i]);
		}
		scanf ("\n");
		Or = 1; Bl = 1;
		IOr = 0; IBl = 0;
		
		t = 0;
		for (i = 1; i <= N; i++) {
			if (col[i] == 'O') {
				tmp = abs (button[i] - Or) + 1;
				Or = button[i];

				if (Bl < V[IBl])
					Bl = min (Bl + tmp, V[IBl]);
				if (Bl > V[IBl])
					Bl = max (Bl - tmp, V[IBl]);
				t += tmp;
				++IOr;
			}
			if (col[i] == 'B') {
				tmp = abs (button[i] - Bl) + 1;
				Bl = button[i];
				
				if (Or < G[IOr])
					Or = min (Or + tmp, G[IOr]);
				if (Or > G[IOr])
					Or = max (Or - tmp, G[IOr]);
				t += tmp;
				++IBl;
			}
//			printf ("%d %c\n", t, col[i]);
		}
		printf ("Case #%d: %d\n", tests, t);
	//	return 0;
	}
	return 0;
}
							
