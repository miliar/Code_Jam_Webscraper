#include <iostream.h>
#include <fstream.h>

// Code Jam 2010
// Qualification Round
// A. Snapper Chain



int main(int argc, char *argv[])
{
	int N,T;
	__int64 K;
	
	int t;
	
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
		inFile >> N;
		inFile >> K;
		
		if ( ((((__int64)1<<N)-1) & K) == (((__int64)1<<N)-1) )
			cout << "Case #" << t+1 << ": ON" << endl;
		else
			cout << "Case #" << t+1 << ": OFF" << endl;
	}
		
		
	
	inFile.close();
	return 0;
}