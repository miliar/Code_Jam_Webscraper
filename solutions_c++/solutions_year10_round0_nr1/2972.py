#include <iostream>
#include <fstream>
using namespace std;

ifstream input("A-large.in.txt");
ofstream output("A.out");

int main()
{
	int j, i, n, k, p, t;
	input >> t;
	for(j = 1; j <= t; j++)
	{
		input >> n >> k;
		p = 1;
		for (i = 0; i < n; i++)
			p *= 2;
		output << "Case #" << j << ": ";
		if ((k + 1) % p == 0)
			output << "ON" << endl;
		else
			output << "OFF" << endl;
	}
	input.close();
	output.close();
	return 0;
}
