#include <iostream>
#include <fstream>

using namespace std;

typedef unsigned char byte;

int TestCase(int N, int K);

int main()
{
	// ofstream constructor opens file                
    ifstream inFile( "A-small.in", ios::in );
	ofstream outFile( "A-small.out", ios::out );
	if ( !outFile || !inFile ) // overloaded ! operator
    {
		cerr << "File could not be opened" << endl;
		exit( 1 );
    }

	
	int N;
	int K;
	int T, i;
	inFile >> T;
	
	for (int i=0;i<T;i++)
	{
		inFile >> N >> K;
		outFile << "Case #" << i+1 << ": " << (TestCase(N,K) ? "ON" : "OFF") << endl;
	}
	inFile.close();
	outFile.close();
	//system("PAUSE");
	return 0;
}

int TestCase(int N, int K)
{

	int **snap= new int*[N];
    for (int  i = 0; i < N; i++)
	{
		snap[i] = new int[2];
		snap[i][0]=0;
		snap[i][1]=0;
	}
	snap[0][0]=1;//snap[n][0] - power of n-th snapper
				 //snap[n][1] - status of n-th snapper
	int n, old, max=N;
	for (int j=0;j<K;++j)
	{
		for (n=0;n<N;++n)
		{//verify which snapper will be toggle
			if (snap[n][0])
				snap[n][1]=!snap[n][1];
			else
				break;
		}
		for (n=0;n<N-1;++n)
		{//verify until which snapper the power will reach
			if (snap[n][1])
				snap[n+1][0]=1;
			else
				break;
		}
		if (n==N-1)
			continue;
		++n;
		old=n;
		while (n<N)
		{	//Sets false for the power in the snappers who are after the power
			snap[n][0]=0;
			++n;
		}
		max=old;
	}

	return (snap[N-1][0] && snap[N-1][1]);
}