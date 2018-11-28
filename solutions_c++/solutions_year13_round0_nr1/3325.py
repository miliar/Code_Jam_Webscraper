#include<string.h>
#include<iostream>
using namespace std;

struct boards{
	char l[4][5];
	char status[25];
};

char check_board(boards brd)
{
	//CHECKING THE DIAGONALS
	char checkl = brd.l[0][0];
	if(checkl == 'T')
		checkl = brd.l[1][1];
	bool flagl = false;
	if(checkl != '.')
	{
		for (int i=1;i<4;++i)
			if(checkl != brd.l[i][i])
				if(brd.l[i][i] == 'T')
					continue;
				else
					{flagl = true;
					break;}
		if(!flagl)
			return checkl;
	}
	
	char checkr = brd.l[0][3];
	if(checkr == 'T')
		checkr = brd.l[1][2];
	bool flagr = false;
	if(checkr != '.')
	{
		for (int i=1;i<4;++i)
			if(checkr != brd.l[i][3-i])
				if(brd.l[i][3-i] == 'T')
					continue;
				else
					{flagr = true;
					break;}
		if(!flagr)
			return checkr;
	}
	//CHECKED THE DIAGONALS
	
	//CHECK COLS
	for (int i=0; i<4; ++i)
	{
		char checkc = brd.l[0][i];
		if(checkc == 'T')
			checkc = brd.l[1][i];
		bool flagc = false;
		if(checkc != '.')
		{
			for (int j=1;j<4;++j)
				if(checkc != brd.l[j][i])
					if(brd.l[j][i] == 'T')
						continue;
					else
						{flagc = true;
						break;}
			if(!flagc)
				return checkc;
		}
	}
	
	//CHECK ROWS
	for (int i=0; i<4; ++i)
	{
		char checkR = brd.l[i][0];
		if(checkR == 'T')
			checkR = brd.l[i][1];
		bool flagR = false;
		if(checkR != '.')
		{
			for (int j=1;j<4;++j)
				if(checkR != brd.l[i][j])
					if(brd.l[i][j] == 'T')
						continue;
					else
						{flagR = true;
						break;}
			if(!flagR)
				return checkR;
		}
	}
	
	//CHECK FOR DRAW
	for (int i=0; i<4; ++i)
		for (int j=0; j<4; ++j)
		{
			if(brd.l[i][j] == '.')
			 	return 'N';
		}
	return 'D';
	
}

int main()
{
	int T;
	cin>>T;
	boards brd[T];
	
	for (int i = 0; i<T; ++i)
		for (int lin=0; lin<4; ++lin)
			cin>>brd[i].l[lin];
			
	char win = '.';
	
	for (int i = 0; i<T; ++i)
		{win = check_board(brd[i]);
		if(win == 'N')
			strcpy(brd[i].status,": Game has not completed");
		if(win == 'D')
			strcpy(brd[i].status,": Draw");
		if(win == 'O')
			strcpy(brd[i].status,": O won");
		if(win == 'X')
			strcpy(brd[i].status,": X won");
		}

/*	for (int i = 0; i<T; ++i)
		{
		cout<<brd[i].l[0]<<'\n';
				cout<<"kacham boochaam\n";
		cout<<brd[i].l[1]<<'\n';
				cout<<"kacham boochaam\n";
		cout<<brd[i].l[2]<<'\n';
				cout<<"kacham boochaam\n";
		cout<<brd[i].l[3]<<'\n';
		}	
*/
	
	for (int i = 0; i<T; ++i)
		cout<<"Case #"<<i+1<<brd[i].status<<'\n';
}


