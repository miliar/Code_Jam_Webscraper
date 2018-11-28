//#include<stdio>
#include<iostream>
using namespace std;

void replace();

int main(){
	int T;		//Total number of test cases
//	cout<<"Enter total number of test cases\t";
	cin>>T;
	for (int i=1;i<=T;i++){
		cout<<"Case #"<<i<<":\n";
		replace();
	}
	return 0;
}

void replace(){
	int R=0,C=0,i,j;
	cin>>R>>C;
	char mat[R][C];
	for(i=0;i<R;i++){
		for(j=0;j<C;j++){
			cin>>mat[i][j];		
		}
	}
	for(i=0;i<R-1;i++){
		for(j=0;j<C-1;j++){
			if(mat[i][j]=='#'){
				if(mat[i][j+1]=='#' && mat[i+1][j]=='#' && mat[i+1][j+1]=='#'){
					mat[i][j]='/';		mat[i+1][j+1]='/';
					mat[i][j+1]='\\';	mat[i+1][j]='\\';		
				}
				else{
					cout<<"Impossible"<<endl;;
					return;
				}
			}
				 
		}
	}

	for(j=0;j<C;j++)
		if(mat[R-1][j]=='#')
			{cout<<"Impossible"<<endl;return;}
	for(i=0;i<R;i++)
		if(mat[i][C-1]=='#')
			{cout<<"Impossible"<<endl;	return;}
	for(i=0;i<R;i++){
		for(j=0;j<C;j++){
			cout<<mat[i][j];
		}
		cout<<endl;
	}

	

}
