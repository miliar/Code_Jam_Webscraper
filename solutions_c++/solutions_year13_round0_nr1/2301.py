#include <stdio.h>
#include <string>
#include <set>
using namespace std;
char B[10][10];

bool finished(void){
	for(int i=0;i<4;++i){
		for(int j=0;j<4;++j){
			if(B[i][j]=='.'){
				return false;
			}
		}
	}
	return true;
}

char check(set<char> &S){
	if(S.find('.')!=S.end()){
		return '.';
	}
	if(S.find('X')!=S.end()){
		if(S.find('O')!=S.end()){
			return '.';
		}
		return 'X';
	}
	return 'O';
}

char winnerH(int r){
	set<char> S;
	for(int c=0;c<4;++c){
		S.insert(B[r][c]);
	}
	return check(S);
	
}
char winnerV(int c){
	set<char> S;
	for(int r=0;r<4;++r){
		S.insert(B[r][c]);
	}
	return check(S);
}

char winnerD1(void){
	set<char> S;
	for(int i=0;i<4;++i){
		S.insert(B[i][i]);
	}
	return check(S);
}

char winnerD2(void){
	set<char> S;
	for(int i=0;i<4;++i){
		S.insert(B[i][3-i]);
	}
	return check(S);
}



string getStatus(void){
	for(int i=0;i<4;++i){
		char c=winnerH(i);
		if(c=='.'){
			c=winnerV(i);
		}
		if(c!='.'){
			return (string("")+c)+" won";
		}
	}
	char c=winnerD1();
	if(c!='.'){
		return (string("")+c)+" won";
	}
	c=winnerD2();
	if(c!='.'){
		return (string("")+c)+" won";
	}
	if(finished()){
		return "Draw";
	}
	return "Game has not completed";
}

void print(void){
	printf("****\n");
	for(int i=0;i<4;++i){
		printf("%s\n", B[i]);
	}
	printf("****\n");
}
int main(int argc, char *argv[]){
	int T;
	scanf("%d\n", &T);
	for(int c=1;c<=T;++c){
		for(int i=0;i<4;++i){
			scanf("%s\n", B[i]);
		}
		//print();
		string sol=getStatus();
		printf("Case #%d: %s\n", c, sol.c_str());
	}
	return 0;
	
}

