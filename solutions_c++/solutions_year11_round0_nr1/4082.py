#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <map>

//#define dprintf(...) printf(__VA_ARGS__)
#define dprintf(...)

using namespace std;

int main(void) {
	int cases=0;
	long int i=0,j=0;
	long int n=0,step=0;
	long int time, otime, btime;
	int opos,bpos,dpos;
	char tmp;
	char buffer[1024];
	char* bufp;
	if(!scanf("%d\n",&cases)) return 1;
	dprintf("DEBUG: %d cases\n",cases);
	for(i=0;i<cases;i++) {
		if(gets(buffer)==NULL) return 2;
		n = strtol(buffer, &bufp, 10);
		dprintf("DEBUG: '%s' - %ld buttons\n",buffer, n);
		time = otime = btime = 0;
		opos = bpos = 0;
		for(j=0;j<n;j++) {
			while(isblank(*bufp)) (bufp)++;
			tmp=(*bufp);
			(bufp)++;
			step = strtol(bufp, &bufp, 10);
			if(tmp=='B') {
				dprintf("DEBUG: B -> %ld\n",step);
				dpos = abs(bpos - step);
				if(btime+dpos<time) {
					time++;
				} else {
					time = btime + dpos + 1;
				}
				btime = time;
				bpos = step;
			} else {
				dprintf("DEBUG: O -> %ld\n",step);
				dpos = abs(opos - step);
				if(otime+dpos<time) {
					time++;
				} else {
					time = otime + dpos + 1;
				}
				otime = time;
				opos = step;
			}
			dprintf("DEBUG: time = %ld\n", time);
		}
		printf("Case #%ld: %ld\n", i+1, time - 1);
	}
	return 0;
}


