#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int N;
	char checkArr[4][4];
	bool xwon, owon, draw, incomplete;

	in >> N;

	for(int i = 0; i < N; i ++)
	//this for loop cycles through all cases
	{
		//resets all useful variables
		xwon = false, owon = false, draw = false, incomplete = false;

		for(int j = 0; j < 4; j++)
		{
			for(int k = 0; k < 4; k++)
			//these for loops puts one case into checkArr
			{
				in >> checkArr[j][k];
			}
		}

		//checks for X-victory
		for(int j = 0; j < 4; j++)
		{
			if( (checkArr[j][0]=='X' || checkArr[j][0]=='T')
				&& (checkArr[j][1]=='X' || checkArr[j][1]=='T') 
				&& (checkArr[j][2]=='X' || checkArr[j][2]=='T')
				&& (checkArr[j][3]=='X' || checkArr[j][3]=='T') )
			//checks for victory by four in a row
				xwon = true;
			if( (checkArr[0][j]=='X' || checkArr[0][j]=='T')
				&& (checkArr[1][j]=='X' || checkArr[1][j]=='T') 
				&& (checkArr[2][j]=='X' || checkArr[2][j]=='T')
				&& (checkArr[3][j]=='X' || checkArr[3][j]=='T') )
			//checks for victory by four in a collumn
				xwon = true;
		}
		if( (checkArr[0][0]=='X' || checkArr[0][0]=='T')
			&& (checkArr[1][1]=='X' || checkArr[1][1]=='T') 
			&& (checkArr[2][2]=='X' || checkArr[2][2]=='T')
			&& (checkArr[3][3]=='X' || checkArr[3][3]=='T') )
		//checks for victory by first diagonal
			xwon = true;
		if( (checkArr[0][3]=='X' || checkArr[0][3]=='T')
			&& (checkArr[1][2]=='X' || checkArr[1][2]=='T') 
			&& (checkArr[2][1]=='X' || checkArr[2][1]=='T')
			&& (checkArr[3][0]=='X' || checkArr[3][0]=='T') )
		//checks for victory by second diagonal
			xwon = true;

		//checks for O-victory
		for(int j = 0; j < 4; j++)
		{
			if( (checkArr[j][0]=='O' || checkArr[j][0]=='T')
				&& (checkArr[j][1]=='O' || checkArr[j][1]=='T') 
				&& (checkArr[j][2]=='O' || checkArr[j][2]=='T')
				&& (checkArr[j][3]=='O' || checkArr[j][3]=='T') )
			//checks for victory by four in a row
				owon = true;
			if( (checkArr[0][j]=='O' || checkArr[0][j]=='T')
				&& (checkArr[1][j]=='O' || checkArr[1][j]=='T') 
				&& (checkArr[2][j]=='O' || checkArr[2][j]=='T')
				&& (checkArr[3][j]=='O' || checkArr[3][j]=='T') )
			//checks for victory by four in a collumn
				owon = true;
		}
		if( (checkArr[0][0]=='O' || checkArr[0][0]=='T')
			&& (checkArr[1][1]=='O' || checkArr[1][1]=='T') 
			&& (checkArr[2][2]=='O' || checkArr[2][2]=='T')
			&& (checkArr[3][3]=='O' || checkArr[3][3]=='T') )
		//checks for victory by first diagonal
			owon = true;
		if( (checkArr[0][3]=='O' || checkArr[0][3]=='T')
			&& (checkArr[1][2]=='O' || checkArr[1][2]=='T') 
			&& (checkArr[2][1]=='O' || checkArr[2][1]=='T')
			&& (checkArr[3][0]=='O' || checkArr[3][0]=='T') )
		//checks for victory by second diagonal
			owon = true;

		//checks for completeness
		if(!xwon && !owon)
		{
			for(int j = 0; j < 4; j++)
			{
				for(int k = 0; k < 4; k++)
				//these for loops puts one case into checkArr
				{
					if(checkArr[j][k] == '.')
					{
						incomplete = true;
						break;
					}
				}
			}
		}

		if(xwon)
			out << "Case #" << i+1 << ": X won" << endl;
		else if(owon)
			out << "Case #" << i+1 << ": O won" << endl;
		else if(incomplete)
			out << "Case #" << i+1 << ": Game has not completed" << endl;
		else 
			out << "Case #" << i+1 << ": Draw" << endl;
	}
}