#include <iostream>
#include <fstream>

using namespace std;

void main()
{
	unsigned int num, N, K;
	ifstream in("c:\\A-large.in");
	ofstream out("c:\\A-large.out");

	in >> num;

	for(unsigned int i = 0; i < num; ++i)
	{
		out << "Case #" << i + 1 << ": ";
		in >> N;
		in >> K;

		if((K+1) & ((1 << N) - 1))
			out << "OFF" << endl;
		else
			out << "ON" << endl;
	}

	out.close();
	in.close();
}