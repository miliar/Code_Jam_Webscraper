#include<iostream>
using namespace std;

char mat[4][4];
char msg[4][100]={"X won","O won" ,"Draw", "Game has not completed"};

int won( char w)
{
	int result=0;
	for(int i=0;i<4;i++) {
		if(mat[i][i]==w || mat[i][i]=='T')
			result++;
	}	
	if(result==4)
		return 1;

	result=0;
	for(int i=0;i<4;i++) {
		if(mat[i][3-i]==w || mat[i][3-i]=='T')
			result++;
	}	
	if(result==4)
		return 1;

	for(int j=0;j<4;j++) {
		result=0;
		for(int i=0;i<4;i++) {
			if(mat[i][j]==w || mat[i][j]=='T')
				result++;
		}	
		if(result==4)
			return 1;
	}

	for(int j=0;j<4;j++) {
		result=0;
		for(int i=0;i<4;i++) {
			if(mat[j][i]==w || mat[j][i]=='T')
				result++;
		}	
		if(result==4)
			return 1;
	}
	return 0;

}

int Draw()
{
	int result=0;
	for(int i=0;i<4;i++) {
		for(int j=0;j<4;j++) {
			if(mat[i][j]=='.')
				return 0;
		}
	}
	return 1;	
}


int main()
{
	int t;
	cin>>t;
	
	for(int i=0;i<t;i++) {
		int result=0;
		for(int j=0;j<4;j++) {
			for(int k=0;k<4;k++) {
				cin>>mat[j][k];
			}
		}

		if(won('X')) {
			result=1;
		} else if(won('O')) {
			result=2;
		} else if(Draw()) {
			result=3;
		} else {
			result=4;
		}	
		
		cout<<"Case #"<<i+1<<": "<<msg[result-1]<<"\n";		

	}
	return 0;
}