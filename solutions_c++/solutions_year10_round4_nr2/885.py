#include <iostream>
#include <fstream>
#include <string.h>
#include <conio.h>

using namespace std;

enum BOOL {FALSE, TRUE};

BOOL IsBuy[11][1025];
int T, P, M[1025], Price[11][1025], team;
ifstream ifile;
ofstream ofile;

void Input();
int Process();


void main()
{
	int i, result;

	ifile.open("A-small-practice.in");
	ofile.open("A-small-practice.out");

	ifile >> T;

	for ( i = 0; i < T; i++)
	{
		Input();
		result = Process();

		ofile << "Case #" << i+1 << ": " << result << endl;
	}

	ifile.close();
	ofile.close();
}

void Input()
{
	int i, o, tmp;

	team = 1;

	ifile >> P;

	for(i = 0; i < P; i++)
		team *= 2;

	tmp = team;

	for(i = 1; i <= team; i++)
		ifile >> M[i];

	//for(i = 1; i <= team; i++)
	//	cout << M[i];

	for(i = 1; i <= P; i++)
	{
		tmp /= 2;
		for(o = 1; o <= tmp; o++)
		{
			ifile >> Price[i][o];
			IsBuy[i][o] = FALSE;
		}
	}
/*	cout << endl;
	tmp = team;
	for(i = 1; i <= P; i++)
	{
		tmp /= 2;
		for(o = 1; o <= tmp; o++)
		{
			cout << Price[i][o];
			//IsBuy[i][o] = FALSE;
		}
		cout << endl;
	}
	cout << P;*/
}

int Process()
{
	int i, o, K = 0, tmp,x;

						//		cout << P;
	for(i = 0; i < P; i++)
	{
		for(o = 1; o <= team; o++)
		{
			//				cout << "d";
			if(M[o] == i)
			{
			//	cout << "d";
				tmp = (o+1) / 2;
				for(x = 0; x < i; x++)
					tmp = (tmp+1)/2;
				for(x = i + 1; x <= P; x++)
				{
					if(IsBuy[x][tmp])
						break;
					else
					{
					//	cout << Price[x][tmp];
						K += Price[x][tmp];
						IsBuy[x][tmp] = TRUE;
						tmp = (tmp + 1) / 2;
					}
				//	cout << endl;
				}
			}
		}
	}

	return K;
}