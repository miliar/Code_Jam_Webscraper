#include <iostream>

using namespace std;
typedef long long llong;

int n,m;
char board[100][100];
int put(int i,int j) {
	if (i>=n-1||j>=m-1)
		return 0;
	return (board[i][j]=='#'&&board[i+1][j]=='#'&&board[i][j+1]=='#'&&board[i+1][j+1]=='#');
}
int main(){

	int NN;cin>>NN;
	for(int MM=1;MM<=NN;MM++){
		cin>>n>>m;
		for (int i=0;i<n;i++)
			cin>>board[i];
		int pos=1;
		for (int i=0;i<n&&pos;i++)
			for (int j=0;j<m&&pos;j++)
				if(board[i][j]=='#') {
					if (!put(i,j))
						pos=0;
					else {
						board[i][j]=board[i+1][j+1]='/';
						board[i+1][j]=board[i][j+1]='\\';
					}
				}

		cout<<"Case #"<<MM<<":"<<endl;
		if (!pos)
			cout<<"Impossible"<<endl;
		else {
			for (int i=0;i<n;i++)
				cout<<board[i]<<endl;
		}
	}
	return 0;
}