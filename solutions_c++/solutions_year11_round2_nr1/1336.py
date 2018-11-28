#include <stdio.h>
#define N 400
struct Info
{	int op, w;
	double WP, OWP, OOWP;
};
int main()
{	freopen("large.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	struct Info info[N];
	char rel[N +1][N +1];
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int n;
		scanf("%d", &n);
		getchar();
		for (int i = 0; i < n; ++i) {
			info[i].w = info[i].op = 0;
			info[i].WP = info[i].OWP = info[i].OOWP = 0.0;
		}
		for (int i = 0; i < n; ++i)
			scanf("%s", rel[i]);
			
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j)
				if (rel[i][j] == '.')	continue;
				else {
					++info[i].op;
					if (rel[i][j] == '1')
						++info[i].w;
				}
		}
		for (int i = 0; i < n; ++i) {
			info[i].WP = double(info[i].w) / double(info[i].op);
			for (int j = 0;j < n; ++j)
				if (i == j)	continue;
				else {
					if (rel[i][j] == '.')	continue;
					if (rel[j][i] == '1')	info[i].OWP += (double(info[j].w - 1) / double(info[j].op -1));
					else					info[i].OWP += (double(info[j].w) / double(info[j].op -1));					
							 
				}		
			info[i].OWP /= double(info[i].op);
		}
		for (int i = 0; i < n; ++i) {	
				for (int j = 0; j < n; ++j)
					if (i == j)	continue;
					else {
						if (rel[i][j] == '.')	continue;
						else {
							info[i].OOWP += info[j].OWP;
						}	
					}
				info[i].OOWP /= double(info[i].op);
			}
		printf("Case #%d:\n", t);
		for (int i = 0; i < n; ++i)
			printf("%lf\n", 0.25 * info[i].WP + 0.50 * info[i].OWP + 0.25 * info[i].OOWP);
	}
	scanf(" ");
	return 0;
}
