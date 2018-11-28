#include <iostream>
#include <cstdio>

using namespace std;

typedef long double LD;

struct team {
	
	long double wp, owp, oowp, swin;
	int ile;
};

team teams[109];
int win[109][109];
char tab[109];

int main() {
	
	int t, n;
	
	scanf("%d", &t);
	
	for (int i = 1; i <= t; i++) {
		
		scanf("%d", &n);
		
		for (int j = 0; j < n; j++) {
			scanf("%s", &tab);
			
			for (int k = 0; k < n; k++) {
					
					if (tab[k] == '1')
						win[j][k] = 1;
					else if (tab[k] == '0')
						win[j][k] = 0;
					else
						win[j][k] = 2;
			}
		}
		
		long double tmp;
		int ile;
		
		for (int j = 0; j < n; j++) {
			
			tmp = 0.0;
			ile = 0;
			
			for (int k = 0; k < n; k++) {
				
				if (win[j][k] == 1) {
					tmp += 1.0;
					ile++;
				} else if (win[j][k] == 0) {
					ile++;
				}
			}
			
			
			teams[j].wp = tmp / LD(ile);
			teams[j].swin = tmp;
			teams[j].ile = ile;
		}
		
		for (int j = 0; j < n; j++) {
			
			tmp = 0.0;
			ile = 0;
			
			for (int k = 0; k < n; k++) {
				
				if (win[j][k] != 2) {
					tmp += (teams[k].swin - (win[j][k] ? 0.0 : 1.0)) / LD(teams[k].ile - 1);
					ile++;
				}
			}
			
			teams[j].owp = tmp / LD(ile);
		}
		
		for (int j = 0; j < n; j++) {
			
			tmp = 0.0;
			ile = 0;
			
			for (int k = 0; k < n; k++) {
				
				if (win[j][k] != 2) {
					tmp += teams[k].owp;
					ile++;
				}
			}
			
			teams[j].oowp = tmp / LD(ile);
		}
		
		printf("Case #%d:\n", i);
		
		for (int j = 0; j < n; j++)
			printf("%.9Lf\n", 0.25 * teams[j].wp + 0.5 * teams[j].owp + 0.25 * teams[j].oowp);
	}
	
	return 0;
	
}
