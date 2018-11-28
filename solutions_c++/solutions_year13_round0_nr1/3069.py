#include <sstream>
#include <fstream>
#include <iostream>
#include <string>

int board[4][4];
int result; //0 draw, 1 X win, 2 Y win, 3 incomplete
bool incomplete;

void ReadGame(std::ifstream& inputFile)
{
	incomplete=false;	
	std::string line;	
	if(inputFile.is_open()){
		for(int i=0; i<4; ++i){
    		getline(inputFile,line); 
			for(int j=0; j<4; ++j){
				if(line[j]=='X') board[i][j] = 1;
				else if(line[j]=='O') board[i][j]=-1;
				else if(line[j]=='T') board[i][j]=0;
				else{	
					board[i][j]=10; //large enough
					incomplete=true;
				}
			}
		}
		getline(inputFile,line); 
	}
}

void Output(int idx)
{
	if(result==1){
		std::cout<<"Case #"<<idx<<": X won"<<std::endl;
	}	
	else if(result==2){
		std::cout<<"Case #"<<idx<<": O won"<<std::endl;
	}
	else if(result==3){
		std::cout<<"Case #"<<idx<<": Game has not completed"<<std::endl;
	}
	else{
		std::cout<<"Case #"<<idx<<": Draw"<<std::endl;
	}
}

void JudgeGame()
{
	int h_sum[4]={0,0,0,0}; 
	int v_sum[4]={0,0,0,0};
	int d_sum[2]={0,0};	
	for(int i=0; i<4; i++){
		for(int j=0; j<4; j++){
			h_sum[i]+=board[i][j];
			v_sum[j]+=board[i][j];
		}
	}
	d_sum[0]=board[0][0]+board[1][1]+board[2][2]+board[3][3];
	d_sum[1]=board[3][0]+board[2][1]+board[1][2]+board[0][3];
	for(int i=0; i<4; i++){	
		if((h_sum[i]>=3 && h_sum[i]<=4) || (v_sum[i]>=3 && v_sum[i]<=4)){
			result=1;
			return;
		}
		if((h_sum[i]<=-3 && h_sum[i]>=-4) || (v_sum[i]<=-3 && v_sum[i]>=-4)){
			result=2;
			return;
		}
	}
	for(int i=0; i<2; i++){
		if(d_sum[i]>=3 && d_sum[i]<=4){
			result=1;
			return;
		}
		if(d_sum[i]<=-3 && d_sum[i]>=-4){
			result=2;
			return;
		}
	}
	if(incomplete) result = 3;
	else result = 0;
	return;
}

int main(int argv, char** argc)
{
	std::ifstream inputFile(argc[1]);
	std::string strNumOfCases;
	int n_of_cases=0;
    if(inputFile.is_open()){
    	getline(inputFile, strNumOfCases); 
		std::stringstream ss;
		ss<<strNumOfCases;
		ss>>n_of_cases;
		for(int i=1; i<=n_of_cases; i++){
			ReadGame(inputFile);
			JudgeGame();
			Output(i);	
			
		}
	}
	
		
	
}
