#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

#define N 1
#define W 2
#define E 3
#define S 4

#define MX 10000

int h,w;

char lab[102][102];
int  alt[102][102];
char dir[102][102];

char last;

int get_pos ( int i , int j ){
	int m, p;
	m = alt[i][j];
	p = 0;
	if ( m > alt[i-1][j] ){
		m = alt[i-1][j];
		p = N;
	}
	if ( m > alt[i][j-1] ){
		m = alt[i][j-1];
		p = W;
	}
	if ( m > alt[i][j+1] ){
		m = alt[i][j+1];
		p = E;
	}
	if ( m > alt[i+1][j] ){
		m = alt[i+1][j];
		p = S;
	}
	return p;
}

void high_is_diff(int i , int j){
	if ( dir[i-1][j] == S && (lab[i-1][j] > lab[i][j]) ){
		lab[i-1][j] = lab[i][j];
		high_is_diff(i-1,j);
	}
	if ( dir[i][j-1] == E && (lab[i][j-1] > lab[i][j]) ){
		lab[i][j-1] = lab[i][j];
		high_is_diff(i,j-1);
	}

	if ( dir[i][j+1] == W && (lab[i][j+1] > lab[i][j]) ){
		lab[i][j+1] = lab[i][j];
		high_is_diff(i,j+1);
	}	

	if ( dir[i+1][j] == N && (lab[i+1][j] > lab[i][j]) ){
		lab[i+1][j] = lab[i][j];
		high_is_diff(i+1,j);
	}
}

void refresh (int i , int j){
	int p;
	p = dir[i][j];

	if ( p == N ){
		if ( lab[i][j] > lab[i-1][j] ){
			lab[i][j] = lab[i-1][j];
			high_is_diff(i,j);
		}else{
			lab[i-1][j] = lab[i][j];
			high_is_diff(i,j);
			
			refresh(i-1,j);
		}
	} else if ( p == W ){
		if ( lab[i][j] > lab[i][j-1] ){
			lab[i][j] = lab[i][j-1];
			
			high_is_diff(i,j);
		}else{
			lab[i][j-1] = lab[i][j];
			high_is_diff(i,j);
			
			refresh(i,j-1);
		}
	} else if ( p == E ){
		if ( lab[i][j] > lab[i][j+1] ){
			lab[i][j] = lab[i][j+1];
			high_is_diff(i,j);
		}else{
			lab[i][j+1] = lab[i][j];
			high_is_diff(i,j);
			
			refresh(i,j+1);
		}
	} else if ( p == S ){
		if ( lab[i][j] > lab[i+1][j] ){
			lab[i][j] = lab[i+1][j];
			high_is_diff(i,j);
		}else{
			lab[i+1][j] = lab[i][j];
			high_is_diff(i,j);
			
			refresh(i+1,j);
		}
	} else
		high_is_diff(i,j);
}

void go(){
	int i , j , p ;
	last = 'a';

	for ( i = 1 ; i <= h ; i++ ){
		alt[i][w+1] = MX;
		dir[i][w+1] = 0;
	}
	for ( i = 1 ; i <= w ; i++ ){
		alt[h+1][i] = MX;
		dir[h+1][i] = 0;
	}
	
	for ( i = 1 ; i <= h ; i++ )
		for ( j = 1; j <= w ; j++ )
			lab[i][j] = '{';

	for ( i = 1 ; i <= h ; i++ )
		for ( j = 1; j <= w ; j++ )
			dir[i][j] = get_pos(i,j);
	
	lab[1][1] = 'a';
	
	for ( i = 1 ; i <= h ; i++ )
		for ( j = 1; j <= w ; j++ ){
			if ( lab[i][j] == '{' ){
				lab[i][j] = ++last;
			}
			refresh(i,j);
		}
}

int main(){
	int T,t;
	int i,j;

	for ( i = 1 ; i < 102 ; i++ ){
		alt[i][0] = alt[0][i] = MX;
		dir[i][0] = dir[0][i] = 0;
	}

	scanf("%d",&T);
	for ( t = 1 ; t <= T ; t++ ){
		scanf("%d %d", &h, &w);
		for ( i = 1 ; i <= h ; i++ )
			for ( j = 1; j <= w ; j++ )
				scanf("%d", &alt[i][j]);

		printf("Case #%d:\n", t);
		go();
	
		for ( i = 1 ; i <= h ; i++ ){
			for ( j = 1; j < w ; j++ )
				printf("%c ", lab[i][j]);
			printf("%c\n", lab[i][w]);
		}
	}

	return 0;
}
