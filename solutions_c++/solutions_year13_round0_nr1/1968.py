#include<iostream>
#include<cstdio>
#include<cstring>
#include<fstream>
using namespace std;
string brd[4];
bool chk_dig(char c)
{
	if((brd[0][0]==c || brd[0][0]=='T') && (brd[1][1]==c || brd[1][1]=='T') && (brd[2][2]==c || brd[2][2]=='T') && (brd[3][3]==c || brd[3][3]=='T'))
		return true;
	if((brd[0][3]==c || brd[0][3]=='T') && (brd[1][2]==c || brd[1][2]=='T') && (brd[2][1]==c || brd[2][1]=='T') && (brd[3][0]==c || brd[3][0]=='T'))
		return true;
	return false;
}
bool chk_row(int i,char c)
{
	if((brd[i][0]==c || brd[i][0]=='T') && (brd[i][1]==c || brd[i][1]=='T') && (brd[i][2]==c || brd[i][2]=='T') && (brd[i][3]==c || brd[i][3]=='T'))
		return true;
	return false;
}
bool chk_clm(int i,char c)
{
	if((brd[0][i]==c || brd[0][i]=='T') && (brd[1][i]==c || brd[1][i]=='T') && (brd[2][i]==c || brd[2][i]=='T') && (brd[3][i]==c || brd[3][i]=='T'))
		return true;
	return false;
}
bool chk_x()
{
	if(chk_dig('X'))
		return true;
	for(int i=0;i<4;i++)
		if(chk_row(i,'X'))
			return true;
	for(int i=0;i<4;i++)
		if(chk_clm(i,'X'))
			return true;
	return false;
}
bool chk_o()
{
	if(chk_dig('O'))
		return true;
	for(int i=0;i<4;i++)
		if(chk_row(i,'O'))
			return true;
	for(int i=0;i<4;i++)
		if(chk_clm(i,'O'))
			return true;
	return false;
}
bool nt_com()
{
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(brd[i][j]=='.')
				return true;
	return false;
}


int main()
{
	ifstream rf("input.txt");
	ofstream wf("result.txt");
	int t;
	rf>>t;
	for(int z=1;z<=t;z++)
	{
		rf.ignore(100,'\n');
		for(int i=0;i<4;i++)
			rf>>brd[i];
		if(chk_x())
			wf<<"Case #"<<z<<": X won\n";
		else if(chk_o())
			wf<<"Case #"<<z<<": O won\n";
		else if(nt_com())
			wf<<"Case #"<<z<<": Game has not completed\n";
		else
			wf<<"Case #"<<z<<": Draw\n";
	}
	
	
	return 0;
}
