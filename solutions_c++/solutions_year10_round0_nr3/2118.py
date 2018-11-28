#include <cstdio>
#include <vector>

#define input "C-small-attempt0.in"
#define output "C.out"
using namespace std;

int main()
{
	int i, j, m, t, r, k, n, l = 0;
	int ans;

	FILE *fin = fopen(input, "r");
	FILE *fout = fopen(output, "w");

	fscanf(fin, "%d", &t);
	while (t--) {
		fscanf(fin, "%d %d %d", &r, &k, &n);
		vector<int> g(n), tg;
		for (i = 0; i < n; i++) fscanf(fin, "%d", &g[i]);
		ans = 0;
		for (i = 0; i < r; i++) {
			tg = g;
			for (j = k, m = 0; m < n; m++) {
				j -= g[m]; 
				if (j >= 0) {
					ans += g[m];
					tg.push_back(tg[0]); tg.erase(tg.begin());	
				}
				else break;
			}
			g = tg;
		}
		fprintf(fout, "Case #%d: %d\n", ++l, ans);  
	}

	fclose(fout);
	fclose(fin);

	return 0;
}