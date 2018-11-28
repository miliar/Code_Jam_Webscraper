#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;


bool etudeCase(char c, char* winner, bool* t)
{
	if(c=='.')
		return false;
	if(c=='T')
	{
		if(*t)
			return false;
		*t=true;
		return true;
	}
	if(*winner==0)
	{
		*winner = c;
		return 1;
	}
	else
		return *winner==c;
}


int main()
{
	string name("A-large");
	ifstream in;
	ofstream out;
	int nbCases = 0; // size of the sets loaded

	vector<string> grid;

	// Variables end -------------------------------------------------------------------------

	in.open((name + ".in").c_str());
	out.open((name + ".out").c_str()); // flux opening

	if(!(in.is_open() && out.is_open()))
	{
		cerr << "> one of the file could not be loaded" << endl;
	}

	in >> nbCases; // getting case number
	grid.resize(nbCases);

	for(int c=1;c<=nbCases;c++)
	{
		char res=0; // 0: draw, 1: rien, 2: X winner, 3: O winner
		for(int j=0;j<4;j++)
			in >> grid[j]; // data recperation
		//cout << "fin pré passe" << endl;
		for(int i=0;i<4;i++)
		{
			char win1=0, win2=0;
			bool t1=false, t2=false;
			bool ok1=true, ok2=true;

			for(int j=0;j<4;j++)
			{
				//column
				ok1 &= etudeCase(grid[j][i], &win1, &t1);
				//line
				ok2 &= etudeCase(grid[i][j], &win2, &t2);
			}

			if(ok1)
				res= (win1=='X'?2:3);
			else if(ok2)
				res= (win2=='X'?2:3); // if there was a winner
		}
		//cout << "fin première passe" << endl;
		if(res==0)
		{
			char win1=0, win2=0;
			bool t1=false, t2=false;
			bool ok1=true, ok2=true;

			for(int j=0;j<4;j++)
			{
				//column
				ok1 &= etudeCase(grid[j][j], &win1, &t1);
				//line
				ok2 &= etudeCase(grid[j][3-j], &win2, &t2);
			}
			if(ok1)
				res= (win1=='X'?2:3);
			else if(ok2)
				res= (win2=='X'?2:3); // if there was a winner

			if(res==0)
			{
				for(int i=0;i<4 && res==0;i++)
					for(int j=0;j<4 && res==0;j++)
						if(grid[i][j]=='.')
							res=1; // on a pas un draw
			}
		}


		out << "Case #" << c << ": ";

		switch(res)
		{
			case 0: out << "Draw"; break;
			case 1: out << "Game has not completed"; break;
			case 2: out << "X won"; break;
			case 3: out << "O won"; break;
			default: cerr << "erreur de calcul" << endl;
		}

		out << endl; // starts at 1
	}

    in.close();
    out.close();
    cout << "Appuyez sur ENTER pour continuer" << endl;
    cin.get();
    return 0;
}
