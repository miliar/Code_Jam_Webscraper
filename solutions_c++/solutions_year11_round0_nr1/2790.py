#include<stdio.h>
#include<vector>
using namespace std;
int tc, nbutton;
char ch;
int k;

int abs (int a) {
	if (a<0) return a*-1;
	return a;
}

int main() {
	scanf("%d",&tc);
	for (int ti = 1; ti <= tc; ti++) {
		scanf("%d",&nbutton);
		
		int res = 0;
		int cur = 0;
		int saveB = 0;
		int saveO = 0;
		int posB = 1;
		int posO = 1;
		int dist = 0;
		
		for (int i = 0; i < nbutton; i++) {
			scanf(" %c %d",&ch, &k);
			if (ch == 'O') {
				dist = abs(posO-k);
				saveB += max(dist-saveO,0)+1;
				res += max(dist-saveO,0)+1;
				saveO = 0;		
				posO = k;
			}
			else if (ch == 'B') {
				dist = abs(posB-k);
				saveO += max(dist-saveB,0)+1;
				res += max(dist-saveB,0)+1;
				saveB = 0;
				posB = k;	
			}
		}
		scanf("\n");
		printf("Case #%d: %d\n",ti, res);
	}
}