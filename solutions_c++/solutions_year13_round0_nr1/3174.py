#include<iostream>
char X[4][4];
using namespace std;

bool checkrow(char c)
{
for(int i=0;i<4;i++)
{
	if((X[i][0]==c||X[i][0]=='T')&&(X[i][1]==c||X[i][1]=='T')&&(X[i][2]==c||X[i][2]=='T')&&(X[i][3]==c||X[i][3]=='T'))
		return true;
}
return false;
}
bool checkcol(char c)
{
	for(int i=0;i<4;i++)
		if((X[0][i]==c||X[0][i]=='T')&&(X[1][i]==c||X[1][i]=='T')&&(X[2][i]==c||X[2][i]=='T')&&(X[3][i]==c||X[3][i]=='T'))
		return true;
	return false;
}
bool checkdiag(char c)
{
if((X[0][0]=='T'||X[0][0]==c)&&(X[1][1]=='T'||X[1][1]==c)&&(X[2][2]=='T'||X[2][2]==c)&&(X[3][3]=='T'||X[3][3]==c))
	return true;
if((X[0][3]=='T'||X[0][3]==c)&&(X[1][2]=='T'||X[1][2]==c)&&(X[2][1]=='T'||X[2][1]==c)&&(X[3][0]=='T'||X[3][0]==c))
	return true;
return false;
}

bool checkdraw()
{
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
			if(X[i][j]=='.')
				return false;
	}
	return true;
}

int main()
{
	int T,C=1;

	cin>>T;
	while(T--)
	{
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>X[i][j];
			}
		}
		int i;
		for(i=0;i<4;i++)
			if(checkrow('X'))
				break;
			if(i!=4)
			{
				cout<<"Case #"<<C<<": X won\n";
				C++;
				continue;
			}
		for(i=0;i<4;i++)
			if(checkcol('X'))
				break;
			if(i!=4)
			{
				cout<<"Case #"<<C<<": X won\n";
				C++;
				continue;
			}
		for(i=0;i<4;i++)
			if(checkdiag('X'))
				break;
			if(i!=4)
			{
				cout<<"Case #"<<C<<": X won\n";
				C++;
				continue;
			}
		for(i=0;i<4;i++)
			if(checkrow('O'))
				break;
			if(i!=4)
			{
				cout<<"Case #"<<C<<": O won\n";
				C++;
				continue;
			}
		for(i=0;i<4;i++)
			if(checkcol('O'))
				break;
			if(i!=4)
			{
				cout<<"Case #"<<C<<": O won\n";
				C++;
				continue;
			}
		for(i=0;i<4;i++)
			if(checkdiag('O'))
				break;
			if(i!=4)
			{
				cout<<"Case #"<<C<<": O won\n";
				C++;
				continue;
			}
		if(checkdraw())
		{
			cout<<"Case #"<<C<<": Draw\n";
			C++;
		}
		else
		{
			cout<<"Case #"<<C<<": Game has not completed\n";
			C++;
		}


	}
}