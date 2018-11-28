// CodeJam1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int jeden() {
	int n; scanf("%d", &n);
	int tim[] = {0,0};
	int pos[] = {1, 1};
	int sum = 0;
	for(int i = 0; i<n; i++) {
		int x; char c[20];
		scanf("%s%d", c, &x);
		int t;
		if(c[0] == 'O') t = 0;
		else t = 1;
		//printf("%d %d\n", x, t);
		int dist = x - pos[t];
		if(dist<0) dist = -dist;
		int load = dist - tim[t];
		if(load < 1) load = 0;
		load++;

		tim[1-t] += load;
		sum += load;
		tim[t] += load;

		pos[t] = x;
		tim[t] = 0;
	}
	return sum;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int d; scanf("%d", &d);
	for(int i = 1; i<=d; i++) {
		printf("Case #%d: %d\n", i, jeden());
	}
}

