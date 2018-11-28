#include <cstdio>
#include <algorithm>
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,1,n+1)
char board[4][4];
void check(int t){
	FOR(y,0,4){
		bool X_win=true;
		bool O_win=true;
		FOR(x,0,4){
			if(board[y][x]=='.'){X_win=false;O_win=false;}
			if(board[y][x]=='X'){O_win=false;}
			if(board[y][x]=='O'){X_win=false;}
		}
		if(X_win){printf("Case #%d: X won\n",t);return;}
		if(O_win){printf("Case #%d: O won\n",t);return;}
	}
	FOR(x,0,4){
		bool X_win=true;
		bool O_win=true;
		FOR(y,0,4){
			if(board[y][x]=='.'){X_win=false;O_win=false;}
			if(board[y][x]=='X'){O_win=false;}
			if(board[y][x]=='O'){X_win=false;}
		}
		if(X_win){printf("Case #%d: X won\n",t);return;}
		if(O_win){printf("Case #%d: O won\n",t);return;}
	}
	bool X_win=true;
	bool O_win=true;
	FOR(z,0,4){
		if(board[z][z]=='.'){X_win=false;O_win=false;}
		if(board[z][z]=='X'){O_win=false;}
		if(board[z][z]=='O'){X_win=false;}
	}
	if(X_win){printf("Case #%d: X won\n",t);return;}
	if(O_win){printf("Case #%d: O won\n",t);return;}
	X_win=true;
	O_win=true;
	FOR(z,0,4){
		if(board[3-z][z]=='.'){X_win=false;O_win=false;}
		if(board[3-z][z]=='X'){O_win=false;}
		if(board[3-z][z]=='O'){X_win=false;}
	}
	if(X_win){printf("Case #%d: X won\n",t);return;}
	if(O_win){printf("Case #%d: O won\n",t);return;}
	bool complete=true;
	FOR(y,0,4){
		FOR(x,0,4){
			if(board[y][x]=='.')complete=false;
		}
	}
	if(complete){printf("Case #%d: Draw\n",t);return;}
	if(!complete){printf("Case #%d: Game has not completed\n",t);return;}
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
    int T;scanf("%d",&T);
	REP(t,T){
		
		FOR(i,0,4){
			scanf("\n");
			FOR(j,0,4){
				scanf("%c",&board[i][j]);
			}
		}
		check(t);
	}
}	