#include<iostream>
#include<cstdio>

using namespace std;

int main(){
	int t,kase,i,j,ti,tj;
	bool won=false,incomplete=false;
	char winner='T',symbol;
	scanf("%d\n",&t);
	kase=1;
	while(t--){
		int grid[4][4]={0};
		ti=-1,tj=-1;
		won=false;
		incomplete=false;
		winner='T';
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				scanf("%c",&symbol);
				switch(symbol){
					case 'X':
						grid[i][j]=1;
						break;
					case 'O':
						grid[i][j]=-1;
						break;
					case '.':
						grid[i][j]=0;
						incomplete=true;
						break;
					case 'T':
						grid[i][j]=0;
						ti=i;
						tj=j;
						break;
				}
			}
			getchar();
		}
		getchar();
		int row[4]={0}, column[4]={0}, diagonal[2]={0};
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				row[i]+=grid[i][j];
				column[j]+=grid[i][j];
				if(i==j)
					diagonal[0]+=grid[i][j];
			}
			diagonal[1]+=grid[i][3-i];
		}
		for(i=0;i<4;i++){
			if(row[i]==4 || row[i]==-4){
				won=true;
				winner=row[i]>0?'X':'O';
				break;
			}
			if(column[i]==4 || column[i]==-4){
				won=true;
				winner=column[i]>0?'X':'O';
				break;
			}
			if(ti!=-1){
				if(ti==i && (row[i]==3 || row[i]==-3)){
					won=true;
					winner=row[i]>0?'X':'O';
					break;
				}
				if(tj==i && (column[i]==3 || column[i]==-3)){
					won=true;
					winner=column[i]>0?'X':'O';
					break;
				}
			}
		}
		if(!won && (diagonal[0]>2 || diagonal[0]<-2 || diagonal[1]>2 || diagonal[1]<-2)){
			if(diagonal[0]==4 || diagonal[0]==-4){
				won=true;
				winner=diagonal[0]>0?'X':'O';
			}
			else if(diagonal[1]==4 || diagonal[1]==-4){
				won=true;
				winner=diagonal[1]>0?'X':'O';
			}
			else if(ti!=-1){
					if(ti==tj && (diagonal[0]==3 || diagonal[0]==-3)){
						won=true;
						winner=diagonal[0]>0?'X':'O';
					}
					else if(ti+tj==3){
						if((ti>tj && ti>1) || (ti<tj && ti<2)){
							won=true;
							winner=diagonal[1]>0?'X':'O';
						}
					}
			}
			else{}
		}
		printf("Case #%d: ",kase++);
		won?printf("%c won\n",winner):incomplete?printf("Game has not completed\n"):printf("Draw\n");
	}
	return 0;
}
