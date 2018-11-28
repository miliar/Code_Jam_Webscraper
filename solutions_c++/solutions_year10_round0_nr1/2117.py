#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <conio.h>

using namespace std;


int main()
{
	ifstream input("A-large.in");
	ofstream output("A-large.out");
	long long T, N, K, count=0, val=0;
	input >> T;
	for (int a=0; a < T; a++)
	{
		input >> N;
		input >> K;
		val = (long long) pow((double) 2, (double) N);
		count = (K+1) % val;
		output << "Case #" << a+1<< ": ";
		if (count == 0) 
           output << "ON" << endl;
        else
           output << "OFF" << endl;
	}
	system("PAUSE");
	return 0;
}
