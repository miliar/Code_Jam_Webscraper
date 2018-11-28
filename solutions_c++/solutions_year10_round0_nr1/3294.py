/*

	P - 0 -F
	P - 1 -N
	P - 0 -F

	P - 0 - 0 -F
	P - 1 - 0 -F
	P - 0 - 1 -F
	P - 1 - 1 -N

	P - 0 - 0 - 0 - 0 -F
	P - 1 - 0 - 0 - 0 -F
	P - 0 - 1 - 0 - 0 -F
	P - 1 - 1 - 0 - 0 -F
	P - 0 - 0 - 1 - 0 -F
	0000   15 - 16(OFF)- 31 - 32(OFF) - 47 
	1000   (2^N)-1      ((2^N)*2)+1     ((2^N)*3)+2           
	0100
	1100
	0010
	1010
	0110
	1110
	0001
	1001
	0101
	1101
	0011
	1011
	0111
	1111

*/

#include <iostream>
using namespace std;
#include <math.h>

bool getState(int N,long int K)
{
	int j = 1;
	long int onS;//The State at which it is On
		while(1)
		{	
			if(j == 1)
				onS = pow(2.0,N) - 1;
			else
				onS = (pow(2.0,N)-1)*j +(j-1);

			
				if(onS == K)
					return true;
				if(onS < K)
					j++;
				else
					return false;
		}
}

/*int main()
{
	int T; // # of Test Cases
	int N;// # of Snappers
	long int K;//# of Snap
	

	cin >> T;
	for(int i=0;i<T;i++)
	{
		cin >> N;
		cin >> K;
		cout << "Case #"<<i+1<<": ";
		if(getState(N,K))
			cout<<"ON"<<endl;
		else
			cout<<"OFF"<<endl;
			
	
	}
}*/

