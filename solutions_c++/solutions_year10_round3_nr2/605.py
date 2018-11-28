#include <iostream>
using namespace std;
#include <cmath>
int main()
{
	long T,L,P,C;
	int nT = 0;
	
	cin >> T;
	
	for( int i = 0; i< T ; i++)
	{
		cin >> L >> P >> C;
		nT = 0;
		while (P > L  )
		{
			L = L * C ;
			//cout << L << endl;
			nT++;
		}
		
		 cout <<"Case #"<<i+1<<": "<<ceil(log(nT)/log(2))<<endl;
	}		
 
	
}