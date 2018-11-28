//			Case #1: X won
//Case #2: Draw
//Case #3: Game has not completed
//Case #4: O won
#include<iostream>
#include<string>
using namespace std;
int main(){
	int x,o,t,T,done=0;
	cin>>T;
	string mat[4],empty;
	for(int i=0; i<T; i++){
		getline(cin,empty);
		done=0;
		for (int j=0; j<4; j++) {	getline(cin,mat[j]);	}//print

		
		//Check for winning
		//check for rows
		for (int j=0; j<4; j++){
			x=o=t=0;
			for(int k=0; k<4; k++){
				if(mat[j][k]=='X') x++;
				if(mat[j][k]=='O') o++;
				if(mat[j][k]=='T') t++;
			}
			if(t==0){	if(x==4) {	cout<<"Case #"<<(i+1)<<": X won"<<endl;	done =1;	}
				else if(o==4) {	cout<<"Case #"<<(i+1)<<": O won"<<endl; done=1;	}	}
			else{	if(x==3) {	cout<<"Case #"<<(i+1)<<": X won"<<endl;	done =1;	}
				else if(o==3) {	cout<<"Case #"<<(i+1)<<": O won"<<endl; done=1;	}	}
			if(done==1) break;
		}
		
		if(done==1)	continue;
		
		//check for columns
		for (int j=0; j<4; j++){
			x=o=t=0;
			for(int k=0; k<4; k++){
				if(mat[k][j]=='X') x++;
				if(mat[k][j]=='O') o++;
				if(mat[k][j]=='T') t++;
			}
			if(t==0){	if(x==4) {	cout<<"Case #"<<(i+1)<<": X won"<<endl;	done =1;	}
				else if(o==4) {	cout<<"Case #"<<(i+1)<<": O won"<<endl; done=1;	}	}
			else{	if(x==3) {	cout<<"Case #"<<(i+1)<<": X won"<<endl;	done =1;	}
				else if(o==3) {	cout<<"Case #"<<(i+1)<<": O won"<<endl; done=1;	}	}
			if(done==1) break;
		}
		
		if(done==1)	continue;
		
		////check for two diagonals
		x=o=t=0;
		for (int j=0; j<4; j++){
			//cout<<"P"<<mat[j][j]<<endl;
			if(mat[j][j]=='X') x++;
			if(mat[j][j]=='O') o++;
			if(mat[j][j]=='T') t++;
		}
		//cout<<"M"<<x<<' '<<o<<' '<<t<<' '<<endl;
		if(t==0){	if(x==4) {	cout<<"Case #"<<(i+1)<<": X won"<<endl;	done =1;	}
				else if(o==4) {	cout<<"Case #"<<(i+1)<<": O won"<<endl; done=1;	}	}
		else{	if(x==3) {	cout<<"Case #"<<(i+1)<<": X won"<<endl;	done =1;	}
				else if(o==3) {	cout<<"Case #"<<(i+1)<<": O won"<<endl; done=1;	}	}
				
		if(done==1)	continue;
		
		x=o=t=0;
		for (int j=0; j<4; j++){
			if(mat[j][3-j]=='X') x++;
			if(mat[j][3-j]=='O') o++;
			if(mat[j][3-j]=='T') t++;
		}
		//cout<<"A"<<x<<' '<<o<<' '<<t<<' '<<endl;
		if(t==0){	if(x==4) {	cout<<"Case #"<<(i+1)<<": X won"<<endl;	done =1;	}
				else if(o==4) {	cout<<"Case #"<<(i+1)<<": O won"<<endl; done=1;	}	}
			else{	if(x==3) {	cout<<"Case #"<<(i+1)<<": X won"<<endl;	done =1;	}
				else if(o==3) {	cout<<"Case #"<<(i+1)<<": O won"<<endl; done=1;	}	}
				
		if(done==1)	continue;
		//for game not completed
		for (int j=0; j<4; j++) {
			if(mat[j][0] == '.' ||mat[j][1] == '.' ||mat[j][2] == '.' ||mat[j][3] == '.' ){ 
				cout<<"Case #"<<(i+1)<<": Game has not completed"<<endl;
				done=1; break;	}
		}
		if(done==1)	continue;
				
		if(done==0){	cout<<"Case #"<<(i+1)<<": Draw"<<endl;	}
		
	}
}
