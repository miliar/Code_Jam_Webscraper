#include <iostream>
#include <fstream>
#include <string>
using namespace std;

//#include "Case.h"


int checkList(int start, string* list, int length, char test)
{
	for(int i = start; i < length; i++)
	{
		if (list[i].at(0) == test || list[i].at(1) == test)
			return i;
	}

	return -1;
}

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
	cout<<"got here!\n";

	int C, D, N;
	string combine[100];
	string oppose[100];
	bool done;
	string invoke;
	char list [1000];
	int listLength, comLen, oppLen;
	string next;
	int check;
	char otherone;
	for (int i = 0; i<T; i++)
	{
		listLength = 0, comLen = 0; oppLen = 0, done = false;
		//initialize case CODE HERE
		cout<<"and here:"<<i<<endl;
		in >> C;
		for (int j = 0; j<C; j++)
		{
			in>> next;
			combine[comLen++] = next;
		}
		in >> D;
		for (int j = 0; j<D; j++)
		{
			in>> next;
			oppose[oppLen++] = next;

		}
		in >> N;
		in >> invoke;
		list[listLength++] = invoke.at(0);

		for(int j = listLength; j< invoke.length(); j++)
		{
			cout<< "take that! "<< j <<endl;
			check = checkList(0, combine, comLen, invoke.at(j));
			while (check != -1)
			{
				if ((list[listLength-1] == combine[check].at(0) && invoke.at(j) == combine[check].at(1)) ||
					(list[listLength-1] == combine[check].at(1) && invoke.at(j) == combine[check].at(0)) )
				{
					listLength--;
					invoke.replace(j,1,1,combine[check].at(2));
					check = -1;
				}
				check++;
				check = checkList(check, combine, comLen, invoke.at(j));
				if (listLength == 0)
					check = -1;
			}
			check = checkList(0, oppose, oppLen, invoke.at(j));
			while (check != -1)
			{
				if (invoke.at(j) == oppose[check].at(0))
				{
					otherone = oppose[check].at(1);
				}
				else
					otherone = oppose[check].at(0);
				for (int k = 0; k< listLength; k++)
				{
					if (list[k] == otherone)
					{
						listLength = 0;
						j++;
					}
				}
				check++;
				if (j < invoke.length())
				{
					check = checkList(check, oppose, oppLen, invoke.at(j));
				}
				if (listLength == 0)
					check = -1;
			}
			if (j<invoke.length())
			{
				list[listLength++] = invoke.at(j);
			}
		}


		
		//run case & add to output file
		out << "Case #" << i+1 << ": [";
		for (int j = 0; j <listLength; j++)
		{
			if (j != 0)
			{
				out << ", ";
			}
			out<< list[j];
		}

		out << "]" << endl;
	}		
	//close input file
	in.close();
	//close output file
	out.close();
	return 0;
}





