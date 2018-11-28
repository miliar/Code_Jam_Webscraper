#include<stdio.h>
#include<string>
#include<map>
#define INF 20000

using namespace std;
int mat[200][200];
int wat[200][200];
char lab[200][200];
int vis[200][200];

void bucket(int letra, int row, int col){
	if(vis[row][col])
		return;

	vis[row][col]=1;
	lab[row][col]='a'+letra;
	if(wat[row-1][col]==4){
		bucket(letra,row-1,col);
	}
	if(wat[row][col-1]==3){
		bucket(letra,row,col-1);
	}
	if(wat[row][col+1]==2){
		bucket(letra,row,col+1);
	}
	if(wat[row+1][col]==1){
		bucket(letra,row+1,col);
	}	
}

int main(){
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		int row,col;
		scanf("%d%d",&row,&col);
		for(int j=0;j<=row+1;j++){
			for(int k=0;k<=col+1;k++){
				mat[j][k]=INF;
				vis[j][k]=0;
				wat[j][k]=5;//forbiden
			}
		}
		for(int j=1;j<=row;j++){		
			for(int k=1;k<=col;k++){
				scanf("%d",&mat[j][k]);
			}
		}
		//descobrir as direcoes e sinks
		for(int j=1;j<=row;j++){		
			for(int k=1;k<=col;k++){
				int min = 15000;
				int dir = 0;
				//cima
				if(mat[j-1][k]<min){
					min = mat[j-1][k];
					dir = 1;
				}
				//esq
				if(mat[j][k-1]<min){
					min = mat[j][k-1];
					dir = 2;
				}
				//dir
				if(mat[j][k+1]<min){
					min = mat[j][k+1];
					dir = 3;
				}
				//baixo
				if(mat[j+1][k]<min){
					min = mat[j+1][k];
					dir = 4;
				}
				if((min>=mat[j][k])&&(min!=15000)){
					dir=0;
				}
				//sink = 0
				wat[j][k] = dir;				
			}
		}
		//bucket fill
		int letra = 0;
		for(int j=1;j<=row;j++){
			for(int k=1;k<=col;k++){
				if(wat[j][k]==0){
					bucket(letra,j,k);
					letra++;
				}
			}
		}
		
	/*	
	printf("Mat\n");
		for(int j=0;j<=row+1;j++){
			for(int k=0;k<=col+1;k++){
				printf("%d ",mat[j][k]);
			}
			printf("\n");
		}

	printf("Dir\n");
		for(int j=0;j<=row+1;j++){
			for(int k=0;k<=col+1;k++){
				printf("%d ",wat[j][k]);
			}
			printf("\n");
		}

	printf("Lab\n");
		for(int j=1;j<=row;j++){
			for(int k=1;k<=col;k++){
				printf("%c ",lab[j][k]);
			}
			printf("\n");
		}
	printf("Final\n");*/

		printf("Case #%d:\n",i+1);
		int count = 0;
		map< int, int > mapa;
		for(int j=0;j<26;j++){
			mapa[j]=0;
		}
		for(int j=1;j<=row;j++){
			for(int k=1;k<=col;k++){
				if(mapa[lab[j][k]]!=0){
					printf("%c ",'a'+mapa[lab[j][k]]-1);
				}
				else{
					count++;
					mapa[lab[j][k]]=count;
					printf("%c ",'a'+mapa[lab[j][k]]-1);
				}
			}
			printf("\n");
		}
			


		
		
	}



}
