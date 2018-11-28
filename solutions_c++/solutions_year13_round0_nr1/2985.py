#include <string>
#include <iostream>
#include <algorithm>
#include <cstdlib>

using namespace std;

int main(){
	int T;
	cin >> T;
	for(int t=1;t<=T;t++){
		string s[4];
		for(int i=0;i<4;i++){
			
			cin >> s[i];
			while(s[i].size()!=4) cin >> s[i];
		}

		int dot = 0;
		int state = -1;
		//rows
		for(int i=0;i<4;i++){
			int numx = 0;
			int numo = 0;
			int numt = 0;
			for(int j=0;j<4;j++){
				if(s[i][j]=='X') numx++;
				else if(s[i][j]=='O') numo++;
				else if(s[i][j]=='T') numt++;
				else if(s[i][j]=='.') dot++;
			}
			if((numx==3&&numt==1)||numx==4){
				state = 1;
				goto printAns;
			} else if((numo==3&&numt==1)||numo==4){
				state = 2;
				goto printAns;
			}
		}
		//columns
		for(int i=0;i<4;i++){
			int numx = 0;
			int numo = 0;
			int numt = 0;
			for(int j=0;j<4;j++){
				if(s[j][i]=='X') numx++;
				else if(s[j][i]=='O') numo++;
				else if(s[j][i]=='T') numt++;
			}
			if((numx==3&&numt==1)||numx==4){
				state = 1;
				goto printAns;
			} else if((numo==3&&numt==1)||numo==4){
				state = 2;
				goto printAns;
			}
		}

		//diag1
		{
			int numx = 0;
			int numo = 0;
			int numt = 0;
			for(int i=0;i<4;i++){
				if(s[i][i]=='X') numx++;
				else if(s[i][i]=='O') numo++;
				else if(s[i][i]=='T') numt++;
			}
			if((numx==3&&numt==1)||numx==4){
				state = 1;
				goto printAns;
			} else if((numo==3&&numt==1)||numo==4){
				state = 2;
				goto printAns;
			}
		}

		//diag2
		{
			int numx = 0;
			int numo = 0;
			int numt = 0;
			for(int i=0;i<4;i++){
				if(s[i][3-i]=='X') numx++;
				else if(s[i][3-i]=='O') numo++;
				else if(s[i][3-i]=='T') numt++;
			}
			if((numx==3&&numt==1)||numx==4){
				state = 1;
				goto printAns;
			} else if((numo==3&&numt==1)||numo==4){
				state = 2;
				goto printAns;
			}
		}

		if(dot>0) state = 0;
		else state = 3;
		printAns:
		if(state==0){
			cout<<"Case #"<<t<<": Game has not completed"<<endl;
		} else if(state==1){
			cout<<"Case #"<<t<<": X won"<<endl;
		} else if(state==2){
			cout<<"Case #"<<t<<": O won"<<endl;
		} else if(state==3){
			cout<<"Case #"<<t<<": Draw"<<endl;
		} else {
			cout<<"error"<<endl;
		}
	}
}