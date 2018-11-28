#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <iostream>
#include <string>

using namespace std;

string row;
int ax[10], ao[10]; //row 0-3 , col 4+ 0-3, diag 
int n;

int main(){
	
	scanf("%d\n",&n);
	int tc;
	for(tc=1;tc<=n;tc++){
	
		for(int i = 0 ; i < 10; i++){
			ax[i]=0;
			ao[i]=0;
		}
		
		int dot = 0;
		
		for(int i = 0 ; i <4; i++){
			getline(cin,row);
			for(int j=0; j<4;j++){
				
				if(row[j]=='X'){
					ax[i] += 1;
					ax[4+j]+=1;
				}
				else if(row[j]=='O'){
					ao[i] += 1;
					ao[4+j]+=1;
				}
				else if(row[j]=='T'){
					ax[i] += 1;
					ax[4+j]+=1;
					ao[i] += 1;
					ao[4+j]+=1;
				}
				else dot++;
				
				if(i==j){
					if(row[j]=='X'){
						ax[8] += 1;
					}
					else if(row[j]=='O'){
						ao[8] += 1;
					}
					else if(row[j]=='T'){
						ax[8] += 1;
						ao[8] += 1;
					}
				}
				
				if(i+j==3){
					if(row[j]=='X'){
						ax[9] += 1;
					}
					else if(row[j]=='O'){
						ao[9] += 1;
					}
					else if(row[j]=='T'){
						ax[9] += 1;
						ao[9] += 1;
					}	
				}
			}	
		}
		
		getline(cin,row);
					
		cout << "Case #" << tc << ": "; 
		int winner = 0;
		for(int i=0;i<10;i++){
			if(ax[i]==4){
				winner = 1;
				break;
			}else if(ao[i]==4){
				winner = 2;
				break;
			}
		}
		
		if(winner == 0){
			if(dot > 0) cout << "Game has not completed" << endl;
			else cout << "Draw" << endl;
		}else if(winner == 1){
			cout << "X won" <<endl;
		}else{
			cout << "O won" <<endl;
		}
		
	}
		
	return 0;
}