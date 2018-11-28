#include <iostream>
#include <fstream>
using namespace std;

int myArray[30];


int main()
{
	int cases,temp, N, K;
	ifstream in("input.txt");
	ofstream out("output.txt");
	myArray[0] = 1;
	for(int i=1; i<30; i++)
		myArray[i] = 2*myArray[i-1]+1;
	in >> cases;
	for (int j=0; j<cases; j++)
	{
		in >> N >> K;
		while(K > myArray[N-1])
		{
			for(int i=0; i<30; i++)
			{
				if(myArray[i] == K)
				{
					K = myArray[N-1];
					break;
				}
				if (myArray[i] > K)
				{
					K = K - myArray[i-1]-1;
					break;
				}
			}
		}
		out << "Case #" << j+1 << ": ";
		if (K==myArray[N-1])
			out << "ON" << endl;
		else
			out << "OFF" <<endl;
	}
}