#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");
	int T, S, p, N, y;
	vector<int> a;

	in >> T;

	for (int i = 0; i < T; i++)
	{
		in >> N;
		in >> S;
		in >> p;
		a.resize(N);
		for (int j = 0; j < N; j++)
		{
			in >> a[j];
		}

		//alg begin
		int alpha = max(1, 3*p - 4);
		int beta = 3*p - 2;
		int good = 0, surprise = 0;
		for (int j = 0; j < N; j++)
		{
			if (beta <= a[j])
			{
				good++;
			}
			else if (alpha <= a[j])
			{
				surprise++;
			}
		}
		y = good + min(S, surprise);
		//alg end

		//output
		out << "Case #" << i + 1 << ": " << y << "\n";
	}


	return 0;
}