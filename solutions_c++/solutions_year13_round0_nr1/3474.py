#include<iostream>
#include<fstream>
#include<vector>
#include<sstream>
using namespace std;
class Judge{
	public:
	vector<int> prefed;
    Judge(){
		int array[]={0xf000,0x0f00,0x00f0,0x000f,0x8888,0x4444,0x2222,0x1111,0x8421,0x1248};
		prefed=vector<int> (array,array+sizeof(array)/sizeof(int));
	}
	int getBoard(vector<string> board,char a){
		int result=0;
		for(int row=0;row <4;row++)
		for(int col=0;col <4;col++){
			if(board[row][col]=='T'||board[row][col]==a){
				result|=1<<(row*4+col);
			}		
		}
		return result;
	}
	int getStatus(int board){
		for(int i=0;i <(int)prefed.size();i++){
			if((prefed[i]&board)==prefed[i]){
				return 1;
			}
		}
		return 0;
	}
	int isFull(vector<string>board){
		for(int i=0;i < 4;i++)
		for(int j=0;j < 4;j++){
			if(board[i][j]=='.')return 0;
		}	
		return 1;
	}
};
int main(){

	ifstream myfile;
	myfile.open("input.txt");
	string N;int num;
	Judge judge;

	if(myfile.is_open()){
		if(myfile.good()){
			getline(myfile,N);
			istringstream(N) >> num;
			
		}
		for(int i=1;i <=num;i++){
			vector<string>board;
			string tmp;
			for(int j=0;j <4;j++)
			{
				getline(myfile,tmp);
				board.push_back(tmp);
			}
			getline(myfile,tmp);
			int X=judge.getBoard(board,'X');
			int O=judge.getBoard(board,'O');
			if(judge.getStatus(X)){
				cout << "Case #" << i<<": X won" << endl; 
			}				
			else if(judge.getStatus(O)){
				cout << "Case #" << i<<": O won" << endl;
			}
			else if(judge.isFull(board)){
				cout << "Case #" << i << ": Draw" << endl;
			}
			else {
				cout << "Case #" << i << ": Game has not completed" << endl;
			}
		}
	}
}
