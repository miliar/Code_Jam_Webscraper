/*
 *  Problem B
 *	Disjoint-Set
 */

#include<cstdio>
#include<cstdlib>
const int N=200;

int pr[N][N], pc[N][N], num[N][N]; // p[i][j]: the parent of the ceil (i,j)
char color[N][N]; 
int H, W;

// OP#1: create a set
void createSet(int r, int c) {
	pr[r][c] = r; pc[r][c] = c;
}

// OP#2: find the rep. of set
void find(int& r, int& c) {
	while(!(pr[r][c]==r && pc[r][c]==c)) {
		int tmpR=pr[r][c], tmpC=pc[r][c];
		r = tmpR; c=tmpC;
	}
}

// OP#3: 
void mergeSets(int r1, int c1, int r2, int c2) {
	find(r1, c1);  find(r2, c2);
	pr[r2][c2] = r1; pc[r2][c2]=c1;
}

// Op4: coloring
void tocolor(int r, int c, char& cr) {
	int tr=r, tc=c; find(tr, tc);
	if(color[tr][tc]==' ') {
		color[tr][tc]=cr;
		cr++;
	}
	color[r][c]=color[tr][tc];
}

////////////////////////
void readData(FILE* f) {
	fscanf(f, "%d %d", &H, &W);
	for(int i=0; i<N; i++) {
		for(int j=0; j<N; j++) {
			pr[i][j] = -1;
			pc[i][j]=-1;
			color[i][j]=' ';
		}
	}
	
	for(int i=0; i<H; i++) 
		for(int j=0; j<W; j++) {
			fscanf(f, "%d", &num[i][j]);
			createSet(i, j);
		}
}

void calc(int cnum) {
	int nb[][2]={{-1, 0}, {0, -1} , {0, 1}, {1, 0} };
	for(int i=0; i<H; i++)
		for(int j=0; j<W; j++) {
			int r=-1, c=-1, v=65535;
			for(int k=0; k<4; k++) {
				int tr=i+nb[k][0], tc=j+nb[k][1];
				if(tr>=0 && tr<H && tc>=0 && tc<W && num[tr][tc]<v) {
					v=num[tr][tc]; r=tr; c=tc;
				}
			}
			if(v<num[i][j]) mergeSets(i,j, r, c);
		}
	
	char ch='a';
	for(int i=0; i<H; i++)
		for(int j=0; j<W; j++) {
			tocolor(i, j, ch);
		}
	
	// output 
	printf("Case #%d:\n", cnum);
	for(int i=0; i<H; i++) {
		for(int j=0; j<W; j++) {
			printf("%c", color[i][j]);
			if(j<W-1)
				printf(" ");
		}
		printf("\n");
	}
}

//////////////////
int main (int argc, char * const argv[]) {
	FILE *f = fopen((const char*) argv[1], "r");
	int nc; fscanf(f, "%d", &nc);
	for(int k=1; k<=nc; k++) {
		readData(f);
		calc(k);
	}
	
	fclose(f);
	return 0;
}