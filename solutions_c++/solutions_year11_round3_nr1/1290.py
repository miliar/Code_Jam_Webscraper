#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include <stdlib.h>
using namespace std;
#define fo(A,S,D) for(int A=S;A<D;A++)
int main(int argc, char **argv)
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.out","w",stdout);
	int T,R,C;
	char board[55][55];
	cin>>T;
	fo(t,0,T){
		cin>>R>>C;
		cout<<"Case #"<<t+1<<":\n";
		fo(i,0,R)
			fo(j,0,C)
				cin>>board[i][j];
		int f=1;
		for(int i=0;i<R&&f;i++){
			for(int j=0;j<C&&f;j++){
				if(board[i][j]=='#'){
						if(i+1<R&&j+1<C&&board[i+1][j]=='#'&&board[i][j+1]=='#'&&board[i+1][j+1]=='#'){
							board[i][j]='/';board[i][j+1]='\\';
							board[i+1][j]='\\'; board[i+1][j+1]='/';
						}else{
							cout<<"Impossible\n";f=0;
						}
				}
			}
		}
		if(!f) continue;
		fo(i,0,R){
			fo(j,0,C)
				cout<<board[i][j];
			cout<<endl;
		}
	}
	return 0;
}