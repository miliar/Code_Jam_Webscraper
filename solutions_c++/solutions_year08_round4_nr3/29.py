#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>

using namespace std;

int T, N;
vector<double> x, y, z, p;

int main()
{
	ifstream input;
	ofstream output;
	input.open("C-large.in");
	output.open("C-large.out");

	input >> T;
	for (int c = 0; c < T; c++)
	{
		input >> N;
		x.resize(N);
		y.resize(N);
		z.resize(N);
		p.resize(N);

		for (int i = 0; i < N; i++)
			input >> x[i] >> y[i] >> z[i] >> p[i];

		double ans = 0;
		for (int i = 0; i < N; i++)
			for (int j = i + 1; j < N; j++)
			{
				double now = abs(x[i] - x[j]) + abs(y[i] - y[j]) + abs(z[i] - z[j]);
				now = now / (p[i] + p[j]);
				if (now > ans) ans = now;
			}

		output << "Case #" << c + 1 << ": ";
		output << fixed << setprecision(7) << ans << endl;
	}

	input.close();
	output.close();
}
