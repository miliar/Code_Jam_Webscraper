#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <fstream>
using namespace std;
ofstream output;
void linewinner(string s)
{
	int i;
	int X=0,O=0;
	for(i=0;i<4;i++)
		{
			if(s[i]=='X')X++;
			if(s[i]=='O')O++;
			if(s[i]=='T'){X++;O++;}
		}
	if(X==4)output<<"X won";
	if(O==4)output<<"O won";

}
bool linewins(string s)
{
	int i;
	int X=0,O=0;
	for(i=0;i<4;i++)
		{
			if(s[i]=='X')X++;
			if(s[i]=='O')O++;
			if(s[i]=='T'){X++;O++;}
		}
	if(X==4 or O==4)return true;
	return false;
}
void linewinner(char* s)
{
	int i;
	int X=0,O=0;
	for(i=0;i<4;i++)
		{
			if(s[i]=='X')X++;
			if(s[i]=='O')O++;
			if(s[i]=='T'){X++;O++;}
		}
	if(X==4)output<<"X won";
	if(O==4)output<<"O won";

}
bool linewins(char* s)
{
	int i;
	int X=0,O=0;
	for(i=0;i<4;i++)
		{
			if(s[i]=='X')X++;
			if(s[i]=='O')O++;
			if(s[i]=='T'){X++;O++;}
		}
	if(X==4 or O==4)return true;
	return false;
}

void getwinner(vector<string> board)
{
	int dots=0;
	int i,j;
	char temp[4];
	for(i=0;i<4;i++)
		if(linewins(board[i])){linewinner(board[i]);return;}
	for(i=0;i<4;i++)
		{for(j=0;j<4;j++)
			temp[j]=board[j][i];
		if(linewins(temp)){linewinner(temp);return;}}
	for(i=0;i<4;i++)temp[i]=board[i][i];
	if(linewins(temp)){linewinner(temp);return;}
	for(i=0;i<4;i++)temp[i]=board[i][3-i];
	if(linewins(temp)){linewinner(temp);return;}
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			if(board[i][j]=='.')dots++;
	if(dots==0){output<<"Draw";return;}
	
	output<<"Game has not completed";
}
int main()
{
	int t,tt=1;
	ifstream input;
	input.open("A-large.in");
	output.open("result.txt");
	input>>t;
	while(t--)
	{
		vector<string>b;
		string temp;
		int i,j;
		for(i=0;i<4;i++)
		{
			input>>temp;
			b.push_back(temp);
		}
		output<<"Case #"<<tt++<<": ";
		getwinner(b);
		output<<endl;

	}
	output.close();
	return 0;
}