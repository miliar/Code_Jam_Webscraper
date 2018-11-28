#include <cstdio>
#include <algorithm>
using namespace std;

int t, n, s, p, x, l, res, g[3];

int main(){
	l = 1;
	scanf ("%d", &t);
	while (t--){
		res = 0;
		scanf ("%d%d%d", &n, &s, &p);
		for (int i = 0; i < n; i++){
			scanf ("%d", &x);
			g[0] = x/3;
			g[1] = (x - g[0])/2;
			g[2] = x - g[0] - g[1];
			sort (g, g+3);
			reverse (g, g+3);
			//printf ("|%d %d %d|", g[0], g[1], g[2]);
			if (g[0] >= p)
				res++;
			else if (g[0] == p-1 && s > 0 && g[1]){
				res++;
				s--;
			}
			/*if (x > 0 && p <= x){
				if (x/3 >= p || (x/3 == p-1 && x%3))
					res++;
				else if ((x/3 == p-1 || x/3 == p-2 && x%3) && s > 0){
					res++;
					s--;
				}
			}*/
		}
		printf ("Case #%d: %d\n", l, res);
		l++;
	}
}
