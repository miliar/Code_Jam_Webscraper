#include "iostream"
#include "fstream"
#include "string"
#include "algorithm"
#include "math.h"

using namespace std;
int main()
{
	int a;
	long n,k,l;

	ifstream infile("A-large.in");
	infile >> l;
	infile.get();

	ofstream outfile("A-large.out");

	int temp;
	int x = 1;
	do
	{
		int N;
		infile >> N;
		int a[1001], b[1001];
		long long count = 0;
		for (int i = 0; i < N; ++i)
			infile >> a[i] >> b[i];

		for (int i = 0; i < N; ++i)
			for (int j = 0; j < N; ++j)
			{
				if (((a[i]  > a[j]) && (b[i] < b[j])) || ((a[i] < a[j]) && (b[i] > b[j])))
					++count;
			}

			count = count/2;
			outfile << "Case #" << x << ": " << count << "\n";
			++x;

	} while (x <= l );
	infile.close();
	outfile.close();
	return(0);
}