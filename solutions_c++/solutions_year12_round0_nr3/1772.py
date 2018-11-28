#include<stdio.h>
#include<cstring>

FILE*f=fopen("recycled.in","r");
FILE*g=fopen("recycled.out","w");

int A,B,sol;
int v[10],v2[10],used[2000005];

inline void generate ( int x ){
	int aux = x;
	
	int nrc = 0;
	while ( x ){
		v2[++nrc] = x % 10;
		x /= 10;
	}
	int p10 = 1;
	for ( int i = 1 ; i <= nrc ; ++i ){
		v[i] = v2[nrc-i+1];
		p10 *= 10;
	}
	p10 /= 10;
	
	int st = 0; int dr = 0;
	for ( int i = 1 ; i <= nrc ; ++i ){
		dr = dr * 10 + v[i];
	}
	
	int p1010 = 1;
	for ( int i = 1 ; i < nrc ; ++i ){
		st = st * 10 + v[i];
		dr = dr - p10 * v[i];
		p1010 *= 10; p10 /= 10;
		
		if ( v[i+1] ){
			int b = dr * p1010 + st;
			if ( b <= B && b > aux && used[b] != aux ){
				used[b] = aux;
				++sol;
			}
		}
	}
}

int main () {
	
	int t;
	fscanf(f,"%d",&t);
	
	for ( int ii = 1 ; ii <= t ; ++ii ){
		fscanf(f,"%d %d",&A,&B); memset(used,0,sizeof(used));
		
		sol = 0;
		for ( int i = A ; i < B ; ++i ){
			generate(i);
		}
		
		fprintf(g,"Case #%d: %d\n",ii,sol);
	}
	
	
	
	fclose(f);
	fclose(g);
	
	return 0;
}
