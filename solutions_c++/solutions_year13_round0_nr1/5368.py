#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <deque>
#include <utility>
using namespace std;


bool Won(pair<int,int> T,char simb,vector<string> b)
{
	b[T.first][T.second]=simb;
		for(int j=0;j<4;++j)
			if(b[j][0]==simb && b[j][1]==simb && b[j][2]==simb && b[j][3]==simb)
			return true;

	
	

		for(int j=0;j<4;++j)
			if(b[0][j]==simb && b[1][j]==simb && b[2][j]==simb && b[3][j]==simb)
			return true;
	
	if(b[0][0]==simb && b[1][1]==simb && b[2][2]==simb && b[3][3]==simb)
		return true;
	if(b[0][3]==simb && b[1][2]==simb && b[2][1]==simb && b[3][0]==simb)
		return true;
	return false;
}




int main()
{
	
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int T;
	pair<int,int> Tindex;
	vector<string> board(5);
	for(int i=0;i<5;++i)
		board[i].resize(5);
	cin>>T;
	for(int k=1;k<=T;++k)
	{
		bool OK=false;
		bool point=false;
		for(int i=0;i<4;++i)
		{
			cin>>board[i];
		}
		for(int i=0;i<4;++i)
		{
			if(board[i].find('.')!=-1)
			{
				point=true;
			}
			if(board[i].find('T')!=-1)
			{
				Tindex.first=i;
				Tindex.second=board[i].find('T');
			}
		}
		if(!OK && Won(Tindex,'X',board))
		{
			cout<<"Case #"<<k<<": X won"<<endl;
			OK=true;
		}
		if(!OK && Won(Tindex,'O',board))
		{
			cout<<"Case #"<<k<<": O won"<<endl;
			OK=true;
		}
		if(!OK && point)
		{
			cout<<"Case #"<<k<<": Game has not completed"<<endl;
			bool OK=true;
		}
		if(!OK && !point)
			cout<<"Case #"<<k<<": Draw"<<endl;
	}
	return 0;
}
