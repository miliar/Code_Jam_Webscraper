// thiago kronig <thiagokronig@gmail.com>

#include <cstdio>

using namespace std;

int main() {
	
	int t,tt;
	
	char combine[200][200];
	char opposed[200];
	int list[200];
	char map[8] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};
	
	for (int i=0; i<200; i++) for(int j=0; j<200; j++) combine[i][j] = ' ';
	for (int i=0; i<200; i++) opposed[i] = ' ';
	
	scanf("%d",&t);
	for (int tt=1; tt<=t; tt++) {
	
		for (int i=0; i<8; i++) for(int j=0; j<8; j++) combine[map[i]][map[j]] = ' ';
		for (int i=0; i<8; i++) opposed[map[i]] = ' ';
				
		int c,d;
	
		scanf("%d",&c);
		while (c--) {
			char x,y,z;
			scanf(" %c%c%c", &x, &y, &z);
			combine[x][y] = z;
			combine[y][x] = z;
		}
		
		scanf("%d",&d);
		while (d--) {
			char x,y;
			scanf(" %c%c", &x, &y);
			opposed[x] = y;
			opposed[y] = x;
		}
		
		int n,out[200];
		int j = 0;
		
		for (int i=0; i<8; i++) list[map[i]] = 0;
		
		scanf("%d ",&n);
		while (n--) {
			char k,l;
			scanf("%c", &k);
			out[j] = k;
			list[k]++;
			
		//	printf(" | ");
		//	for (int m=0; m<=j; m++) printf("%c", out[m]);
			
			if (j == 0)
				j++;
			else if ((l = combine[out[j]][out[j-1]]) != ' ') {
			//	printf("%c%c%c | ",out[j],out[j-1],l);
				list[out[j]]--;
				list[out[j-1]]--;
				out[j-1] = l;
			}
			else if ((l = opposed[out[j]]) != ' ') {
				//printf(" $ %c%c %d", out[j], l, list[l]);
				if (list[l] > 0) {
					for (int i=0; i<8; i++) list[map[i]] = 0;
					j = 0;
				} else
					j++;
			}
			else
				j++;
		}
	//	printf(" \n");
		printf("Case #%d: [", tt);
		if (j > 0) {
			printf("%c", out[0]);
			for (int i=1; i<j; i++)
				printf(", %c", out[i]);
		}
		printf("]\n");
	}
	
	return 0;
}