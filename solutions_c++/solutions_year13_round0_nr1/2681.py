//============================================================================
// Name        : TicTac.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>
#include <iostream>
using namespace std;
char winner='.';
bool empty=false;
bool checkdiag(char * field){
	int O=0;
	int X=0;
	int O2=0;
	int X2=0;
	for (int i = 0; i < 4; ++i) {
		char c=field[i*4+i];
		if(c=='T'){
			X++;O++;
		}else if(c=='X'){
			X++;
		}else if(c=='O'){
			O++;
		}
		c=field[i*4+(3-i)];
		if(c=='T'){
			X2++;O2++;
		}else if(c=='X'){
			X2++;
		}else if(c=='O'){
			O2++;
		}
	}
	if(O==4){
		winner='O';
		return true;
	}
	if(X==4){
		winner='X';
		return true;
	}
	if(O2==4){
		winner='O';
		return true;
	}
	if(X2==4){
		winner='X';
		return true;
	}
	return false;
}
bool horizontal(char * field){
	for (int j = 0; j < 16; j+=4) {
			int O=0;
			int X=0;
			for (int i = 0; i < 4; ++i) {
				char c=field[j+i];
				empty=empty|(field[j+i]=='.');
				if(c=='T'){
					X++;O++;
				}else if(c=='X'){
					X++;
				}else if(c=='O'){
					O++;
				}

			}
			if(O==4){
				winner='O';
				return true;
			}
			if(X==4){
				winner='X';
				return true;
			}
		}

		return false;
}
bool vertical(char * field){
	for (int j = 0; j < 4; ++j) {
			int O=0;
			int X=0;
			for (int i = 0; i < 4; ++i) {
				char c=field[j+i*4];
				if(c=='T'){
					X++;O++;
				}else if(c=='X'){
					X++;
				}else if(c=='O'){
					O++;
				}

			}
			if(O==4){
				winner='O';
				return true;
			}
			if(X==4){
				winner='X';
				return true;
			}
		}

		return false;
}
int main() {
	int L, D, N;
	scanf("%d",&N);

	int c=1;
	while(N--){
		char* field=new char[17];
		scanf("%s",field);
		scanf("%s",&(field[4]));
		scanf("%s",&(field[8]));
		scanf("%s",&(field[12]));
		empty=false;
		winner='.';
		checkdiag(field)||horizontal(field)||vertical(field);
		if(winner!='.'){
			printf("Case #%d: %c won\n",c++,winner);
		}else{
			if(empty){
				printf("Case #%d: Game has not completed\n",c++);

			}else{
				printf("Case #%d: Draw\n",c++);
			}
		}
	}

	return 0;
}
