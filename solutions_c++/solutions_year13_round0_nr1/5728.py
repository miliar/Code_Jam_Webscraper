using namespace std;
#include<iostream.h>
#include<fstream.h>
#include<conio.h>
#include<string.h>
int main()
{
//clrscr();
ifstream file;
file.open("inputA.txt");
int T;
char row1[11][4];
char row2[11][4];
char row3[11][4];
char row4[11][4];

while(!file.eof())
{
file>>T;
	for(int x=1;x<=T;x++)
	{
		file>>row1[x]>>row2[x]>>row3[x]>>row4[x];

		if(((row1[x][0]=='O' || row1[x][0]=='T') && (row1[x][1]=='O' || row1[x][1]=='T') && (row1[x][2]=='O' || row1[x][2]=='T') && (row1[x][3]=='O' || row1[x][3]=='T')) || ((row2[x][0]=='O' || row2[x][0]=='T') && (row2[x][1]=='O' || row2[x][1]=='T') && (row2[x][2]=='O' || row2[x][2]=='T') && (row2[x][3]=='O' || row2[x][3]=='T')) || ((row3[x][0]=='O' || row3[x][0]=='T') && (row3[x][1]=='O' || row3[x][1]=='T') && (row3[x][2]=='O' || row3[x][2]=='T') && (row3[x][3]=='O' || row3[x][3]=='T')) || ((row4[x][0]=='O' || row4[x][0]=='T') && (row4[x][1]=='O' || row4[x][1]=='T') && (row4[x][2]=='O' || row4[x][2]=='T') && (row4[x][3]=='O' || row4[x][3]=='T')))
			cout<<"Case #"<<x<<": O won"<<endl;
			
		else if(((row1[x][0]=='X' || row1[x][0]=='T') && (row1[x][1]=='X' || row1[x][1]=='T') && (row1[x][2]=='X' || row1[x][2]=='T') && (row1[x][3]=='X' || row1[x][3]=='T')) || ((row2[x][0]=='X' || row2[x][0]=='T') && (row2[x][1]=='X' || row2[x][1]=='T') && (row2[x][2]=='X' || row2[x][2]=='T') && (row2[x][3]=='X' || row2[x][3]=='T')) || ((row3[x][0]=='X' || row3[x][0]=='T') && (row3[x][1]=='X' || row3[x][1]=='T') && (row3[x][2]=='X' || row3[x][2]=='T') && (row3[x][3]=='X' || row3[x][3]=='T')) || ((row4[x][0]=='X' || row4[x][0]=='T') && (row4[x][1]=='X' || row4[x][1]=='T') && (row4[x][2]=='X' || row4[x][2]=='T') && (row4[x][3]=='X' || row4[x][3]=='T')))
			cout<<"Case #"<<x<<": X won"<<endl;
			
		else if(((row1[x][0]=='X' || row1[x][0]=='T') && (row2[x][0]=='X' || row2[x][0]=='T') && (row3[x][0]=='X' || row3[x][0]=='T') && (row4[x][0]=='X' || row4[x][0]=='T')) || ((row1[x][1]=='X' || row1[x][1]=='T') && (row2[x][1]=='X' || row2[x][1]=='T') && (row3[x][1]=='X' || row3[x][1]=='T') && (row4[x][1]=='X' || row4[x][1]=='T')) || ((row1[x][2]=='X' || row1[x][2]=='T') && (row2[x][2]=='X' || row2[x][2]=='T') && (row3[x][2]=='X' || row3[x][2]=='T') && (row4[x][2]=='X' || row4[x][2]=='T')) || (row1[x][3]=='X' || row1[x][3]=='T') && (row2[x][3]=='X' || row2[x][3]=='T') && (row3[x][3]=='X' || row3[x][3]=='T') && (row4[x][3]=='X' || row4[x][3]=='T'))
			cout<<"Case #"<<x<<": X won"<<endl;
			
		else if(((row1[x][0]=='O' || row1[x][0]=='T') && (row2[x][0]=='O' || row2[x][0]=='T') && (row3[x][0]=='O' || row3[x][0]=='T') && (row4[x][0]=='O' || row4[x][0]=='T')) || ((row1[x][1]=='O' || row1[x][1]=='T') && (row2[x][1]=='O' || row2[x][1]=='T') && (row3[x][1]=='O' || row3[x][1]=='T') && (row4[x][1]=='O' || row4[x][1]=='T')) || ((row1[x][2]=='O' || row1[x][2]=='T') && (row2[x][2]=='O' || row2[x][2]=='T') && (row3[x][2]=='O' || row3[x][2]=='T') && (row4[x][2]=='O' || row4[x][2]=='T')) || (row1[x][3]=='O' || row1[x][3]=='T') && (row2[x][3]=='O' || row2[x][3]=='T') && (row3[x][3]=='O' || row3[x][3]=='T') && (row4[x][3]=='O' || row4[x][3]=='T'))
			cout<<"Case #"<<x<<": O won"<<endl;
			
		else if(((row1[x][0]=='X' || row1[x][0]=='T') && (row2[x][1]=='X' || row2[x][1]=='T') && (row3[x][2]=='X' || row3[x][2]=='T') && (row4[x][3]=='X' || row4[x][3]=='T')) || ((row1[x][3]=='X' || row1[x][3]=='T') && (row2[x][2]=='X' || row2[x][2]=='T') && (row3[x][1]=='X' || row3[x][1]=='T') && (row4[x][0]=='X' || row4[x][0]=='T')))
			cout<<"Case #"<<x<<": X won"<<endl;
			
		else if(((row1[x][0]=='O' || row1[x][0]=='T') && (row2[x][1]=='O' || row2[x][1]=='T') && (row3[x][2]=='O' || row3[x][2]=='T') && (row4[x][3]=='O' || row4[x][3]=='T')) || ((row1[x][3]=='O' || row1[x][3]=='T') && (row2[x][2]=='O' || row2[x][2]=='T') && (row3[x][1]=='O' || row3[x][1]=='T') && (row4[x][0]=='O' || row4[x][0]=='T')))
			cout<<"Case #"<<x<<": O won"<<endl;
			
		else if(row1[x][0]=='.' || row1[x][1]=='.' || row1[x][2]=='.' || row1[x][3]=='.' || row2[x][0]=='.' || row2[x][1]=='.' || row2[x][2]=='.' || row2[x][3]=='.' || row3[x][0]=='.' || row3[x][1]=='.' || row3[x][2]=='.' || row3[x][3]=='.' || row4[x][0]=='.' || row4[x][1]=='.' || row4[x][2]=='.' || row4[x][3]=='.')
			cout<<"Case #"<<x<<": Game has not completed"<<endl;
		else
			cout<<"Case #"<<x<<": Draw"<<endl;
		
	}

       getch();
       return 0;

	}
}

