#include<fstream>
#include<iostream>
char game[4][4];
int checkx();
int checko();
int isempty();
using namespace std;
int main()
{
	char ch;
	int i,j;
	int T,ref;
	int x,o,e;	
	ifstream fin;
	ofstream fout;
	fin.open("input.in",ios::in);
	fout.open("output",ios::out);
	fin>>T;
	fin.get(ch);
	
	
	for(ref=0;ref<T;ref++)
	{

	
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
		fin.get(game[i][j]);
		}
		fin.get(ch);
	}
	fin.get(ch);
	
	fout<<"Case #"<<ref+1<<": ";
	x=0; o=0; e=0;
	x=checkx();
	if(x==1) { cout<<"X won\n"; fout<<"X won\n"; continue; }
	o=checko();
	if(o==1) { cout<<"O won\n"; fout<<"O won\n"; continue; }
	e=isempty();
	if(e==1) { cout<<"Game has not completed\n"; fout<<"Game has not completed\n"; }
	else { cout<<"Draw\n"; fout<<"Draw\n"; }
	}

fin.close();
fout.close();

}

int checkx()
{
	int i,j;
	int flag;
	for(i=0;i<4;i++)
	{
		flag=0;
		for(j=0;j<4;j++)	
		{
		if(game[i][j]=='X') flag++;
		else if(game[i][j]=='T') flag++;
		}
		if(flag==4) return 1;
	}
	
	for(i=0;i<4;i++)						
	{								
		flag=0;
		for(j=0;j<4;j++)	
		{
		if(game[j][i]=='X') flag++;
		else if(game[j][i]=='T') flag++;
		}
		if(flag==4) return 1;					
	}								

	flag=0;
	for(i=0;i<4;i++)
	{
	if(game[i][i]=='X') flag++;
	else if(game[i][i]=='T') flag++;
	}
	if(flag==4) return 1;

	flag=0;
	for(i=0;i<4;i++)
	{
	if(game[i][3-i]=='X') flag++;
	else if(game[i][3-i]=='T') flag++;
	}
	if(flag==4) return 1;

	return 0;

}



int checko()
{
	int i,j;
	int flag;
	for(i=0;i<4;i++)						
	{
		flag=0;
		for(j=0;j<4;j++)	
		{
		if(game[i][j]=='O') flag++;
		else if(game[i][j]=='T') flag++;
		}
		if(flag==4) return 1;
	}
	
	for(i=0;i<4;i++)						
	{								
		flag=0;
		for(j=0;j<4;j++)	
		{
		if(game[j][i]=='O') flag++;
		else if(game[j][i]=='T') flag++;
		}
		if(flag==4) return 1;					
	}								

	flag=0;
	for(i=0;i<4;i++)
	{
	if(game[i][i]=='O') flag++;
	else if(game[i][i]=='T') flag++;
	}
	if(flag==4) return 1;

	flag=0;
	for(i=0;i<4;i++)
	{
	if(game[i][3-i]=='O') flag++;
	else if(game[i][3-i]=='T') flag++;
	}
	if(flag==4) return 1;

	return 0;

}

int isempty()
{
	int i,j;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
		if(game[i][j]=='.') return 1;
		}
	}
	return 0;
}
