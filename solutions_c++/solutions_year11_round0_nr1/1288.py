#include <iostream>
#include <fstream>
#include <string>
using namespace std;

//#include "Case.h"

int main()
{
	//Open files
	ifstream in;
	ofstream out;

	in.open("in.txt", ios::in);

	if (!in) {
	  cout << "Can't open input file." << endl;
	}

	out.open("out.txt", ios::out);

	if (!out) {
	  cout << "Can't open output file " << endl;
	  return 1;
	}
	//Get number of cases
	int T = 0;
	in >> T;

//	Case cur;

	int N, No, Nb, Opos, Bpos;
	int Olist[102];
	int Blist[102];
	int Clist[102];
	char next;
	int time;
	bool done;
	int Ostep, Bstep;
	for (int i = 0; i<T; i++)
	{
		No = 0, Nb= 0, Opos = 1, Bpos = 1, time = 0, done = false, Ostep = 0, Bstep = 0;
		//initialize case CODE HERE
		in >> N;
		for (int j = 0; j<N; j++)
		{
			in >> next;
			if (next == 'O')
			{
				in >> Olist[No++];
				Clist[j] = 0;
			}
			else
			{
				in >> Blist[Nb++];
				Clist[j] = 1;
			}
		}
		while(!done)
		{
			if (Clist[Ostep + Bstep] == 0)
			{
				if (Opos == Olist[Ostep])
							{
								Ostep++;
							}
							else if (Opos < Olist[Ostep])
							{
								Opos++;
							}
							else
							{
								Opos--;
							}
							if (Bpos < Blist[Bstep])
							{
								Bpos++;
							}
							else if (Bpos > Blist[Bstep])
							{
								Bpos--;
							}
			}
			else
			{
				if (Opos < Olist[Ostep])
				{
					Opos++;
				}
				else if (Opos > Olist[Ostep])
				{
					Opos--;
				}
				if (Bpos == Blist[Bstep])
				{
					Bstep++;
				}
				else if (Bpos < Blist[Bstep])
				{
					Bpos++;
				}
				else
				{
					Bpos--;
				}
			}
			if (Ostep == No && Bstep == Nb)
				done = true;
			time++;
		}








		
		//run case & add to output file
		out << "Case #" << i+1 << ": " << time << endl;
	}		
	//close input file
	in.close();
	//close output file
	out.close();
}
