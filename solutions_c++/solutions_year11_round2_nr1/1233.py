#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <queue>
#include <string>
#include <map>

using namespace std;


char grid[200][200];

long double WP[200][2], WPR[200], OWP[200], OOWP[200];

int main(){

	int casos, caso = 1;
	int n;
	double q, p;
	scanf("%d", &casos);
	while(casos--){
		printf("Case #%d:\n", caso++);
		scanf("%d", &n);
		for(int i = 0; i < n; ++i){
			scanf("%s", grid[i]);
			q = p = 0;
			for(int j = 0; j < n; ++j){
				if(grid[i][j] != '.'){
					++q;
					if(grid[i][j] == '1') p++;
				}
			}
			WPR[i] = p/q;
			 --q;
			 
			if(q == 0) WP[i][0] = WP[i][1] = 1;
			else {
				WP[i][1] = p/q;
				--p;
				p = max(p, 0.0);
				WP[i][0] = p/q;
			}
		//	printf("%d: %Lf %Lf\n", i, WP[i][0], WP[i][1]);
		}
		for(int i = 0; i < n; ++i){
				q = p = 0;
			
			for(int j = 0; j < n; ++j){
				if(grid[i][j] != '.'){
					p += WP[j][grid[i][j]-'0'];
					++q;
				}
			}
			OWP[i] = p/q;
		//	printf("%d: %Lf\n", i, OWP[i]);
		}
		for(int i = 0; i < n; ++i){
				q = p = 0;
			for(int j = 0; j < n; ++j){
			
				if(grid[i][j] != '.'){
					p += OWP[j];
					++q;
				}
			}
			OOWP[i] = p/q;
		//	printf("%d: %Lf\n", i, OOWP[i]);
		}
		for(int i = 0; i < n; ++i){
			printf("%.7Lf\n",  0.25 * WPR[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
		}
	}

	return 0;
}
