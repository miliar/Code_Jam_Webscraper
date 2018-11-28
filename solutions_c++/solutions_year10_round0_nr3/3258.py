#include <iostream.h>
#include <fstream.h>

// Code Jam 2010
// Qualification Round
// C. Theme Park



int main(int argc, char *argv[])
{
	__int32 R,k;
	int T,t;
	
	int N,n;
	__int32 g[1001];
	
	__int32 money;
	
	int capacity;
	int fills;
	
	ifstream inFile;
	
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
		inFile >> R;
		inFile >> k;
		inFile >> N;
		
		for (n=0;n<N;n++)
			inFile >> g[n];
		
		money = 0;
		n = 0;
		while (R>0)
		{
			capacity = g[n];
			fills = 0;
			while ( capacity <= k )
			{
				if ( n<N-1 )
					n++;
				else
					n = 0;
				capacity += g[n];
				fills++;
				if ( fills == N )
					break;
			}
			capacity -= g[n];

			money += capacity;
			R--;
		}
		
		cout << "Case #" << t+1 << ": " << money << endl;
	}
		
		
	
	inFile.close();
	return 0;
}