#include<cstdio>
#include<iostream>
#include<cstring>

using namespace std;

int main(){
	int t;
	cin>>t;
	for(int tcno=1;tcno<=t;tcno++){
		char board[4][4];
		char temp;
		scanf("%c",&temp);
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%c",&board[i][j]);
			}
			scanf("%c",&temp);
		}
		int o=0,x=0,d=1,n=0;
		for(int i=0;i<4;i++){
			if( (board[i][0]=='O'||board[i][0]=='T') && (board[i][1]=='O'||board[i][1]=='T') && (board[i][2]=='O'||board[i][2]=='T') && (board[i][3]=='O'||board[i][3]=='T') ){
				o=1;
				break;
			}
			if( (board[i][0]=='X'||board[i][0]=='T') && (board[i][1]=='X'||board[i][1]=='T') && (board[i][2]=='X'||board[i][2]=='T') && (board[i][3]=='X'||board[i][3]=='T') ){
				x=1;
				break;
			}
			
			if( (board[0][i]=='O'||board[0][i]=='T') && (board[1][i]=='O'||board[1][i]=='T') && (board[2][i]=='O'||board[2][i]=='T') && (board[3][i]=='O'||board[3][i]=='T') ){
				o=1;
				break;
			}
			if( (board[0][i]=='X'||board[0][i]=='T') && (board[1][i]=='X'||board[1][i]=='T') && (board[2][i]=='X'||board[2][i]=='T') && (board[3][i]=='X'||board[3][i]=='T') ){
				x=1;
				break;
			}
		}
		
		if( (board[0][0]=='O'||board[0][0]=='T') && (board[1][1]=='O'||board[1][1]=='T') && (board[2][2]=='O'||board[2][2]=='T') && (board[3][3]=='O'||board[3][3]=='T') ){
			o=1;
		}
		if( (board[0][0]=='X'||board[0][0]=='T') && (board[1][1]=='X'||board[1][1]=='T') && (board[2][2]=='X'||board[2][2]=='T') && (board[3][3]=='X'||board[3][3]=='T') ){
			x=1;
		}
		
		if( (board[0][3]=='O'||board[0][3]=='T') && (board[1][2]=='O'||board[1][2]=='T') && (board[2][1]=='O'||board[2][1]=='T') && (board[3][0]=='O'||board[3][0]=='T') ){
			o=1;
		}
		if( (board[0][3]=='X'||board[0][3]=='T') && (board[1][2]=='X'||board[1][2]=='T') && (board[2][1]=='X'||board[2][1]=='T') && (board[3][0]=='X'||board[3][0]=='T') ){
			x=1;
		}
		
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(board[i][j]=='.'){
					d=0;
					break;
				}
			}
		}
		
		if(o==1){
			printf("Case #%d: O won\n",tcno);
		}
		else if(x==1){
			printf("Case #%d: X won\n",tcno);
		}
		else if(d==1){
			printf("Case #%d: Draw\n",tcno);
		}
		else{
			printf("Case #%d: Game has not completed\n",tcno);
		}
	}
}
