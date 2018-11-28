#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <map>
#include <set>
#include <list>
#include <string>
#include <vector>
#include <algorithm>

#define INF 		2000000000ll
#define FOR(i,a,b)	for(int i = a; i < b; i++)
#define MIN(a,b)	({a < b ? a : b;})
#define MAX(a,b)	({a > b ? a : b;})
#define AB(a)		({a < 0 ? -a : a;})
#define EQ(a,b)		({AB(a - b) <= 1e-10 ? true : false;})
#define CL(a)		memset(a,b,sizeof(a))
#define NOT(a)		a = not a

using namespace std;

struct b{
	int x;
	int o;
	int t;
	b(){ x = 0; o = 0; t = 0; }
	void clear() { x = 0; o = 0; t = 0; }
};
char input[4][5];
int judge(b cnt){
	if(cnt.t == 1) {
		if(cnt.x == 3) return 1;
		else if(cnt.o == 3) return 2;
	}
	else {
			if(cnt.x == 4) return 1;
			else if(cnt.o == 4) return 2;
	}
	return 0;
}
int row(int a){
	b cnt;
	FOR(i,0,4){
		if(input[a][i] == 'X') cnt.x++;
		else if(input[a][i] == 'O') cnt.o++;
		else if(input[a][i] == 'T') cnt.t++;
	}
	return judge(cnt);
}
int col(int a){
	b cnt;
	FOR(i,0,4){
		if(input[i][a] == 'X') cnt.x++;
		else if(input[i][a] == 'O') cnt.o++;
		else if(input[i][a] == 'T') cnt.t++;
	}
	return judge(cnt);
}
int diag(){
	b cnt;
	FOR(i,0,4){
		if(input[i][i] == 'X') cnt.x++;
		else if(input[i][i] == 'O') cnt.o++;
		else if(input[i][i] == 'T') cnt.t++;
	}
	int result = judge(cnt);
	if(result != 0) return result;
	cnt.clear();
	FOR(i,0,4) {
		if(input[i][3-i] == 'X') cnt.x++;
		else if(input[i][3-i] == 'O') cnt.o++;
		else if(input[i][3-i] == 'T') cnt.t++;
	}
	return judge(cnt);
}
bool winner(int val){
	if(val == 1) { cout << "X won" << endl; return true; }
	else if(val == 2) { cout << "O won" << endl; return true; }
	else return false;
}
void solve(int num){
	FOR(i,0,4) scanf("%s", input[i]);
	
	cout << "Case #" << (num+1) << ": ";
	FOR(i,0,4) if(winner(row(i) ) ) return ;
	FOR(i,0,4) if(winner(col(i) ) ) return ;
	if(winner(diag() ) ) return ;
	
	FOR(i,0,4) FOR(n,0,4)
		if(input[i][i] == '.') { cout << "Game has not completed" << endl; return ; }
	
	cout << "Draw" << endl;
}
int main(){
	int T;
	
	cin >> T;
	FOR(i,0,T) solve(i);
	return 0;
}