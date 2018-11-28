#include<iostream.h>
#include<stdio.h>
#include<conio.h>
#include<fstream.h>


int main()
{
   int test;
   ifstream myfile;
   myfile.open("example2.in");
   myfile >>test ;
   cout<<test;
   bool Owon,Xwon,ecb,fin;
	int i,j;
	char tictac[4][4];
   ofstream yourfile("ouptut1.txt");
	for(int c=0;c<test;c++)
	{
		ecb=false;
		fin=false;
		for(i=0;i<4;i++)
		{
				for(j=0;j<4;j++)
				{
            myfile>>tictac[i][j];
					if(tictac[i][j]=='.') ecb=true;
				}
		}
		for(i=0;i<4;i++)
		{
			Owon=true;
			Xwon=true;
			for(j=0;j<4;j++)
			{
				if(tictac[i][j]!='X'&&tictac[i][j]!='T') Xwon=false;
				if(tictac[i][j]!='O'&&tictac[i][j]!='T') Owon=false;
			}
			if(Owon||Xwon)
			{
				fin=true;
				break;
			}
		}
		if(!fin) for(j=0;j<4;j++)
		{
			Owon=true;
			Xwon=true;
			for(i=0;i<4;i++)
			{
				if(tictac[i][j]!='X'&&tictac[i][j]!='T') Xwon=false;
				if(tictac[i][j]!='O'&&tictac[i][j]!='T') Owon=false;
			}
			if(Owon||Xwon)
			{
				fin=true;
				break;
			}
		}
		if(!fin)
		{
			Owon=true;
			Xwon=true;
			 for(j=0;j<4;j++)
			{
				if(tictac[j][j]!='X'&&tictac[j][j]!='T') Xwon=false;
				if(tictac[j][j]!='O'&&tictac[j][j]!='T') Owon=false;
			}
			if(Owon||Xwon)
				fin=true;
		}
		if(!fin)
		{
			Owon=true;
			Xwon=true;
			if(!fin) for(j=0;j<4;j++)
			{
				if(tictac[j][3-j]!='X'&&tictac[j][3-j]!='T') Xwon=false;
				if(tictac[j][3-j]!='O'&&tictac[j][3-j]!='T') Owon=false;
			}
			if(Owon||Xwon)
				fin=true;
		}
		if(Owon)
         yourfile<<"Case #"<<c+1<<": O won\n";
		else if(Xwon)
         yourfile<<"Case #"<<c+1<<": X won\n";
		else if(ecb)
         yourfile<<"Case #"<<c+1<<": Game has not completed\n";
		else
         yourfile<<"Case #"<<c+1<<": Draw\n";

	}
getch();
}