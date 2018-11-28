#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int T, N, Pd, Pg;
	bool isPossible;
	ifstream inFile( "A-small-attempt1.in" );
	ofstream outFile( "A-small.txt" );

	inFile >> T;

	int temp;
	for(int i = 0; i < T; i++)
	{
		inFile >> N >> Pd >> Pg;
		isPossible = false;
		for(int j = 1; j <= N; j++)
		{
			float div = j*(Pd/100.0f);
			if(div-(int)(div)==0.0f)
			{
				isPossible = true;
				if((Pg==100.0f)&&(Pg>Pd))
					isPossible = false;
				if((Pg==0.0f)&&(Pd>Pg))
					isPossible = false;
				break;
			}
		}

		outFile << "Case #" << i+1 << ": ";

		if(isPossible)
		{
			outFile << "Possible" << endl;
		}
		else
		{
			outFile << "Broken" << endl;
		}
	}

	return 0;
}