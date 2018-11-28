#include <cstdio>
#include <algorithm>
#include <string>

using namespace std;

#define rep(i,n) for(int i=0;i<n;i++)

char mat[10][10];

string result(int r){return (r==1)?("X won"):("O won");}
int check(int a,int b,int c){
	if (a+c>=4) return 1;
	if (b+c>=4) return -1;
	return 0;
}
string solve() {
	int r,a,b,c;
	rep(i,4) scanf("%s",mat[i]);
	rep(i,4){
		a=b=c=0;
		rep(j,4) a+=(mat[i][j]=='X'),b+=(mat[i][j]=='O'),c+=(mat[i][j]=='T');
		if (r=check(a,b,c)) return result(r);
		a=b=c=0;
		rep(j,4) a+=(mat[j][i]=='X'),b+=(mat[j][i]=='O'),c+=(mat[j][i]=='T');
		if (r=check(a,b,c)) return result(r);
	}
	a=b=c=0;
	rep(i,4) a+=(mat[i][i]=='X'),b+=(mat[i][i]=='O'),c+=(mat[i][i]=='T');
	if (r=check(a,b,c)) return result(r);
	a=b=c=0;
	rep(i,4) a+=(mat[i][3-i]=='X'),b+=(mat[i][3-i]=='O'),c+=(mat[i][3-i]=='T');
	if (r=check(a,b,c)) return result(r);
	rep(i,4) rep(j,4) if (mat[i][j]=='.') return "Game has not completed";
	return "Draw";
}

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int T,i;
	for (scanf("%d",&T),i=1;i<=T;i++){
		printf("Case #%d: %s\n",i,solve().c_str());
	}
	return 0;
}
