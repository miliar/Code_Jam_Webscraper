#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

void readInteger (int & n)
{
	cin >> n;
	cin.ignore();
}
int main()
{
	int nCases, N, S, p, count;
	int suprScore, highScore;

	readInteger( nCases );
	for (int i=1;i<=nCases;i++)
	{
		readInteger( N );
		readInteger( S );
		readInteger( p ); // best result >= p
		count = 0;
		suprScore = max( p, 3*p-4 );
		highScore = max( p, 3*p-2 );

		int * scores = new int[N];
		for (int j=0;j<N;j++)
			readInteger( scores[j] );

		for (int j=0;j<N;j++)
		{
			if (scores[j] >= highScore)
				count++;
			else if (scores[j] >= suprScore && S > 0)
			{
				count++;
				S--;
			}
		}
		delete [] scores;
		cout << "Case #" << i << ": " << count << endl;
	}
	return 0;
}
