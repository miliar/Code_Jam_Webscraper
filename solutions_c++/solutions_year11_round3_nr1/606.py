
//Problem A. Square Tiles

#include <iostream>

using namespace std;

int n;

int r,c;
char grid[51][51];

int compute(){
	int i,j,k;
	for (i=0;i<r;i++){
		for (j=0;j<c;j++){
			if (grid[i][j]=='#'){
				if (grid[i+1][j]=='#' && grid[i][j+1]=='#' && grid[i+1][j+1]=='#'){
					grid[i][j]='/';
					grid[i][j+1]='\\';
					grid[i+1][j]='\\';
					grid[i+1][j+1]='/';
				}else {
					return 0;
				}
			}
		}
	}
	return 1;
}

int main(){
	int t;
	int i,j,k;
	int result;

	cin>>t;
	for (i=0;i<t;i++){
		cin>>r>>c;
		memset(grid,0,sizeof(char)*51*51);
		for (j=0;j<r;j++){
			for (k=0;k<c;k++){
				cin>>grid[j][k];
			}
		}
		result=compute();
		cout<<"Case #"<<(i+1)<<":"<<endl;
		if (result){
			//print grid
			for (j=0;j<r;j++){
				for (k=0;k<c;k++){
					cout<<grid[j][k];
				}
				cout<<endl;
		}
		}else {
			cout<<"Impossible"<<endl;
		}
	}
}
