#include <iostream>
#include <cstdio>

using namespace std;

int i,j,k,l,m,n,t;
string s[4];

int win(char ch){
	int i,j;
	for (i=0;i<4;i++){
		int d = 1;
		for (j=0;j<4;j++){
			if (s[i][j]!=ch && s[i][j]!='T'){
				d=0;
				break;				
			}		
		}
		if (d) return 1;
		d = 1;			
		for (j=0;j<4;j++){
			if (s[j][i]!=ch && s[j][i]!='T'){
				d=0;
				break;				
			}		
		}
		if (d) return 1;
	}
	int d = 1;
	for (i=0;i<4;i++)
		if (s[i][i]!=ch && s[i][i]!='T'){
			d=0;
			break;				
		}
	if (d) return 1;
	d = 1;
	for (i=0;i<4;i++)
		if (s[i][3-i]!=ch && s[i][3-i]!='T'){
			d=0;
			break;				
		}
	if (d) return 1;
	return 0;		
}

int main(){
	freopen("output.txt","w",stdout);
	cin>>t;
	for (i=1;i<=t;i++){
		int number = 0;
		for (j=0;j<4;j++){
			cin>>s[j];
			for (k=0;k<4;k++)
				if (s[j][k]=='.') number++;		
		}
		if (win('X'))
			cout<<"Case #"<<i<<": "<<'X'<<" won\n"; else
		if (win('O'))
			cout<<"Case #"<<i<<": "<<'O'<<" won\n"; else
		if (number==0) cout<<"Case #"<<i<<": Draw\n"; else 
			cout<<"Case #"<<i<<": Game has not completed\n"; 
	}
	return 0;
}
