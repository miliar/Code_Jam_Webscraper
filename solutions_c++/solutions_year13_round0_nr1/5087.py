#include <iostream>
#include <deque>
#include <fstream>
#include <set>

#define VI			deque<int>

#define REP(i,a,b)	for(i=(int)a ; i<=(int)b ; i++)
#define FOR(i,N)	REP(i,0,N-1)

using namespace std;

char B[4][4];

bool XWon(){
	int i,j;
	FOR(i,4){
		FOR(j,4) if(B[i][j]=='.' || B[i][j]=='O') break;
		if(j==4) return true;
		FOR(j,4) if(B[j][i]=='.' || B[j][i]=='O') break;
		if(j==4) return true;
	}
	FOR(i,4) if(B[i][i]=='.' || B[i][i]=='O') break;
	if(i==4) return true;
	FOR(i,4) if(B[i][3-i]=='.' || B[i][3-i]=='O') break;
	if(i==4) return true;
	return false;
}

bool OWon(){
	int i,j;
	FOR(i,4){
		FOR(j,4) if(B[i][j]=='.' || B[i][j]=='X') break;
		if(j==4) return true;
		FOR(j,4) if(B[j][i]=='.' || B[j][i]=='X') break;
		if(j==4) return true;
	}
	FOR(i,4) if(B[i][i]=='.' || B[i][i]=='X') break;
	if(i==4) return true;
	FOR(i,4) if(B[i][3-i]=='.' || B[i][3-i]=='X') break;
	if(i==4) return true;
	return false;
}

bool Draw(){
	int i,j;
	FOR(i,4) FOR(j,4) if(B[i][j]=='.') return false;
	return true;
}

int main(){
	ifstream cin("input.txt");
	ofstream cout("a2.out");
	int T,t;
	cin >> T;
	REP(t,1,T){
		int i,j;
		FOR(i,4) FOR(j,4) cin >> B[i][j];

		cout <<"Case #"<<t<<": ";
		if(XWon()) cout <<"X won"<<endl;
		else if(OWon()) cout <<"O won"<<endl;
		else if(Draw()) cout <<"Draw"<<endl;
		else cout <<"Game has not completed"<<endl;
	}
}
