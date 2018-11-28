#include<stdio.h>
#include<string.h>
#include <ctype.h>
#include <stdlib.h>
#define INF 0x3f3f3f
int T, N, M;

typedef struct {

		int val,up,down,left,right;
		char lit;
	
} Cell; 

Cell C[124][124];


void cit();

int main() {
	
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	cit();
	
	return 0;
}



void bordare() {
	
	int i,j;
	
	for(i=1; i<=N; i++) {
		C[i][0].val=INF;
		C[i][M+1].val=INF;
	}
	
	for(j=1; j<=M; j++) {
		C[0][j].val=INF;
		C[N+1][j].val=INF;
	}
	
}


void fill(int i, int j, char c) {
	
	C[i][j].lit=c;
	
	if(C[i][j].up)
		if(C[i-1][j].lit==NULL) 
			fill(i-1,j,c);
		
	if(C[i][j].down)
		if(C[i+1][j].lit==NULL) 
			fill(i+1,j,c);
	
	if(C[i][j].left)
		if(C[i][j-1].lit==NULL) 
			fill(i,j-1,c);		
		
	if(C[i][j].right)
		if(C[i][j+1].lit==NULL) 
			fill(i,j+1,c);
}


void coloreaza() {
	
	char culori[30]=" abcdefghijklmnopqrstuvwxyz";
	int ord=0;
	int i,j;
	
	
	for(i=1; i<=N; i++)
		for(j=1; j<=M; j++) {
		
			if(C[i][j].lit==NULL) {
				ord++;
				//C[i][j].lit=culori[ord];
				fill(i,j,culori[ord]);
			}
			
		}
	
	
	
}


void afis() {
	
	for(int i=1; i<=N; i++) {
		for(int j=1; j<=M; j++)
			printf("%c ", C[i][j].lit);
	printf("\n");
	}
}

void fatreaba(int caz) {
	
	int i,j;
	
	bordare();
	
	i=0;
	
	
	for(i=1; i<=N; i++) {
			for(j=1; j<=M; j++) {
				
				int tmin=INF;
				int nord=0,sud=0,est=0,vest=0;
				
				//cautare minim
					
					
					if(C[i-1][j].val < C[i][j].val)
						if(C[i-1][j].val < tmin) {
							nord=1;
							est=sud=vest=0;
							tmin=C[i-1][j].val;
						}
					


					if(C[i][j-1].val < C[i][j].val)
						if(C[i][j-1].val < tmin) {
							vest=1;
							nord=sud=est=0;
							tmin=C[i][j-1].val;
						}

					if(C[i][j+1].val < C[i][j].val)
						if(C[i][j+1].val < tmin) {
							est=1;
							nord=sud=vest=0;
							tmin=C[i][j+1].val;
						}
						
						
					if(C[i+1][j].val < C[i][j].val)
						if(C[i+1][j].val < tmin) {
							sud=1;
							nord=est=vest=0;
							tmin=C[i+1][j].val;
						}


				
				//printf("%d ", tmin);
				
				
				if(nord) {
					C[i][j].up=1;
					C[i-1][j].down=1;
				}				
				


				if(vest) {
					C[i][j].left=1;
					C[i][j-1].right=1;
				}
				
				if(est) {
					C[i][j].right=1;
					C[i][j+1].left=1;
				}
				
				if(sud) {
					C[i][j].down=1;
					C[i+1][j].up=1;
				}

				
			}
			
	}
	
	coloreaza();
	
	printf("Case #%d:\n",caz);
	afis();
	
	memset(C,0,sizeof(C));
	
}



void cit() {
	
	
	scanf("%d", &T);
	
	//T teste
	for(int k=1; k<=T; k++) {
		
		scanf("%d %d", &N, &M);
		
		//citire matrice
		for(int i=1; i<=N; i++)
			for(int j=1; j<=M; j++)
				scanf("%d", &C[i][j]);
			
		fatreaba(k);
	}
	
}
