#include <iostream>
#include <string>
#include <iostream>
#include <iostream>
#include <iostream>
#include <iostream>

using namespace std;

#define rep(i,n) for( int i = 0; i < (n); i++ )


char mpp [4][4];

string solve(){
	rep(i,4) rep(j,4) cin>>mpp[i][j];


	int t1 = 0, t2 = 0, tt = 0;
	int emp = 0;
	rep(i,4){
		t1 = t2 = tt = 0;
		rep(j,4){
			if( mpp[i][j]=='T' ) tt++;
			else if( mpp[i][j]=='O' ) t1++;
			else if( mpp[i][j]=='X' ) t2++;
			else emp++;
		}
		if( t1+tt==4 ) return "O won";
		else if( t2+tt==4 ) return "X won";
	}
	

	rep(j,4){
		t1 = t2 = tt = 0;
		rep(i,4){
			if( mpp[i][j]=='T' ) tt++;
			else if( mpp[i][j]=='O' ) t1++;
			else if( mpp[i][j]=='X' ) t2++;
		}
		if( t1+tt==4 ) return "O won";
		else if( t2+tt==4 ) return "X won";
	}
	

	t1 = t2 = tt = 0;
	for( int i = 0, j = 0; i < 4; i++, j++ ){
		if( mpp[i][j]=='T' ) tt++;
		else if( mpp[i][j]=='O' ) t1++;
		else if( mpp[i][j]=='X' ) t2++;
	}
	if( t1+tt==4 ) return "O won";
	else if( t2+tt==4 ) return "X won";

	t1 = t2 = tt = 0;
	for( int i = 0, j = 3; i < 4; i++, j-- ){
		if( mpp[i][j]=='T' ) tt++;
		else if( mpp[i][j]=='O' ) t1++;
		else if( mpp[i][j]=='X' ) t2++;
	}
	if( t1+tt==4 ) return "O won";
	else if( t2+tt==4 ) return "X won";


	if(emp==0) return "Draw";
	return "Game has not completed";
}

int main(){

	freopen("A.txt", "r", stdin);	freopen("A.out", "w", stdout);


	int T;
	scanf("%d", &T);

	for( int i = 0; i < T; i++ ){
		printf("Case #%d: ", i+1);
		cout<<solve()<<endl;
	}

}