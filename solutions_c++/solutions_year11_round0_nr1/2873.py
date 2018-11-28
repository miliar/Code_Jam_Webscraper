// codejam1.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

char *charSqu;
int *buttonSqu;

int GoStraight(int step, int length, int hallwayloc);

int main(int argc, char* argv[])
{
	ifstream infile;
	infile.open("in.txt",ios::in);
	if(!infile)
	{
		cout<<"not found in.txt"<<endl;
		return 0;
	}
	int totalTest = 0;
	char A, B;
	infile>>totalTest;
	ofstream outfile;
	outfile.open("out.txt", ios::out | ios::trunc);
	int i = 0, j = 0, N = 0;
	while(++i <= totalTest)
	{
		N = 0, j =0;
		infile>>N;
		charSqu = new char [N + 1];
		buttonSqu = new int [N + 1];
		while(++j <= N)
		{
			infile.ignore();
			infile>>charSqu[j];
			infile>>buttonSqu[j];
		}
		int ahallwayloc = 1, bhallwayloc = 1, totalStep = 0, aStep = 1, bStep = 1;
		A = charSqu[1];
		B = (A=='O' ? 'B' : 'O');
		bool finddifferent = true;
		while(aStep <= N && bStep <= N)
		{
			if(finddifferent)
			{
				bStep = aStep;
				while(bStep <= N && charSqu[++bStep] == A);
				if(bStep <= N)
					B = charSqu[bStep];
			}
			if(bStep > N)
			{
				totalStep += GoStraight(aStep, N, ahallwayloc);
				break;
			}else
			{
				int flag = buttonSqu[aStep] - ahallwayloc;
				totalStep += abs(flag) + 1;
				ahallwayloc = buttonSqu[aStep];
				if(buttonSqu[bStep] != bhallwayloc)
				{
					int flag2 = buttonSqu[bStep] - bhallwayloc;
					if(abs(flag)+1 >= abs(flag2))
					{
						bhallwayloc = buttonSqu[bStep];
					}else if(abs(flag)+1 < abs(flag2))
					{
						if(flag2 > 0)
							bhallwayloc +=  abs(flag) + 1;
						else
							bhallwayloc -= abs(flag) + 1;
					}
				}
			}
			if(aStep < N)
			{
				A = charSqu[++aStep];
				if(A == B)
				{
					int temp = ahallwayloc;
					ahallwayloc = bhallwayloc;
					bhallwayloc = temp;
					finddifferent = true;
				}else
				{
					finddifferent = false;

				}
			}else
				break;
		}
		outfile<<"Case #"<<i<<": "<<totalStep<<endl;
		delete buttonSqu;
		delete charSqu;
	}
	infile.close();
	outfile.close();
	return 0;
}

int GoStraight(int step, int length, int hallwayloc)
{
	int result = 0;
	while(step <= length)
	{
		result += abs(buttonSqu[step] - hallwayloc) + 1;
		hallwayloc = buttonSqu[step];
		step++;
	}
	return result;
}