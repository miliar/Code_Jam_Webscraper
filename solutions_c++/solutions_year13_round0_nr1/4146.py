#include <iostream>
#include <string>

using namespace std;

const int movr[4]={0,1,1,1};
const int movc[4]={1,0,1,-1};

string B[4];

int anal(int r, int c, int mov){
	int o=0,x=0;
	
	for (int i=0; i<4; i++,r+=movr[mov],c+=movc[mov]){
		if(B[r][c]=='O'){o++;continue;}
		if(B[r][c]=='X'){x++;continue;}
		if(B[r][c]=='.')continue;
		o++;x++;
	}
	
	if(o==4)return 0;
	if(x==4)return 1;
	return -1;
}

int main(){
	int t;
	cin >> t;
	
	for(int tt=1; tt<=t; tt++){
		int dot=0;
		
		for (int i=0; i<4; i++){
			cin>>B[i];
			for(int j=0; j<4; j++){
				if (B[i][j]=='.')dot++;
			}
		}
		
		int win=-1;
		
		for(int i=0; i<4&&win==-1; i++){
			win=anal(i,0,0);
		}
		for(int i=0; i<4&&win==-1; i++){
			win=anal(0,i,1);
		}
		
		if(win==-1)win=anal(0,0,2);
		if(win==-1)win=anal(0,3,3);
		
		if(win!=-1){
			printf("Case #%d: %c won\n", tt, win==0?'O':'X');
			continue;
		}
		
		if(dot){
			printf("Case #%d: Game has not completed\n", tt);
		}
		else{
			printf("Case #%d: Draw\n", tt);
		}
	}
	return 0;
}