#include<iostream>
#include <fstream>
#include<list>
using namespace std;


unsigned long long function ( int R , unsigned long long k , int N , int *A );

int main()
{
	ifstream inf;
	ofstream out;
	inf.open ( "C-large.in" );
	out.open ("out.out" );
	int T;
	inf>>T;
	int * A;
	int R,N;
	unsigned long long k;
	for ( int i = 0 ; i < T ; i++ )
	{
		inf>>R>>k>>N;
		int *A = new int[N];
		for ( int i = 0 ; i < N ; i++ )
			inf>>A[i];

		out<<"Case #"<<i+1<<": "<<function ( R , k , N , A )<<endl;
	}
	return 0;
}

unsigned long long function ( int R , unsigned long long k , int N , int* A )
{
	unsigned long long *S = new unsigned long long[N];// money in each cycle 
	int *D = new int[N]; // when we get again the same group at the head of the line
	bool *E = new bool[N]; // needed for D
	for ( int i = 0 ; i <N ; i++ )
	{
		S[i] = -1;
		D[i] = -1;
		E[i] = false;
	}

	int p = 0;
	unsigned long long s;
	unsigned long long money = 0;
	int j;
	int index;
	for ( int i = 0 ; i < R ; i++ )
	{	
		s = 0;
		j = p;
		index = p;
		if ( E[p] == false)
		{	if ( D[p] == -1 )
			{
				D[p] = i;
				S[p] = money;
			}
			else
			{
				D[p] = i - D[p];
				E[p] = true;
				S[p] = money - S[p];
			}
		}
		if (( E[p] == false) || ((i + D[p]) > R ))
		{
			while (( j-p < N ) && (A[index] <= (k-s) ))
			{
				s = s+A[index];
				j++;
				index++;
				if ( index == N )
					index = 0;
			}
			p = index;
			money = money + s;
		}
		else
		{
			money = money + S[p];
			i = i + D[p] -1 ;
		}
	}
	return money;
}