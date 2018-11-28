#include<stdio.h>
#include<iostream>
#include<string>
#include<string.h>

using namespace std;

int main(){
	string line1;
	char m[26][2];
	int t,i,j;
	
	m[0][0]='a';
	m[0][1]='y';
	
	m[1][0]='b';
	m[1][1]='h';
	
	m[2][0]='c';
	m[2][1]='e';
	
	m[3][0]='d';
	m[3][1]='s';

	m[4][0]='e';
	m[4][1]='o';
	
	m[5][0]='f';
	m[5][1]='c';
	
	m[6][0]='g';
	m[6][1]='v';
	
	m[7][0]='h';
	m[7][1]='x';
	
	m[8][0]='i';
	m[8][1]='d';
	
	m[9][0]='j';
	m[9][1]='u';
	
	m[10][0]='k';
	m[10][1]='i';
	
	m[11][0]='l';
	m[11][1]='g';
	
	m[12][0]='m';
	m[12][1]='l';
	
	m[13][0]='n';
	m[13][1]='b';
	
	m[14][0]='o';
	m[14][1]='k';
	
	m[15][0]='p';
	m[15][1]='r';
	
	m[16][0]='q';
	m[16][1]='z';
	
	m[17][0]='r';
	m[17][1]='t';
	
	m[18][0]='s';
	m[18][1]='n';
	
	m[19][0]='t';
	m[19][1]='w';
	
	m[20][0]='u';
	m[20][1]='j';
	
	m[21][0]='v';
	m[21][1]='p';
	
	m[22][0]='w';
	m[22][1]='f';
	
	m[23][0]='x';
	m[23][1]='m';
	
	m[24][0]='y';
	m[24][1]='a';
	
	m[25][0]='z';
	m[25][1]='q';
	
	cin>>t;getline(cin, line1);
	
	for (i=0;i<t;i++){
		cout<<"Case #"<<i+1<<": ";
		getline(cin, line1);
		for (j=0;j<line1.length();j++){
			if (line1[j]!=' ')
				cout<<m[(int)line1[j]-97][1];
			else
				cout<<' ';
		}
		cout<<endl;			
	}
	return 0;

}
