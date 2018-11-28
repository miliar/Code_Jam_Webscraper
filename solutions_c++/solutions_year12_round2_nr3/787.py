#include <cmath>
#include <iostream>
using namespace std;

#define M_E 2.71828182845904523536

double f(double x)
{
	return 0.2 * (2 * pow(M_E, x) - 2);
}

int main()
{
	double eps = 1e-4;
	double l = -0.2, r = 0.2;
	double previous = ~(1 << 31), current = l;

	int nIteration = 1;
	while (fabs(current - previous) >= eps)
	{
		previous = current;
		current = f(previous);
		cout << "#" << nIteration << ": " 
			 << "x" << nIteration - 1 << " = " << previous << " "
			 << "x" << nIteration << " = " << current << '\n';
		nIteration++;
	}

	cout << "Result: " << previous << '\n';
	return 0;
}