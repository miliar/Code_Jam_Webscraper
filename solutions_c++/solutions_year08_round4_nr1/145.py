#include <stdio.h>
#include <string.h>

const int INFINITY = 2000000;
const int T_AND = 0;
const int T_OR = 1;
const int T_0 = 2;
const int T_1 = 3;

int min(int a, int b) { return (a>b?b:a);}
#define L(i) (2*i+1)
#define R(i) (2*i+2)

void main(void){
	FILE* fin = fopen("tree.in","rt");
	FILE* fout = fopen("tree.out","wt");

	int N;
	fscanf(fin,"%d",&N);
	for(int i=0;i<N;i++){
		int dimension;
		
		int Tree[40000];
		bool Changable[40000];
		int M[40000][2];
		int V,Nodes,G,C;
		memset(Tree,0,sizeof(Tree));
		memset(M,0,sizeof(M));
		memset(Changable,0,sizeof(Changable));

		fscanf(fin, "%d %d\n", &Nodes, &V);
		for (int j=0;j<Nodes;j++) 
		if(j<((Nodes-1)/2)) {
			fscanf(fin, "%d %d\n", &G, &C);
				if (G==1) Tree[j] = T_AND; else Tree[j] = T_OR;
				if (C==1) Changable[j] = true; else Changable[j] = false;
				M[j][0] = INFINITY;M[j][1] = INFINITY;
			} else {
				fscanf(fin, "%d\n", &G);
				if (G==1) Tree[j] = T_1; else Tree[j] = T_0;
				Changable[j] = false;
				M[j][0] = INFINITY;M[j][1] = INFINITY;
		}
		
		for(int j=Nodes-1;j>=0;j--) {
			if (Tree[j] == T_0) {
				M[j][0] = 0; M[j][1] = INFINITY;			
			}else if (Tree[j] == T_1) {
				M[j][1] = 0; M[j][0] = INFINITY;			
			}else if (Tree[j] == T_OR) {
				M[j][0] = min(INFINITY, M[L(j)][0] + M[R(j)][0]);
				M[j][1] = min(M[L(j)][0] + M[R(j)][1],
								min( M[L(j)][1] + M[R(j)][0],
										M[L(j)][1] + M[R(j)][1])
							);
				if (Changable[j])  M[j][0] = min(M[j][0],1 + min(M[L(j)][0] + M[R(j)][1],M[L(j)][1] + M[R(j)][0])
												);
			}else if (Tree[j] == T_AND) {
				M[j][1] = min(INFINITY, M[L(j)][1] + M[R(j)][1]);
				M[j][0] = min(M[L(j)][0] + M[R(j)][1],
					min( M[L(j)][1] + M[R(j)][0],
					M[L(j)][0] + M[R(j)][0])
					);
				if (Changable[j])  M[j][1] = min(M[j][1],1 + min(M[L(j)][0] + M[R(j)][1],M[L(j)][1] + M[R(j)][0])
					);
			}
		}
			
		if (M[0][V] == INFINITY)
			fprintf(fout,"Case #%d: IMPOSSIBLE\n",i+1);
		else
			fprintf(fout,"Case #%d: %d\n",i+1, M[0][V]);

	}

	fclose(fin);
	fclose(fout);
}