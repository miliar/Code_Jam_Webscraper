#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cstdlib>

using namespace std;



int main()
{

	int T;


    ifstream fin("C:\\weilin\\Competition\\codeForces\\CodeJam2013\\CodeJam2013\\A-large.in");

//    ifstream fin("C:\\weilin\\Competition\\codeForces\\CodeJam2013\\CodeJam2013\\test.txt");

     ofstream fout("C:\\weilin\\Competition\\codeForces\\CodeJam2013\\CodeJam2013\\output.txt");

	fin >> T;
    string row[4];
	long long total = 0;
	
    char b[4][4];
	for (int i=0; i <T; i++)
	{
        bool filled = true;
		for (int j=0; j < 4; j++)
		{

			for (int m=0; m < 4; m++)
			{
                char c;
                fin >> c;
                b[j][m] = c;
                if ( c == '.')
				{ filled = false;}
			}
		}
        bool hasWinner = false;
        int co = 0; int cx = 0; int ct= 0;
        for (int m=0; m < 4; m++)
		{
           co = 0; cx = 0; ct = 0;
           for (int n=0; n < 4; n++)
		   {
               char c = b[m][n];
               if (c == 'O')
                   co++;
               if (c == 'X')
                   cx++;
               if (c == 'T')
                   ct ++;
		   }
            if (co == 4 || co + ct == 4)
			{    fout << "Case #" << i+1 <<  ": "<< "O won" << endl; goto nextcase;}
			if (cx == 4 || cx + ct == 4)
			{    fout << "Case #" << i+1 <<  ": "<< "X won" << endl; goto nextcase;}
		}

        for (int m=0; m < 4; m++)
		{
           co = 0; cx = 0; ct = 0;
           for (int n=0; n < 4; n++)
		   {
               char c = b[n][m];
               if (c == 'O')
                   co++;
               if (c == 'X')
                   cx++;
               if (c == 'T')
                   ct ++;
		   }
           if (co == 4 || co + ct == 4)
		   {    fout << "Case #" << i+1 <<  ": "<< "O won" << endl; goto nextcase;}
           if (cx == 4 || cx + ct == 4)
		   {    fout << "Case #" << i+1 <<  ": "<< "X won" << endl; goto nextcase;}
		}

        co = 0; cx = 0; ct = 0;
		for (int m=0; m < 4; m++)
		{
			
			char c = b[m][m];
			if (c == 'O')
				co++;
			if (c == 'X')
				cx++;
			if (c == 'T')
				ct ++;
		}
		if (co == 4 || co + ct == 4)
		{    fout << "Case #" << i+1 <<  ": "<< "O won" << endl; goto nextcase;}
		if (cx == 4 || cx + ct == 4)
		{    fout << "Case #" << i+1 <<  ": "<< "X won" << endl; goto nextcase;}

        co = 0; cx = 0; ct = 0;
        for (int m=0; m < 4; m++)
		{
			char c = b[m][3-m];
			if (c == 'O')
				co++;
			if (c == 'X')
				cx++;
			if (c == 'T')
				ct ++;
		}
		if (co == 4 || co + ct == 4)
		{    fout << "Case #" << i+1 <<  ": "<< "O won" << endl; goto nextcase;}
		if (cx == 4 || cx + ct == 4)
		{    fout << "Case #" << i+1 <<  ": "<< "X won" << endl; goto nextcase;}



		if (filled) {
		    fout << "Case #" << i+1 <<  ": " << "Draw" << endl;
		} else 
            fout << "Case #" << i+1 <<  ": " << "Game has not completed" << endl;
nextcase:
        continue;
	}
	return 0;
} 