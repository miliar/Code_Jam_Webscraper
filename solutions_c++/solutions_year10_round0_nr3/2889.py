#include <iostream>
#include <fstream>
using namespace std;

ifstream input("C-small.in");
ofstream output("C-small.out");

int a[1001];

int main()
{
	int i, j, k, r, t, n, l, p, sum, now, w;
	input >> t;
	for (j = 1; j <= t; j++)
	{
		input >> r >> p >> n;
		for (i = 0; i < n; i++)
			input >> a[i];
		sum = 0;
		k = 0;
		for (l = 1; l <= r; l++)
		{
			now = 0; w = 0;
			while (now + a[k] <= p  &&  w < n)
			{
				now += a[k];
				k = (k + 1) % n;
				w++;
			}
			sum += now;
		}
		output << "Case #" << j << ": " << sum << endl;
	}
	input.close();
	output.close();
	return 0;
}
		
		