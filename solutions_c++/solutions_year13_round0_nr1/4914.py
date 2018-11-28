#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		vector<string> board(4);
		for(int i=0;i<4;i++){
			cin>>board[i];
		}

		bool is_end=false;
		for(int y=0;y<4;y++){
			char c='*';
			bool is_win=true;
			for(int x=0;x<4;x++){
				if(board[y][x]=='.'){
					is_win=false;
					break;
				}
				else if(c!=board[y][x] && board[y][x]!='T'){
					if(c=='*'){
						c=board[y][x];
					}
					else{
						is_win=false;
						break;
					}
				}
			}
			if(is_win){
				cout<<"Case #"<<t<<": "<<c<<" won"<<endl;
				is_end=true;
				break;
			}
		}
		if(is_end) continue;

		for(int x=0;x<4;x++){
			char c='*';
			bool is_win=true;
			for(int y=0;y<4;y++){
				if(board[y][x]=='.'){
					is_win=false;
					break;
				}
				else if(c!=board[y][x] && board[y][x]!='T'){
					if(c=='*'){
						c=board[y][x];
					}
					else{
						is_win=false;
						break;
					}
				}
			}
			if(is_win){
				cout<<"Case #"<<t<<": "<<c<<" won"<<endl;
				is_end=true;
				break;
			}
		}

		if(is_end) continue;

		char c='*';
		bool is_win=true;
		for(int p=0;p<4;p++){
			int x=p,y=p;
			if(board[y][x]=='.'){
				is_win=false;
				break;
			}
			else if(c!=board[y][x] && board[y][x]!='T'){
				if(c=='*'){
					c=board[y][x];
				}
				else{
					is_win=false;
					break;
				}
			}
		}

		if(is_win){
			cout<<"Case #"<<t<<": "<<c<<" won"<<endl;
			is_end=true;
			continue;
		}
		if(is_end) continue;

		c='*';
		is_win=true;
		for(int p=0;p<4;p++){
			int x=p,y=3-p;
			if(board[y][x]=='.'){
				is_win=false;
				break;
			}
			else if(c!=board[y][x] && board[y][x]!='T'){
				if(c=='*'){
					c=board[y][x];
				}
				else{
					is_win=false;
					break;
				}
			}
		}

		if(is_win){
			cout<<"Case #"<<t<<": "<<c<<" won"<<endl;
			is_end=true;
			continue;
		}

		for(int y=0;y<4;y++){
			for(int x=0;x<4;x++){
				if(board[y][x]=='.' && !is_end){
					cout<<"Case #"<<t<<": "<<"Game has not completed"<<endl;
					is_end=true;
					break;
				}
			}
		}
		if(!is_end)
			cout<<"Case #"<<t<<": "<<"Draw"<<endl;
	}
}