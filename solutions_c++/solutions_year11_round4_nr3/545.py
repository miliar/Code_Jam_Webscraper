#include<stdio.h>
#include<stdlib.h>
#include<string.h>

double map[520][520];
int p[1002];
int a[1002];
int time[1002];

double abs(double a) {
	if ( a < 0 )	return -a;
	return a;
}
		

int main()
{
	int i, j, k, l;
	int T, N, M, L;
	scanf("%d", &T);
	memset(a,0,sizeof(a));
	int px = 0;
	for ( i = 2 ; i < 1002 ; i++ ) {
		if ( a[i] )	continue;
		for ( j = 2*i ; j < 1002 ; j+=i ) {
			a[i] = 1;
		}
		p[px++] = i;
	}
	
	for ( int t = 1 ; t <= T ; t++ ) {
		scanf("%d", &N);
		if ( N == 1 ) {
			printf("Case #%d: 0\n", t);
			continue;
		}
		int count = 1;
		memset(time,0,sizeof(time));
		int X;
		for ( j = 2 ; j <= N ; j++ ) {
			X = j;
			int key = 0;
			for ( i = 0 ; X != 1 && i < px ; i++ ) {
				int tmp = 0;
				while ( X%p[i]==0 ) {
					tmp++;
					X/=p[i];
				}
				if ( tmp > time[i] ) {
					key = 1;
					time[i] = tmp;
				}
			}
			if ( key == 1 ) {
				count++;
			}
		}
		int worst = 0;
		for ( i = 0 ; i < px ; i++ ) {
			if ( time[i] > 0 )
				worst++;
		}
		printf("Case #%d: %d\n", t, count-worst);
	}
	return 0;
}