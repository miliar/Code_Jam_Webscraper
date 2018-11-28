#include <iostream>
#include <cstdio>
using namespace std;

char Table[5][5];
bool Win(char);
bool Unfinished();

int main(){
	int T;
	scanf("%d",&T);
	for(int Case=1; Case<=T; Case++){
		getchar();
		for(int i=0; i<4; i++)
			scanf("%s",Table[i]);
		printf("Case #%d: ",Case);
		if(Win('X')) printf("X won\n");
		else if(Win('O')) printf("O won\n");
		else if(Unfinished()) printf("Game has not completed\n");
		else printf("Draw\n");
	}
	return 0;
}

bool Win(char c){
	bool Ans=false;
	//row
	for(int i=0; i<4; i++){
		bool ans=true;
		for(int j=0; j<4; j++)
			if(Table[i][j]!=c && Table[i][j]!='T'){ans=false; break;}
		if(ans){Ans=true; break;}
	}
	//column
	if(!Ans)
		for(int i=0; i<4; i++){
			bool ans=true;
			for(int j=0; j<4; j++)
				if(Table[j][i]!=c && Table[j][i]!='T'){ans=false; break;}
			if(ans){Ans=true; break;}
		}
	//diagonal
	if(!Ans){
		bool ans=true;
		for(int i=0; i<4; i++)
			if(Table[i][i]!=c && Table[i][i]!='T'){ ans=false; break;}
		if(ans) Ans=true;
		else{
			ans=true;
			for(int i=0; i<4; i++)
				if(Table[3-i][i]!=c && Table[3-i][i]!='T'){ ans=false; break; }
			if(ans) Ans=true;
		}
	}
	return Ans;
}

bool Unfinished(){
	bool ans=false;
	for(int i=0; i<4; i++){
		for(int j=0; j<4; j++){
			if(Table[i][j]=='.'){
				ans=true;
				break;
			}
		}
		if(ans) break;
	}
	return ans;
}

