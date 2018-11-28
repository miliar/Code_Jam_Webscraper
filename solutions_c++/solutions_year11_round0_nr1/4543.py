// cj2011QA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

using namespace std;

void initArray ( void );

int T, t;
int N, n, i;
int moves, movesO, movesB;
int Oval, Bval;
char c, Sval;
int B[105], O[105];
char S[105];
int Bcount, Ocount, Scount, Bloc, Oloc;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream ifs ("a.in", ifstream::in);
	ofstream ofs;
	ofs.open("a.out", ofstream::out);

	ifs >> T;
	for (t=1; t<=T; t++)
	{
		initArray();

		ifs >> N;
		{
			for (i=0; i<N; i++)
			{
				//fscanf_s(fin, "%c", c);
				//fscanf_s(fin, " %d", &n);
				ifs >> c;
				ifs >> n;
				if (c == 'B')
				{
					B[Bcount] = n;
					Bcount++;
				}
				else if (c == 'O')
				{
					O[Ocount] = n;
					Ocount++;
				}
				else
				{

				}
				S[Scount] = c;
				Scount++;
					
			}
		}
		// finish reading in data solve
		Bcount = 0;
		Ocount = 0;
		Scount = 0;
		moves = 0;
		Bloc = 1;
		Oloc = 1;
		Sval = S[Scount];
		while (Sval != '\0')
		{
			moves++;
			// check if blue can push a button, move orange if needed
			if ( (Sval == 'B') && (Bloc == B[Bcount]) )
			{
				Bcount++;
				Scount++;
				if (Oloc < O[Ocount])
					Oloc++;
				else if (Oloc > O[Ocount])
					Oloc--;
				else
					;
			}
			// check if orange can push a button, move blue if needed
			else if ( (Sval == 'O') && (Oloc == O[Ocount]) )
			{
				Ocount++;
				Scount++;
				if (Bloc < B[Bcount])
					Bloc++;
				else if (Bloc > B[Bcount])
					Bloc--;
				else
					;
			}
			else
			{
				if (Bloc < B[Bcount])
					Bloc++;
				else if (Bloc > B[Bcount])
					Bloc--;
				else
					;

				if (Oloc < O[Ocount])
					Oloc++;
				else if (Oloc > O[Ocount])
					Oloc--;
				else
					;
			}

			Bval = B[Bcount];
			Oval = O[Ocount];
			Sval = S[Scount];
		}
		ofs << "Case #" << t << ": " << moves << endl;
	}
	return 0;
	ifs.close();
	ofs.close();
}

void initArray ( void )
{
	int i;
	for (i=0; i <105; i++)
	{
		B[i] = 0;
		O[i] = 0;
		S[i] = '\0';
	}
	Bcount = 0;
	Ocount = 0;
	Scount = 0;
}
