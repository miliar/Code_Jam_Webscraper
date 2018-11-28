#include<iostream>
#include<fstream>
using namespace std;
char* board[4];
bool isIncomplete()
{

for(int i=0;i<4;i++)
	for(int j=0;j<4;j++)
			{
			if(board[i][j]=='.')
			return true;
			}
return false;
}
char checkRow()
{
	char temp;
	int i,j;
	for(i=0;i<4;i++)
	{
		temp=board[i][0];
		j=1;
		if(temp=='.')
			continue;
		if(temp=='T')
			{	
			temp=board[i][1];
			j=2;
			if(temp=='.')
				continue;
			}

		
		for(;j<4;j++)
			{
				if(board[i][j]!=temp && board[i][j]!='T')
				{
					temp='n';
					break;
				}
			}
		if(temp!='n')
			return(temp);
	
	}
	return('n');
}
char checkCol()
{
	char temp;
	int i,j;
	for(i=0;i<4;i++)
	{	
		temp=board[0][i];
		j=1;
		if(temp=='.')
			continue;
		if(temp=='T')
			{	
			temp=board[1][i];
			j=2;
			if(temp=='.')
			continue;
			}
		
		for(;j<4;j++)
			{
				if(board[j][i]!=temp && board[j][i]!='T')
				{
					temp='n';
					break;
				}
			}
		if(temp!='n')
			return(temp);
	
	}
	return('n');
}
char checkDiag()
{
	int i;
	char temp;
	for(int j=0;j<2;j++)
	{
	temp=board[0][3*j];
	i=1;
	if(temp=='.')
	continue;
	if(temp=='T')
			{	
			temp=board[1][j+1];
			i=2;
			if(temp=='.')
			continue;
			}
	for(;i<4;i++)
	{
		if(temp!=board[i][i+3*j-2*i*j] && board[i][i+3*j-2*i*j]!='T')
		{
		temp='n';
		break;
		}
		
	}
	if(temp!='n')
			return temp;
	}
	return('n');
}
void main()
{
board[0]=new char[10];
board[1]=new char[10];
board[2]=new char[10];
board[3]=new char[10];
char temp[20];
char winner;
int T;
ifstream iff;
ofstream off;
iff.open("C:\\Users\\him\\Desktop\\GOOGLE\\A-small-attempt0.in");
off.open("C:\\Users\\him\\Desktop\\GOOGLE\\output.txt");
iff.getline(board[0],9);
T=atoi(board[0]);
cout<<T<<"\n";

for(int i=0;i<T;i++)
{
	for(int j=0;j<4;j++)
	{
	iff.getline(board[j],9);
	}
	iff.getline(temp,10);
	
	if((winner=checkRow())!='n')
	{
		off<<"Case #"<<i+1<<": "<<winner<<" won\n";
		cout<<"Case #"<<i+1<<": "<<winner<<" won\n";
	}
	else if((winner=checkCol())!='n')
	{
		off<<"Case #"<<i+1<<": "<<winner<<" won\n";
		cout<<"Case #"<<i+1<<": "<<winner<<" won\n";
	}
	else if((winner=checkDiag())!='n')
	{
		off<<"Case #"<<i+1<<": "<<winner<<" won\n";
		cout<<"Case #"<<i+1<<": "<<winner<<" won\n";
	}
	else if(isIncomplete())
	{
		off<<"Case #"<<i+1<<": Game has not completed\n";
		cout<<"Case #"<<i+1<<": Game has not completed\n";
	}
	else
	{
		off<<"Case #"<<i+1<<": "<<"Draw\n";
		cout<<"Case #"<<i+1<<": "<<"Draw\n";
	}
	
	
	
	
	/*
	cout<<board[0]<<"\n";
	cout<<board[1]<<"\n";
	cout<<board[2]<<"\n";
	cout<<board[3]<<"\n";*/
	
}

iff.close();
off.close();
system("pause");
}