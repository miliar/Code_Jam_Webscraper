#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>

using namespace std;

int t, n;

int main()
{
	ifstream input;
	ofstream output;
	input.open("A-large.in");
	output.open("A-large.out");

	input >> t;
	for (int c = 0; c < t; c++)
	{
		input >> n;
		vector<long long> x(n);
		vector<long long> y(n);

		for (int i = 0; i < n; i++) input >> x[i];
		for (int i = 0; i < n; i++) input >> y[i];

		sort(x.begin(), x.end());
		sort(y.begin(), y.end());

		long long ans = 0;
		for (int i = 0; i < n; i++) ans += x[i] * y[n-1-i];

		output << "Case #" << c + 1 << ": " << ans << endl;
	}

	input.close();
	output.close();
}
