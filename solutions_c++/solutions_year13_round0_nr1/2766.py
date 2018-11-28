#include <cstdio>
#define fr(i, a, b) for(int i = (a); i < (b); ++i)

using namespace std;

char grid[10][10];

int winner(){
	int qntO, qntX;
	bool ok;
	bool temPonto = false;
	fr(i, 0, 4){
		qntO = qntX = 0;
		ok = true;
		fr(j, 0, 4){
			if(grid[i][j]=='O') qntO++;
			else if(grid[i][j]=='X') qntX++;
			else if(grid[i][j]=='.') { ok = false; temPonto = true; break; }
		}
		if(ok){
			if(!qntO) return 1;
			else if(!qntX) return 0;
		}
	}
	fr(i, 0, 4){
		qntO = qntX = 0;
		ok = true;
		fr(j, 0, 4){
			if(grid[j][i]=='O') qntO++;
			else if(grid[j][i]=='X') qntX++;
			else if(grid[j][i]=='.') { ok = false; temPonto = true; break; }
		}
		if(ok){
			if(!qntO) return 1;
			else if(!qntX) return 0;
		}
	}
	qntO = qntX = 0;
	ok = true;
	fr(i, 0, 4){
		if(grid[i][i]=='O') qntO++;
		else if(grid[i][i] == 'X') qntX++;
		else if(grid[i][i]== '.' ) { ok = false; temPonto = true; break; }
	}
	if(ok){
		if(!qntO) return 1;
		else if(!qntX) return 0;
	}
	qntO = qntX = 0;
	ok = true;
	fr(i, 0, 4){
		if(grid[i][3-i]=='O') qntO++;
		else if(grid[i][3-i] == 'X') qntX++;
		else if(grid[i][3-i]== '.' ) { ok = false; temPonto = true; break; }
	}
	if(ok){
		if(!qntO) return 1;
		else if(!qntX) return 0;
	}
	if(temPonto) return -1;
	else return 2;
}

int main(){
	int TC;
	scanf("%d", &TC);
	for(int cases = 1; TC--; ++cases){
		fr(i, 0, 4) scanf("%s", grid[i]);
		int aux = winner();
		if(aux==1) printf("Case #%d: X won\n", cases);
		else if(aux==0) printf("Case #%d: O won\n", cases);
		else if(aux==-1) printf("Case #%d: Game has not completed\n", cases);
		else printf("Case #%d: Draw\n", cases);
	}
	return 0;
}