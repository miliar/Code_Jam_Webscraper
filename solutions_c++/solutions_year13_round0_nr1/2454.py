#include <stdio.h>
#include <cassert>
#include <iostream>

using namespace std;

#define JUDGE 1

int main(){
	
	if(JUDGE){
		freopen("input","r",stdin);
		freopen("output","w",stdout);
	}
	
	int t;
	scanf("%d%*c",&t);
	char board[10][10];
	for(int tt=1;tt<=t;tt++){
		char winner='A';
		for(int i=0;i<4;i++){
			scanf("%s",board[i]);
			//fprintf(stdout,"%s\n",board[i]);
		}
		
		bool isempty=false;
		bool haswon=true;
		
		//Row Check
		for(int i=0;i<4;i++){
			
			char c=board[i][0];
			haswon=true;
			
			for(int j=0;j<4;j++){
				if(board[i][j]=='.')
					isempty=true;
				
				if(board[i][j]=='.'){
					haswon=false;
					break;
				}
				
				if(board[i][j] == 'T')
					continue;
					
				if(c=='T' && board[i][j] != 'T'){
					c=board[i][j];
					continue;
				}
				
				if(board[i][j] != c){
					haswon=false;
					break;
				}
			}
			if(haswon){
				winner=c;
				break;
			}
		}
		
		//Column Check
		
		if( !haswon){
			
			for(int j=0;j<4;j++){
			
				char c=board[0][j];
				haswon=true;
				
				for(int i=0;i<4;i++){
					
					if(board[i][j]=='T')
						continue;
					
					if(board[i][j]=='.'){
						haswon=false;
						break;
					}
					
					if(c == 'T' && board[i][j] !='T'){
						c=board[i][j];
						continue;
					}
					
					if(board[i][j] != c){
						haswon = false;
						break;
					}
				}
				if(haswon){
					winner=c;
					break;
				}
			}
			
		}
		
		// Main diagonal check
		if( !haswon){
			char c=board[0][0];
			haswon=true;
			for(int i=0;i<4;i++){
				if(board[i][i]=='T')
					continue;
				
				if(board[i][i]=='.'){
					haswon=false;
					break;
				}
				
				if(c=='T' && board[i][i] !='T'){
					c=board[i][i];
					continue;
				}
				
				if(board[i][i] != c){
					haswon=false;
					break;
				}
			}
			
			if(haswon){
				winner=c;
			}
		}
		
		//Other diagonal check
		
		if( !haswon){
			char c=board[3][0];
			haswon=true;
			for(int i=3;i>=0;i--){
				if(board[i][3-i]=='T')
					continue;
				
				if(board[i][3-i]=='.'){
					haswon=false;
					break;
				}
				
				if(c=='T' && board[i][3-i] !='T'){
					c=board[i][3-i];
					continue;
				}
				
				if(board[i][3-i] != c){
					haswon=false;
					break;
				}
			}
			
			if(haswon){
				winner=c;
			}
		}
			
		if(haswon){
			printf("Case #%d: %c won\n",tt,winner);
		}
		else{
			if(isempty){
				printf("Case #%d: Game has not completed\n",tt);
			}
			else {
				printf("Case #%d: Draw\n",tt);
			}
		}
		char temp[10];
		gets(temp);
	}
	return 0;
}