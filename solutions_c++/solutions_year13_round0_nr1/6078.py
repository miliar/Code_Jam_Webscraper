#include <fstream>
#include <string>
#include <iostream>
using namespace std;

int main()
{
	int x,trigger1=0, trigger2=0,trigger3=0,draw;
	const char *temp;
	char **board;
	FILE *output;
	output = fopen("Output.txt","w");
	string input,input2;
	fstream filestr;
	filestr.open("A-large.in",fstream::in);
	getline(filestr,input);
	int tcase = atoi(input.c_str());
	
	for ( int i =0 ; i < tcase ; i++ ) 
	{
		draw = 0;
		board = new char *[4];
		for ( int j = 0; j < 4 ; j++)
			board[j] = new char [4];
		for ( int j = 0 ; j < 4 ; j ++ )
		{
			getline(filestr,input2);
			temp = input2.c_str();
			strcpy(board[j],temp);
		}
			getline(filestr,input2);

		cout<<"Board "<<i+1<<endl<<board[0]<<endl<<board[1]<<endl<<board[2]<<endl<<board[3]<<endl;
			
		for ( int j = 0; j < 4 ; j++ )
		{
			for ( int k = 0; k < 4 ; k++ )
			{
				if ( board[j][k] == 'X' || board[j][k] == 'T') trigger1++;
				if ( board[j][k] == 'O' || board[j][k] == 'T') trigger2++;				
			}
			if (trigger1 == 4 ) trigger3 = 1;
			if (trigger2 == 4 ) trigger3 = 2;
			trigger1 = 0;
			trigger2 = 0;
		}
		

		for ( int j = 0; j < 4 ; j++ )
		{
			for ( int k = 0; k < 4 ; k++ )
			{
				if ( board[k][j] == 'X' || board[k][j] == 'T') trigger1++;
				if ( board[k][j] == 'O' || board[k][j] == 'T') trigger2++;	
			}
			if (trigger1 == 4 ) trigger3 = 1;
			if (trigger2 == 4 ) trigger3 = 2;
			trigger1 = 0;
			trigger2 = 0;
		}
		
		for ( int k = 0; k < 4 ; k++ )
		{
			if ( board[k][k] == 'X' || board[k][k] == 'T') trigger1++;
			if ( board[k][k] == 'O' || board[k][k] == 'T') trigger2++;				
		}
		if (trigger1 == 4 ) trigger3 = 1;
		if (trigger2 == 4 ) trigger3 = 2;
		trigger1 = 0;
		trigger2 = 0;
		x=3;
		for ( int j = 0; j < 4 ; j++)
		{
			
			if ( board[x][j] == 'X' || board[x][j] == 'T') trigger1++;
			if ( board[x][j] == 'O' || board[x][j] == 'T') trigger2++;	
			x--;
		}
		if (trigger1 == 4 ) trigger3 = 1;
		if (trigger2 == 4 ) trigger3 = 2;
		trigger1 = 0;
		trigger2 = 0;

		if ( trigger3 == 1 ) fprintf(output,"Case #%d: X won\n", i+1);
		if ( trigger3 == 2 ) fprintf(output,"Case #%d: O won\n", i+1);
		if ( trigger3 == 0 ) 
		{
			for ( int j =0; j < 4 ; j++ )
			{
				for ( int k =0; k <4; k++ )
				{
					if ( board[j][k] == '.')
						draw = 1;
				}
			}
			if ( draw == 1 ) fprintf(output,"Case #%d: Game has not completed\n",i+1);
			if ( draw == 0 ) fprintf(output,"Case #%d: Draw\n",i+1);
		}
		trigger3 = 0;
	}
	
	fclose(output);
	filestr.close();
	return 0;
}