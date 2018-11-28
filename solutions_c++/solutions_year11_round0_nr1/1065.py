#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	ifstream input("A-large.in");
	ofstream output("outputl.txt");

	int T;
	input >> T;

	for(int caseID = 1; caseID <= T; caseID++)
	{
		//read data
		vector<char> sequence;
		vector<int> O;
		vector<int> B;
		int N;
		input >> N;
		char tempChar;
		int tempInt;
		for (int i =0 ; i != N; i++)
		{
			input >> tempChar;
			sequence.push_back(tempChar);
			input >> tempInt;

			if (tempChar == 'O')
			{
				O.push_back(tempInt);
			}
			else
			{
				B.push_back(tempInt);
			}


		}


		//solve

		vector<int> OT;
		vector<int> BT;

		for (int i = 0; i != O.size(); i++)
		{
			if (i == 0)
			{
				OT.push_back(O[i]);
			}
			else
			{

				OT.push_back( abs(O[i] - O[i-1])+1 );
			}
		}

		for (int i = 0; i != B.size(); i++)
		{
			if (i == 0)
			{
				BT.push_back(B[i]);
			}
			else
			{
				BT.push_back( abs(B[i] - B[i-1])+1 );		
			}
		}

		int Otimer = 0;
		int Opos = 0;

		int Btimer = 0;
		int Bpos = 0;

		int currTime = 0;

		for (int pos = 0; pos != sequence.size(); pos++)
		{
			if (sequence[pos] == 'O')
			{
				if ( (currTime-Otimer) < OT[Opos] )
				{
					Otimer = Otimer + OT[Opos];
					currTime = Otimer;
					
				}
				else
				{

					currTime++;
					Otimer = currTime;
				}
				Opos++;

			}
			else
			{
				if ( (currTime - Btimer) < BT[Bpos])
				{
					Btimer = Btimer + BT[Bpos];
					currTime = Btimer;
					
				} 
				else
				{
					currTime++;
					Btimer = currTime;
				}
				Bpos++;


			}

		}
		//output result
		output << "Case #" << caseID << ": "<< currTime << endl;
	}
}