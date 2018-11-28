#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream in;
	ofstream out;
	in.open("C-large.in");
	out.open("C-large.out");

	int T,N;
	in>>T;
	
	int sumx;
	int sum;
	int min=1000001;
	int C;

	for (int t=0; t<T; t++)
	{
		sum=0;
		sumx=0;
		min=1000001;

		in>>N;

		for (int i=0; i<N; i++)
		{
			in>>C;
			sumx^=C;
			sum+=C;
			if (C<min) min = C;
		}

		if (sumx!=0) out<<"Case #"<<t+1<<": NO"<<endl;
		else out<<"Case #"<<t+1<<": "<<(sum-min)<<endl;
	}

	in.close();
	out.close();
	return 0;
}