#include<iostream>
#include<stack>
#include<string.h>
#define t(a) (a=='B'?1:2)
#define seP(a,b,c) (0<=(a) && (a)<n && 0<=(b) && (b)<n && board[a][b]==c)
using namespace std;

int cas,n,k;
short board[50][50];
short qu[50];
string s;

short mov[4][2] = {{0,1},{1,0},{1,1},{1,-1}};

bool b,r;

void check2(int ii, int jj, int kk, int tokken, int ll){
	if(kk>=k){
		if(tokken == 1)
			b = true;
		else
			r = true;
		return;
	}
	if(seP(ii+mov[ll][0], jj+mov[ll][1], tokken))
		check2(ii+mov[ll][0], jj+mov[ll][1], kk+1, tokken, ll);
}


void check(int ii, int jj, int kk, int tokken){
	if(kk>=k){
		if(tokken == 1)
			b = true;
		else
			r = true;
		return;
	}
	for(int ll=0;ll<4;ll++)
		if(seP(ii+mov[ll][0], jj+mov[ll][1], tokken))
			check2(ii+mov[ll][0], jj+mov[ll][1], kk+1, tokken, ll);
}



int main(){
	cin >> cas;
	for(int caso = 1 ; caso <= cas ; caso++ ){
		cin >> n >> k;
		memset(board, 0, sizeof board);
		memset(qu, 0, sizeof qu);
		b = r = false;

		for(int i=0;i<n;i++){
			cin >> s;
			for(int j=s.size()-1;j>=0;j--)
				if(s[j]!='.')
					board[n - 1 - (qu[n-i-1]++) ][n - i - 1] = t(s[j]);
		}

		for(int i=0;i<n;i++)
			for(int j=0;j<n && !(b&&r);j++){
				if(!b && seP(i,j,1))
					check(i,j,1,1);
				if(!r && seP(i,j,2))
					check(i,j,1,2);
			}
	
		cout << "Case #" << caso << ": ";
		if(b&&r)
			cout << "Both" << endl;
		else if(b || r)
			cout << (b?"Blue":"Red") << endl;
		else
			cout << "Neither" << endl;		
	}

}
