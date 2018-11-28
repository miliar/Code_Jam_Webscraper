#include<iostream>
#include<fstream>
using namespace std;

bool function( int N , int K );

int main()
{
	ifstream inf;
	ofstream out;
	inf.open ("A-small-attempt3.in");
	out.open ("out.out");
	int T,N,K;
	bool check;
	inf>>T;
	for ( int i = 0 ; i <T ; i++ )
	{
		out<<"Case #"<<i+1<<": ";
		inf>>N>>K;
		check = function (N , K );
		if ( check == 0 )
			out<<"OFF"<<endl;
		else 
			out<<"ON"<<endl;
	}
}

bool function( int N , int K )
{
	if ( K<N)
		return false;

	bool *A = new bool [N];    // represents the ON/OFF states
	bool *B = new bool [N];    // represents the receiving/not receiving power state
	bool *temp1 = new bool[N]; // temporary array of A
	bool *temp2 = new bool[N]; // temporary array of B
	for ( int i = 0 ; i < N ; i++ )
	{
		A[i] = false;
		B[i] = false;
	}
	B[0] = true;
	temp2[0] = true;
	temp1[0] = false;
	for ( int i = 0 ; i < K ; i++ )
	{
		temp1[0] = !A[0];
		for ( int j = 1 ; j< N ; j++ )
		{
			if (A[j-1]== true && B[j-1] == true)  
// a Snapper is in the ON state and is receiving power from its input plug
				temp1[j] = !A[j];
			else
				temp1[j] = A[j];
			if ( temp1[j-1] == true && temp2[j-1]==true )
				temp2[j] = true;
			else
				temp2[j] = false;
		}
		for ( int i = 0 ; i < N ; i++ )
		{
			A[i] = temp1[i];
			B[i] = temp2[i];
		}
	}

	return (B[N-1]&&A[N-1]);
}