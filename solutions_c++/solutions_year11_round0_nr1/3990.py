#include <fstream>
#include <iostream>
#include <utility>
#include <algorithm>
#include <cmath>

using namespace std;

int Obot [100];
int Bbot [100];
char whichbot [100];

int main () 
{
	ifstream in("in.in");
	ofstream out("out.out");

	
	
	int T, N;
	
	in >> T;
	
	for(int i = 0; i < T; ++i)
	{
		int Ocount = 0;
		int Bcount = 0;
		int Oindex = 0;
		int Bindex = 0;
		int Opos = 1;
		int Bpos = 1;		//bot position
		int time = 0;
		
		in >> N;
		
		for(int j = 0; j < N; ++j)
		{
			in >> whichbot[j];
			if (whichbot[j] == 'O')
				in >> Obot[Ocount++];
			else
				in >> Bbot[Bcount++];
		}
		
		//work now
		for(int j = 0; j < N; ++j) //for each button in the list
		{
			if(whichbot[j] == 'O') //orange next
			{
				int diffTime = abs(Opos - Obot[Oindex]) + 1; 	//time it took O to get there and press
				Opos = Obot[Oindex++];						//set the position of O
				time += diffTime; 							//increment the time
				
				int Bdist = abs(Bpos - Bbot[Bindex]);
				
				if(Bdist <= diffTime)
					Bpos = Bbot[Bindex];
				else
				{
					if (Bpos > Bbot[Bindex])
						Bpos -= diffTime;
					else
						Bpos += diffTime;
				}
			}
			else //else blue
			{
				int diffTime = abs(Bpos - Bbot[Bindex]) + 1; 	//time it took O to get there and press
				Bpos = Bbot[Bindex++];						//set the position of O
				time += diffTime; 							//increment the time
				
				int Odist = abs(Opos - Obot[Oindex]);
				
				if(Odist <= diffTime)
					Opos = Obot[Oindex];
				else
				{
					if (Opos > Obot[Oindex])
						Opos -= diffTime;
					else
						Opos += diffTime;
				}
			}
		}
		
		out << "Case #" << i+1 << ": " << time << "\n";
		
	}
}