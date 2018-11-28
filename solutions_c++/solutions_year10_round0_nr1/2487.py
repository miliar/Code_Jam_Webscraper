#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int main()
{
	
    int testcase = 0;
	long N,K;
	
	ifstream in("A-large.in");
	ofstream out("out.txt");
	in >> testcase;
	for(long i  = 1; i <= testcase; i++)
	{
		in >> N;
		in >> K;
		if ((K +1)%((long)pow(2.0,N)) == 0 )
			out << "Case #" << i << ": " << "ON" << endl;
		else
			out << "Case #" << i << ": " << "OFF" << endl;
	   
 	}
	return 0 ;

}
