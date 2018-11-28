#include <iostream>
#include <cstdio>
using namespace std;
#define forn(i,n) for(int i=0; i<(int)(n); i++)
char tab[8][8];

bool CuatroEnLinea(char c){
	//cout<<c<<endl;
	forn(i,4){
		bool tempRes = true;
		forn(j,4)if(tab[i][j]!=c && tab[i][j]!='T')tempRes = false;
		if(tempRes)return true;
	}
	forn(i,4){
		bool tempRes = true;
		forn(j,4)if(tab[j][i]!=c && tab[j][i]!='T')tempRes = false;
		if(tempRes)return true;
	}
	bool tempRes=true;
	forn(i,4)if(tab[i][i]!=c && tab[i][i]!='T')tempRes = false;
	if(tempRes)return true;

	tempRes=true;
	forn(i,4)if(tab[i][3-i]!=c && tab[i][3-i]!='T')tempRes = false;
	if(tempRes)return true;

	return false;
}

int main(){
	int t; cin>>t; int caso = 0;
	while(t>0){
		t--;
		caso++;
		bool falta = false;
		forn(i,4)forn(j,4){
			cin>>tab[i][j];
			if(tab[i][j]=='.')falta=true;
		}
		bool ganoX = false;
		bool ganoO = false;
		ganoX = CuatroEnLinea('X');
		ganoO = CuatroEnLinea('O');
		
		printf("Case #%d: ", caso);
		
		if(ganoX)printf("X won\n");
		else if(ganoO)printf("O won\n");
			else if(falta)printf("Game has not completed\n");
				else printf("Draw\n");
	}
	
}
