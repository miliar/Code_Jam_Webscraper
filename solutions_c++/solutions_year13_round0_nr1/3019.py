#include <cstdio>
#include <cstdlib>
#include <string>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <utility>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <iostream>

#define ln printf("\n")
typedef long long ll;

#define fr(a,b,c) for(int a = b; a < c; a++)
#define rep(a,b) fr(a,0,b)

#define dbg(x) cerr << #x << " = " << x << endl
#define db dbg
#define _  << " , " <<

using namespace std;

const double eps = 1e-8;
int n;

int cn = 1;
char mat[11][11];

bool checkline(char p, int l){
	int t = 0;
	int cont = 0;
	
	rep(i,4) {
		if(mat[l][i] == 'T') t++;
		if(mat[l][i] == p) cont++;
	}
	
	if(t == 1 && cont == 3) return true;
	if(cont == 4) return true;
	return false;
}

bool checkcolumn(char p, int c){
	int t = 0;
	int cont = 0;
	
	rep(i,4) {
		if(mat[i][c] == 'T') t++;
		if(mat[i][c] == p) cont++;
	}
	
	if(t == 1 && cont == 3) return true;
	if(cont == 4) return true;
	return false;
}

bool checkdiagonal(char p, int start, int dif){
	int t = 0;
	int cont = 0;

	rep(i,4) {
		if(mat[i][start+i*dif] == 'T') t++;
		if(mat[i][start+i*dif]  == p) cont++;
	} 
	
	if(t == 1 && cont == 3) return true;
	if(cont == 4) return true;
	return false;
}

bool draw(){
	rep(i,4) rep(j,4) if(mat[i][j] == '.') return false;
	return true;
}

bool win(char p){
	rep(i,4){
		if(checkline(p,i)) return true;
		if(checkcolumn(p,i)) return true;
	}
	
	if(checkdiagonal(p, 0, 1)) return true;
	if(checkdiagonal(p, 3, -1)) return true;
	
	return false;
}

bool read(){
	rep(i,4) scanf("%s", mat[i]);
	
	return true;
}

void process(){
	//rep(i,4) printf("%s\n", mat[i]);
	printf("Case #%d: ", cn++);
	if(win('X')) printf("X won\n");
	else if(win('O')) printf("O won\n");
	else if(draw()) printf("Draw\n");
	else printf("Game has not completed\n");
}

int main(){	
	int t = -1;
	scanf("%d", &t);
	
	while(t-- && read()){		
		process();
	}	
	
	return 0;
}
