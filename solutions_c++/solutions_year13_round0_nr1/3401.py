#include<fstream.h>
ifstream in("input.in");
ofstream out("output.txt");
int Test;
char Map[100][100],Grid;
int Ans,Flag,Cnt;
char Ansgrid[100];
void Find(int test){
	int i,k,j;
	Ans=0;
	Cnt=0;
	for(k=0;k<4;k++){
		Grid=Map[0][k];
		if(Grid=='.')continue;
		if(Grid=='T'){Grid=Map[1][k]; if(Grid=='.')continue;}
		for(i=0;i<4;i++){
			if(Map[i][k]!=Grid){
				if(Map[i][k]=='T')continue;
				break;
			}
		}
		if(i==4){
			Ansgrid[Ans]=Grid;
			Ans+=1;
		}
	}
	for(k=0;k<4;k++){
		Grid=Map[k][0];
		if(Grid=='.')continue;
		if(Grid=='T'){Grid=Map[k][1]; if(Grid=='.')continue;}
		for(i=0;i<4;i++){
			if(Map[k][i]!=Grid){
				if(Map[k][i]=='T')continue;
				break;
			}
		}
		if(i==4){
			Ansgrid[Ans]=Grid;
			Ans+=1;
		}
	}
	for(k=0;k<=0;k++){
		Grid=Map[0][0];
		if(Grid=='.')continue;
		if(Grid=='T'){Grid=Map[1][1]; if(Grid=='.')continue;}
		for(i=0;i<4;i++){
			if(Map[i][i]!=Grid){
				if(Map[i][i]=='T')continue;
				break;
			}
		}
		if(i==4){
			Ansgrid[Ans]=Grid;
			Ans+=1;
		}
	}
	for(k=0;k<=0;k++){
		Grid=Map[3][0];
		if(Grid=='.')continue;
		if(Grid=='T'){Grid=Map[2][1]; if(Grid=='.')continue;}
		for(i=0;i<4;i++){
			if(Map[(3-i)][i]!=Grid){
				if(Map[(3-i)][i]=='T')continue;
				break;
			}
		}
		if(i==4){
			Ansgrid[Ans]=Grid;
			Ans+=1;
		}
	}
	Flag=0;
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			if(Map[i][j]=='.'){
				Flag=1;
			}
		}
	}
	if(Ans==0){
		if(Flag==1){
			out<<"Case #"<<test<<": Game has not completed\n";
			return;
		}
		if(Flag==0){
			out<<"Case #"<<test<<": Draw\n";
			return;
		}
	}
	if(Ans==1){
		out<<"Case #"<<test<<": "<<Ansgrid[0]<<" won\n";
		return;
	}
	for(i=0;i<Ans-1;i++){
		if(Ansgrid[i]!=Ansgrid[i+1])break;
	}
	if(i==Ans-1){
		out<<"Case #"<<test<<": "<<Ansgrid[0]<<" won\n";
		return;
	}
}
int main(){
	int i,k;
	in>>Test;
	for(k=0;k<Test;k++){
		for(i=0;i<4;i++){
			in>>Map[i];
		}
		Find(k+1);
	}
	return 0;
}