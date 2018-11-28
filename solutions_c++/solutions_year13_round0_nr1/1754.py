#include<iostream>
#include<string>
using namespace std;
int tic[20][20];
void initZ(){
	for(int i=0;i<10;++i)for(int j=0;j<10;++j)tic[i][j]=0;
}
int win(int num){
	if(num%16==0)return 1;
	else if(num%81==0)return 2;
	else return 0;
}
bool checkComplete(){
	for(int i=0;i<4;++i){
		for(int j=0;j<4;++j){
			if(tic[i][j]==1)return 1;
		}
	}
	return 0;
}
string play(){
	int row[4] = {1,1,1,1};
	int col[4] = {1,1,1,1};
	int di[2] = {1,1};
	for(int i=0;i<4;++i){
		for(int j=0;j<4;++j){
			row[i]*=tic[i][j];
			col[j]*=tic[i][j];
		}
	}
	for(int i=0;i<4;++i){
		di[0] *= tic[i][i];
		di[1] *= tic[i][3-i];
	}

	for(int i=0;i<4;++i){
		if(win(row[i])==1 || win(col[i])==1)return "O won";
		else if(win(row[i])==2 || win(col[i])==2)return "X won";
	}

	for(int i=0;i<2;++i){
		if(win(di[i])==1)return "O won";
		else if(win(di[i])==2)return "X won";
	}
	if(checkComplete())return "Game has not completed";
	return "Draw";
}
void solve(){
	int t;
	cin>>t;
	for(int k=1;k<=t;++k){
		initZ();

		string toe;
		for(int i=0;i<4;++i){
			cin>>toe;
			for(int j=0;j<4;++j){
				if(toe[j]=='X')tic[i][j] = 3;
				else if(toe[j]=='O')tic[i][j]=2;
				else if(toe[j]=='T')tic[i][j]=6;
				else tic[i][j]=1;
			}
		}

		cout<<"Case #"<<k<<": "<<play()<<endl;
	}
}
int main(){
	solve();
}