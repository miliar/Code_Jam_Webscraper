#include <iostream.h>
#include <fstream.h>

// Code Jam 2011
// Round 1 A
// A. FreeCell Statistics



int main(int argc, char *argv[])
{
	int T,t;
	__int64 N,n;
	
	int PD, PG;
	
	int temp;
	
	int answer;
	
	ifstream inFile;
	
	//inFile.open("test.in");
	if ( argc < 2 )
	{
		cout << "No input file given!" << endl;
		exit(1);
	}
	inFile.open(argv[1]);
	if ( !inFile )
	{
		cout << "Error opening file!" << endl;
		exit(1);
	}
	
	inFile >> T;
	
	for (t=0;t<T;t++)
	{
		inFile >> N;
			
		inFile >> PD;
		
		inFile >> PG;
		
		answer = 0;
	
		n=1;
		while(n<=100)
		{
			if ( ((n*PD) % 100) == 0 )
			{
				if ( n<=N )
				answer = 1;
			}
			n++;
		}
		
		
		if ( PG == 100 && PD < 100 )
		{
			answer = 0;
		}
		
		if ( PD > 0 && PG == 0 )
		{
			answer = 0;
		}
		
		if ( answer == 0 )
		{
			//cout << "Case #" << t+1 << ": " << answer << endl;
			cout << "Case #" << t+1 << ": Broken" << endl;
		}
		else
		{
			cout << "Case #" << t+1 << ": Possible" << endl;
		}
	}
		
		
	
	inFile.close();
	return 0;
}