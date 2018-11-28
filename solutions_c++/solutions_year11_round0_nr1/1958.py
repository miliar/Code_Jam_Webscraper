#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define _max(i , j) (i) > (j) ? (i) : (j)

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, t, opos, bpos, otime, btime, ctime, n, i, nxt;
	char str[10];
	scanf("%d", &T);
	for(t = 1; t <= T; t++){
		scanf("%d", &n);
		opos = bpos = 1;
		otime = btime = ctime = 0;
		for(i = 0; i < n; i++){
			scanf("%s %d", str, &nxt);
			if(str[0] == 'O'){
				otime = _max((abs(nxt - opos) + otime + 1) , (ctime + 1));
				ctime = otime;
				opos = nxt;
			}
			else {
				btime = _max((abs(nxt - bpos) + btime + 1) , (ctime + 1));
				ctime = btime;
				bpos = nxt;
			}
		}
		printf("Case #%d: %d\n", t, ctime);
	}
	return 0;
}
