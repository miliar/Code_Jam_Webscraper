#include <stdio.h>
#include <vector>
#include <utility>
#include <string.h>
using namespace std;

int grid[200][200];
char gridchar[200][200];
int x,y;
char atual;

bool find(int *x2,int *y2,int a,int b){
	int j,k,v = grid[a][b];
	j = -1;
	if(b+1<y) {if(grid[a][b+1]<=v ) {j = a;		k = b+1;	v = grid[j][k]; 
	//	printf("south\n");
	}}

	if(a+1<x) {if(grid[a+1][b]<=v ) {j = a+1;	k = b; 		v = grid[j][k]; 
	//	printf("east\n");
	}}
	if(a-1>=0) {if(grid[a-1][b]<=v ) {j=a-1;		k=b;		v = grid[j][k]; 
	//	printf("west\n");
	}}
	if(b-1>=0) {if(grid[a][b-1]<=v ) {j = a;		k = b-1;	v = grid[j][k]; 
	//	printf("north\n");
	}}

	if(j == -1 || grid[a][b] == v) return 0;
	*x2 = j;
	*y2 = k;
	return 1;
}
void setar(int a, int b,vector < pair<int,int> > v){
	int x2,y2;
	if(gridchar[a][b] == 0){
	//	printf("inicializando %d %d\n",a,b);
		if(find(&x2,&y2,a,b)) {
	//		printf("encontrado menor %d %d para %d %d \n",x2,y2,a,b);
			if(gridchar[x2][y2] != 0){
	//			printf("  encontrei valor em %d %d vou colocar em %d casas\n",x2,y2,v.size());
				gridchar[a][b] = gridchar[x2][y2];
				while(v.size() != 0){
	//				printf("_.setando %c para %d %d\n", gridchar[x2][y2], v[v.size()-1].first,v[v.size()-1].second);
						
					gridchar[(v[v.size()-1]).first][(v[v.size()-1]).second] = gridchar[x2][y2];
					v.pop_back();

				}
			}else{
	//			printf("+adicionando %d %d ao vetor\n",a,b);
				v.push_back(make_pair(a,b));
				setar(x2,y2,v);
			}
		}
		else{

	//		printf("_setando %c para %d %d\n", atual, a,b);
			gridchar[a][b] = atual;
			while(v.size() != 0){
				gridchar[(v[v.size()-1]).first][(v[v.size()-1]).second] = atual;

//				printf("_setando %c para %d %d\n", atual, v[v.size()-1].first,v[v.size()-1].second);

				v.pop_back();
			}

			atual++;
		}
	}
}

int main(){
	int NumCases;
	scanf("%d",&NumCases);
	
	for(int i = 1;i<=NumCases;i++){
		scanf("%d %d",&y,&x);
		memset(gridchar,0,39900);
		for(int k = 0;k<y;k++){
			for(int j = 0;j<x;j++){
				scanf("%d",&grid[j][k]);
//				printf("%d ",grid[k][j]);
			}
//			printf("\n");
		}
		atual = 'a';
		for(int k = 0;k<y;k++){
			for(int j = 0;j<x;j++){
				vector<pair<int,int> > v;
				v.clear();
				setar(j,k,v);
			}
		}
		printf("Case #%d:\n",i);
		for(int k = 0;k<y;k++){
			for(int j = 0;j<x;j++){
				printf("%c ",gridchar[j][k]);
			}
			printf("\n");
		}
		
		
	}
	return 0;
}
