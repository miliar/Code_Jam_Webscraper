#include <iostream>
#include <math.h>
#include <fstream>

using namespace std;

void main(){
	int total;
	long N, K;

	ifstream iptFile ("F:\\KMZ\\A-large.in");
	ofstream optFile ("F:\\KMZ\\output.txt");
	
	iptFile>>total;

	for (int i = 0;i < total;i++)
	{
		iptFile>>N>>K;

		K ++;

		long onNum = pow((double)2, N);
		
		long res = K % onNum;

		if (res != 0)
		{
			optFile<<"Case #"<<(i + 1)<<": "<<"OFF"<<endl;
		}else
		{
			optFile<<"Case #"<<(i + 1)<<": "<<"ON"<<endl;
		}
		
	}

	iptFile.close();
	optFile.close();
}