#include <iostream>
#include <fstream>
using namespace std;
int n,Case,i,j,Xwin,Owin,X,T,O,D;
char a[5][5],ch;
void judge(){
	if(X==4||(X==3&&T==1)) Xwin=1;
	if(O==4||(O==3&&T==1)) Owin=1;
}
int main(){
	ofstream cout ("A-large.out");
	ifstream cin ("A-large.in");
	cin >> n;
	for(Case=1;Case<=n;++Case){
		for(i=1;i<=4;++i) for(j=1;j<=4;++j) cin >> a[i][j];
		Xwin=Owin=D=0;
		for(i=1;i<=4;++i){
			X=T=O=0;
			for(j=1;j<=4;++j){
				if(a[i][j]=='X') ++X;
				if(a[i][j]=='T') ++T;
				if(a[i][j]=='O') ++O;
				if(a[i][j]=='.') ++D;
			}
			judge();
			X=T=O=0;
			for(j=1;j<=4;++j){
				if(a[j][i]=='X') ++X;
				if(a[j][i]=='T') ++T;
				if(a[j][i]=='O') ++O;
				if(a[j][i]=='.') ++D;
			}
			judge();
		}
		X=T=O=0;
		for(i=1;i<=4;++i){
			if(a[i][i]=='X') ++X;
			if(a[i][i]=='T') ++T;
			if(a[i][i]=='O') ++O;
			if(a[i][i]=='.') ++D;
		}
		judge();
		X=T=O=0;
		for(i=1;i<=4;++i){
			if(a[i][4-i+1]=='X') ++X;
			if(a[i][4-i+1]=='T') ++T;
			if(a[i][4-i+1]=='O') ++O;
			if(a[i][4-i+1]=='.') ++D;
		}
		judge();
		cout << "Case #" << Case << ": ";
		if(Xwin) cout << "X won" << endl;
		else if(Owin) cout << "O won" << endl;
		else if(D) cout << "Game has not completed" << endl;
		else cout << "Draw" << endl;
	}
	return 0;
}
