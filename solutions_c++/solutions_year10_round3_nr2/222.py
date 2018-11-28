#include <iostream>
#include <math.h>

using namespace std;

unsigned int T, L, P, C;

void main(int argc, char **argv)
{
	FILE *input;

	input = fopen(argv[1], "r");

	fscanf(input, "%u", &T);

	for(int i=1; i<=T; i++)
	{
		fscanf(input, "%u %u %u", &L, &P, &C);

		double l = L;
		double p = P;
		double c = C;

		unsigned int X = ceil(log(p/l) / log(c));
		X = ceil(log(double(X)) / log(double(2)));

		cout << "Case #" << i << ": " << X << "\n";
	}

	fclose(input);
}