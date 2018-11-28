#include<stdio.h>
#include<string.h>
int J[200];
int p[200];

inline int abs(int a) {
	if ( a < 0 )	return -a;
	return a;
}

int move( int Px , int x , int m ) {
	if ( abs(Px-x) <= m )
		return x;
	if ( Px > x )	return Px-m;
	return Px+m;
}

int main()
{
	int i, j;
	int T, N;
	char s[10];
	scanf("%d", &T);
	for ( int t = 1 ; t <= T ; t++ ) {
		memset(J,0,sizeof(J));
		memset(p,0,sizeof(p));
		scanf("%d", &N);
		for ( i = 0 ; i < N ; i++ ) {
			scanf("%s%d", s, &p[i]);
			if ( s[0] == 'O' ) J[i] = 1;
			else J[i] = 2;
		}
		int ptr = 0;
		int a, b;
		for ( a = 0 ; a < N ; a++ )
			if ( J[a] == 1 )	break;
		for ( b = 0 ; b < N ; b++ )
			if ( J[b] == 2 )	break;
		
		int Pa = 1;
		int Pb = 1;
		int step;
		int total = 0;
		while ( ptr < N ) {
			if ( J[ptr] == 1 ) {
				step = abs(Pa-p[ptr])+1;
				Pa = p[ptr];
				for ( a++ ; a < N ; a++ )
					if ( J[a] == 1 )	break;
				Pb = move(Pb, p[b], step);
			}
			else {
				step = abs(Pb-p[ptr])+1;
				Pb = p[ptr];
				for ( b++ ; b < N ; b++ )
					if ( J[b] == 2 )	break;
				Pa = move(Pa, p[a], step);
			}
			total += step;
			ptr++;
		}
		printf("Case #%d: %d\n", t, total);
	}
	return 0;
}
