#include <stdio.h>

int abso (int a) {
 return (a < 0) ? (-a) : (a);
}

int main (void) {
int cases;

scanf("%d", &cases);
for (int caseX = 1; caseX <= cases; ++caseX) {
	int time = 0, prev = -1, free = 0, n, pos[2] = {1, 1}, curp;
	char c;
	scanf("%d", &n);

	for (int i = 0; i < n; ++i) {
 		while ((c = getchar()) == ' ');
 		int cur = (c == 'B') ? 0 : 1;
 		scanf("%d", &curp);
		 int curt = abso(pos[cur] - curp) + 1;
	 	if (cur != prev) {
 			curt -= free;
  			free = 0;
  			if (curt < 1) {
    				curt = 1;
  			}
 		}
 		time += curt;
 		free += curt;
 		prev = cur;
 		pos[cur] = curp;
	}
	printf("Case #%d: %d\n", caseX, time);
}
}
