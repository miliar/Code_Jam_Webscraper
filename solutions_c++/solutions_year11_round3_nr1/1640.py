#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;
#define INPUT "A-large.in"
#define OUTPUT "a.out"

ifstream inp;
ofstream out;

int T;
int R;
int C;


int pic[2500];
char buffer[51];

void solve(int index)
{
	inp >> R >> C;
	bool imp = false;
	for (int i =0 ; i<R; i++)
	{
		inp >> buffer;
		for (int j=0; j <C; j++)
		{
			pic[i*C+j] = 0;
			if (buffer[j] == '#')
				pic[i*C+j] = 5;
		}
	}
	for (int i =0; i<R-1; i++)
		for (int j =0 ; j<C-1; j++)
			if (pic[i*C+j] == 5)
			{
				if (pic[i*C+j+1] !=5 || pic[(i+1)*C+j]!=5 || pic[(i+1)*C+j+1]!=5)
				{
					imp = true;
					break;
				}
				pic[i*C+j+1] = 2;
				pic[i*C+j] = 1;
				pic[(i+1)*C+j] = 3;
				pic[(i+1)*C+j+1] = 4;
			}
	for(int i=0; i<R; i++)
		if (pic[i*C+C-1] == 5) imp = true;
	for (int j=0;j<C; j++)
		if (pic[(R-1)*C+j] == 5) imp = true;
	out << "Case #" << index << ":" << endl;
	if (imp)
		out<< "Impossible" << endl;
	else
	{
		for (int i=0; i<R; i++)
		{
			for (int j = 0; j<C; j++)
				switch (pic[i*C+j])
			{
				case 0: out << "."; break;
				case 1: out << "/"; break;
				case 2: out << "\\"; break;
				case 3: out << "\\"; break;
				case 4:out << "/"; break;
			}
			out << endl;
		}
	}
}

void main()
{
	inp.open(INPUT);
	out.open(OUTPUT);
	inp >> T;
	for (int i = 1; i <= T; i++)
		solve(i);
	inp.close();
	out.close();
}