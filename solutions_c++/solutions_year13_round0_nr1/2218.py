#include<iostream>
#include<vector>
#include<string>


using namespace std;


bool won(vector<string> board,char ch){
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(board[i][j]=='T')
				board[i][j]=ch;
		}
	}
	
	for(int i=0;i<4;i++){
		bool fr=true,fc=true;
		for(int j=0;j<4;j++){
			if(board[i][j]!=ch)
				fr=false;
			if(board[j][i]!=ch)
				fc=false;
		}
		if(fr||fc)
			return true;
	}
	
	bool f1=true,f2=true;
	for(int i=0;i<4;i++){
		if(board[i][i]!=ch)
			f1=false;
		if(board[i][3-i]!=ch)
			f2=false;
	}
	if(f1||f2)
		return true;
	
	return false;
}

bool Draw(vector<string> board){
	
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(board[i][j]=='.'){
				return false;
			}
		}
	}
	return true;
}

vector<string> input_data(){
	vector<string> result(4);
	for(int i=0;i<4;i++){
		cin>>result[i];
	}
	return result;
}


int main(){
	
	int T;
	cin>>T;
	for(int testcase=1;testcase<=T;testcase++){
		vector<string> board=input_data();
		
		if(won(board,'X')){
			cout<<"Case #"<<testcase<<": X won"<<endl;
		}else if(won(board,'O')){
			cout<<"Case #"<<testcase<<": O won"<<endl;
		}else if(Draw(board)){
			cout<<"Case #"<<testcase<<": Draw"<<endl;
		}else{
			cout<<"Case #"<<testcase<<": Game has not completed"<<endl;
		}
	}
	return 0;
}
