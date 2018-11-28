#include <cstdio>
#include <cstdlib>
#include <algorithm>
#define MAX 1005

using namespace std;

int v[MAX];
int N;

int main(){
	int T;
	scanf ("%d", &T);
	for (int t = 1; t <= T; t++){
		scanf ("%d", &N);
		for (int i = 0; i < N; i++)
			scanf ("%d", &v[i]);
		int best = -1;
		for (int i = 1; i < (1<<N); i++){
			int s1, s2;
			int x1, x2;
			s1 = s2 = x1 = x2 = 0;
			for (int j = 0; j < N; j++){
				if (i & (1<<j)){
					x1 ^= v[j];
					s1 += v[j];
				}
				else{
					x2 ^= v[j];
					s2 += v[j];
				}
			}
			if (x1 == x2 && s1 > 0 && s2 > 0 && (s1 > best || s2 > best)){
				best = max(s1, s2);
			}
		}
		printf ("Case #%d: ", t);
		if (best == -1)
			printf ("NO\n");
		else
			printf ("%d\n", best);
	}
	return 0;
}
