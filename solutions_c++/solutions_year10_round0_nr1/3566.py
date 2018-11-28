#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int T,N,K;

	ifstream in("a-small.in");
	ofstream out("a.out");

	in >> T;

	for (int i = 0;i < T;i++)
	{
		in >> N >> K;
		out << "Case #" << i+1 << ": ";
		if ((K+1) % (1 << N) == 0)
			out << "ON" << endl;
		else
			out << "OFF" << endl;

		//cout << K+1 << ' ' << (1 << N) << endl;
	}

	return 0;
}