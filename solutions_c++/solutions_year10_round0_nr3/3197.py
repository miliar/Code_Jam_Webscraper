/*

R = 4 # of Rides
K = 6 Max # of Seats
1 4 2 1 


*/

#include <iostream>
using namespace std;
#include <math.h>

int index = 0;

long read(long *gC , int nG)
{
	index = index%nG;
	index++;
	return gC[index -1];
}

long unRead(long *gC,int nG)
{
	if( index > 0)
	{
		index = index -1;
		return gC[index];
	}
	else
		return 0;
}


int main()
{
	long R,K,N,T;
	long *gC; //group Cardinality
	long cC=0,tR=0; //Toatal capacity;


	cin >> T;
	
	for( int i = 0; i< T ; i++)
	{
		tR = 0;
		index = 0;
		cin >> R;
		cin >> K;
		cin >> N;
		
		gC = new long[N];

		for( int j = 0;j < N;j++)
		{
			cin >> gC[j];
			
		}
		
		
		for(int k=0;k<R;k++)
		{
			cC = 0;
			int temp = 0;
			do
			{
				long p = read(gC,N);
				temp++;
			
				cC = cC + p;
			}while(cC < K && temp < N);
			
			if(cC > K)
			{
				long q = unRead(gC,N);
				cC = cC - q;

			}
			
			tR = tR + cC;

		}
		cout <<"Case #"<<i+1<<": "<<tR<<endl;
	}		
 
	
}