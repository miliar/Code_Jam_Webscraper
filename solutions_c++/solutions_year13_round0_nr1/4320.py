#include<iostream>
using namespace std;
//#define DEBUG
bool checkRow(char arr[4][4], char c)
{
	#ifdef DEBUG
		cout<<"checking rows for "<<c;
	#endif
	
	char mat[4][4];
	for(int i=0; i<4; i++) {
		for(int j=0; j<4; j++) {	
			if(arr[i][j] == 'T')
				mat[i][j] = c;
			else
				mat[i][j] = arr[i][j];
		}
	}
		
	for(int i=0; i<4; i++) {	
		for(int j=0; j<4; j++){
		#ifdef DEBUG
			cout<<mat[i][j];
		#endif
			if(mat[i][j] != c)
				break;
			if(j==3) return true;
		}
		#ifdef DEBUG
			cout<<endl;
		#endif
	}
	return false;
}
	
bool checkCol(char arr[4][4], char c)
{
	char mat[4][4];
	for(int i=0; i<4; i++) {
		for(int j=0; j<4; j++) {	
			if(arr[i][j] == 'T')
				mat[i][j] = c;
			else
				mat[i][j] = arr[i][j];
		}
	}
	
	#ifdef DEBUG
		cout<<"checking cols for "<<c;
	#endif
	for(int j=0; j<4; j++) {	
		for(int i=0; i<4; i++){
			#ifdef DEBUG
				cout<<mat[i][j];
			#endif
			if(mat[i][j] != c)
				break;
			if(i==3) return true;
		}
		#ifdef DEBUG
			cout<<endl;
		#endif
	}
	return false;
}

bool checkDiag(char arr[4][4], char c)
{
	char mat[4][4];
	for(int i=0; i<4; i++) {
		for(int j=0; j<4; j++) {	
			if(arr[i][j] == 'T')
				mat[i][j] = c;
			else
				mat[i][j] = arr[i][j];
		}
	}
	
	#ifdef DEBUG
		cout<<"checking diags for "<<c;
	#endif
	
	for(int i=0; i<4; i++) {
		if(mat[i][i]!=c) break;
		if(i==3) return true;
	}
	
	for(int i=0, j=3; i<4; i++, j--) {
		if( mat[i][j]!=c )break;
		if(i==3) return true;
	}
	
	return false;
}

bool checkNoDot(char mat[4][4]) 
{
	for(int i=0; i<4; i++)
		for(int j=0; j<4; j++)
			if(mat[i][j] == '.')
				return false;
	
	return true;
}

bool checkWin(char mat[4][4], char c)
{
	if(checkRow(mat, c)) return true;
	if(checkCol(mat, c)) return true;
	if(checkDiag(mat, c)) return true;
	return false;
}


	
int main() 
{
	freopen("ip.txt", "r", stdin);
	freopen("op.txt", "w", stdout);
	int t;
	cin>>t;
	for(int tc=1; tc<=t; tc++) {
		char mat[4][4];
		for(int i=0; i<4; i++) {			
			for(int j=0; j<4; j++) {
				cin>>mat[i][j];	
				#ifdef DEBUG
					cout<<mat[i][j];
				#endif
			}
			#ifdef DEBUG
				cout<<endl;
			#endif
	}
		
		if(checkWin(mat, 'X')) {
			cout<<"Case #"<<tc<<": X won"<<endl;
			continue;
		}
		else if(checkWin(mat, 'O')) {
			cout<<"Case #"<<tc<<": O won"<<endl;
			continue;
		}
		else if(checkNoDot(mat)) {
			cout<<"Case #"<<tc<<": Draw"<<endl;
			continue;
		}
		else 
			cout<<"Case #"<<tc<<": Game has not completed"<<endl;
	}
	return 0;
}	