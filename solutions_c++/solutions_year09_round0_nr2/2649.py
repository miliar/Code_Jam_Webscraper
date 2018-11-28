#include <cstdio>
#include <vector>

using namespace std;

int moves[4][2]={
				-1,0,
				0,-1,
				0,1,
				1,0,				
				};

int h, w;
int grid[150][150];
int label[150][150];
vector<char> map;
char letter;


int isValid(int a, int b){
	if(a < 0 || b < 0 || a >= h || b >= w) return 0;
	return 1;
}

int findMovement(int a, int b){
	int min = 1000;
	int i,j,k = -1;
	for(i=0;i<4;i++){
		if(isValid(a+moves[i][0],b+moves[i][1])){
			if(grid[a][b] > grid[a+moves[i][0]][b+moves[i][1]]){
				if(min > grid[a+moves[i][0]][b+moves[i][1]]){
					min = grid[a+moves[i][0]][b+moves[i][1]];
					k = i;
				}
			}
		}
	}
	return k;
}

void dfs(int a, int b){
	if(label[a][b] >= 0){
		//printf("	marking as %d(%c)\n",map.size(),map[label[a][b]]);
		map.push_back(map[label[a][b]]);
		return;
	}
	label[a][b] = map.size();
	//printf("	@(%d,%d) marked as %d\n",a,b,label[a][b]);
	int k;
	k = findMovement(a,b);
	if(k >= 0){
		
		dfs(a+moves[k][0],b+moves[k][1]);
	} else{
		//printf("	marking as %d(%c)\n",map.size(),letter);
		map.push_back(letter++);

	}
}

int main(){
	int i,j,k = 1;
	int cases;
	scanf("%d\n",&cases);
	while(cases--){
		scanf("%d %d\n",&h, &w);
		for(i=0;i<h;i++){
			for(j=0;j<w;j++){
				scanf("%d\n",&grid[i][j]);
				label[i][j] = -1;
			}
		}
		printf("Case #%d:\n",k++);
		letter = 'a';
		map.clear();
		for(i=0;i<h;i++){
			for(j=0;j<w;j++){
				if(label[i][j] < 0){
					//printf("Entering (%d,%d)\n",i,j);
					dfs(i,j);
				}
			}
		}
		
		for(i=0;i<h;i++){
			printf("%c",map[label[i][0]]);
			for(j=1;j<w;j++){
				printf(" %c",map[label[i][j]]);
			}
			printf("\n");
		}		
	}
}
