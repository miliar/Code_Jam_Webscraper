#include<iostream>
#include<fstream>
using namespace std;
char a[10][10];
bool fun(char ch)
{
	if((a[0][0]==ch || a[0][0]=='T') && (a[0][1]==ch || a[0][1]=='T') && (a[0][2]==ch || a[0][2]=='T') && (a[0][3]==ch || a[0][3]=='T'))return true;

	if((a[0][0]==ch || a[0][0]=='T') && (a[1][1]==ch || a[1][1]=='T') && (a[2][2]==ch || a[2][2]=='T') && (a[3][3]==ch || a[3][3]=='T'))return true;

	if((a[1][0]==ch || a[1][0]=='T') && (a[1][1]==ch || a[1][1]=='T') && (a[1][2]==ch || a[1][2]=='T') && (a[1][3]==ch || a[1][3]=='T'))return true;

	if((a[2][0]==ch || a[2][0]=='T') && (a[2][1]==ch || a[2][1]=='T') && (a[2][2]==ch || a[2][2]=='T') && (a[2][3]==ch || a[2][3]=='T'))return true;

	if((a[3][0]==ch || a[3][0]=='T') && (a[3][1]==ch || a[3][1]=='T') && (a[3][2]==ch || a[3][2]=='T') && (a[3][3]==ch || a[3][3]=='T'))return true;

	if((a[0][0]==ch || a[0][0]=='T') && (a[1][0]==ch || a[1][0]=='T') && (a[2][0]==ch || a[2][0]=='T') && (a[3][0]==ch || a[3][0]=='T'))return true;

	if((a[0][1]==ch || a[0][1]=='T') && (a[1][1]==ch || a[1][1]=='T') && (a[2][1]==ch || a[2][1]=='T') && (a[3][1]==ch || a[3][1]=='T'))return true;

	if((a[0][2]==ch || a[0][2]=='T') && (a[1][2]==ch || a[1][2]=='T') && (a[2][2]==ch || a[2][2]=='T') && (a[3][2]==ch || a[3][2]=='T'))return true;

	if((a[0][3]==ch || a[0][3]=='T') && (a[1][3]==ch || a[1][3]=='T') && (a[2][3]==ch || a[2][3]=='T') && (a[3][3]==ch || a[3][3]=='T'))return true;

	if((a[0][3]==ch || a[0][3]=='T') && (a[1][2]==ch || a[1][2]=='T') && (a[2][1]==ch || a[2][1]=='T') && (a[3][0]==ch || a[3][0]=='T'))return true;

	return false;
}

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("ans.txt");
	int i,j,k,t;
	fin>>t;
	for(k=1;k<=t;k++){
		bool flg=0;
		for(i=0;i<4;i++){
			fin>>a[i];
			for(j=0;j<4;j++)if(a[i][j]=='.')flg=1;
		}
		if(fun('X'))fout<<"Case #"<<k<<": X won"<<endl;
		else if(fun('O'))fout<<"Case #"<<k<<": O won"<<endl;
		else if(flg==1)fout<<"Case #"<<k<<": Game has not completed"<<endl;
		else fout<<"Case #"<<k<<": Draw"<<endl;
	}
	return 0;
}
				
