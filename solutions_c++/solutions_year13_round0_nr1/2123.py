#include <iostream>
#include <algorithm>
using namespace std;
#define N 4
string getColumn(string board[],int col){
	string retVal;
	int i,j;
	for(i=0;i<N;i++){
		retVal+=board[i][col];
	}

	return retVal;
}
void validate(string board[],int caseno){
	
	int i,j;
	string s1="TXXX";
	string s2="OOOT";
	string x="XXXX";
	string o="OOOO";
	string tmp;
	for(i=0;i<N;i++){
		if(board[i].compare(x)==0)
		{
			cout<<"Case #"<<caseno<<": X won"<<endl;
			return;
		}else if(board[i].compare(o)==0){
			cout<<"Case #"<<caseno<<": O won"<<endl;
			return;
		}
	}
	for(i=0;i<N;i++){
		tmp=board[i];
		sort(tmp.begin(),tmp.end());
		if(tmp.compare(s1)==0)
		{
			cout<<"Case #"<<caseno<<": X won"<<endl;
			return;
		}else if(tmp.compare(s2)==0){
			cout<<"Case #"<<caseno<<": O won"<<endl;
			return;
		}		
	}
	for(i=0;i<N;i++){
		tmp=getColumn(board,i);
		if(tmp.compare(x)==0)
		{
			cout<<"Case #"<<caseno<<": X won"<<endl;
			return;
		}else if(tmp.compare(o)==0){
			cout<<"Case #"<<caseno<<": O won"<<endl;
			return;
		}
	}
	for(i=0;i<N;i++){
		tmp=getColumn(board,i);
		sort(tmp.begin(),tmp.end());
		if(tmp.compare(s1)==0)
		{
			cout<<"Case #"<<caseno<<": X won"<<endl;
			return;
		}else if(tmp.compare(s2)==0){
			cout<<"Case #"<<caseno<<": O won"<<endl;
			return;
		}		
	}
	//diagonals
	tmp.clear();
	tmp+=board[0][0];
	tmp+=board[1][1];
	tmp+=board[2][2];
	tmp+=board[3][3];
	sort(tmp.begin(),tmp.end());
	if(tmp.compare(x)==0||tmp.compare(s1)==0){
		cout<<"Case #"<<caseno<<": X won"<<endl;
		return;
	}else if(tmp.compare(o)==0||tmp.compare(s2)==0){
		cout<<"Case #"<<caseno<<": O won"<<endl;
		return;
	}
	tmp.clear();
	tmp+=board[0][3];
	tmp+=board[1][2];
	tmp+=board[2][1];
	tmp+=board[3][0];
	sort(tmp.begin(),tmp.end());
	if(tmp.compare(x)==0||tmp.compare(s1)==0){
		cout<<"Case #"<<caseno<<": X won"<<endl;
		return;
	}else if(tmp.compare(o)==0||tmp.compare(s2)==0){
		cout<<"Case #"<<caseno<<": O won"<<endl;
		return;
	}
	for(i=0;i<N;i++){
		for(j=0;j<N;j++){
			if(board[i][j]=='.'){
				cout<<"Case #"<<caseno<<": Game has not completed"<<endl;
				return;
			}
		}
	}
	cout<<"Case #"<<caseno<<": Draw"<<endl;
}
int main(){
	int T,i,j;
	string newline;
	string board[N];
	string tmp;
	cin>>T;
	getline(cin,newline);
	for(int i=0;i<T;i++){
		//read board
		for(int j=0;j<N;j++){
			getline(cin,board[j]);
		}
		validate(board,i+1);
		getline(cin,newline);
	}
}
