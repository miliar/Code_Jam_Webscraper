#include <fstream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

ifstream in("A-small.in");
ofstream out("A-small.out");

int calc(vector <int> x, vector <int> y)
{
	sort(x.rbegin(), x.rend());
	sort(y.begin(), y.end());

	return inner_product(x.begin(), x.end(), y.begin(), 0);
}

int main()
{
	int T;
	in >> T;

	for (int i = 0; i < T; i++)
	{
		int n, t;
		in >> n;
		vector <int> x;
		vector <int> y;

		for (int j = 0; j < n; j++)
		{
			in >> t;
			x.push_back(t);
		}

		for (int j = 0; j < n; j++)
		{
			in >> t;
			y.push_back(t);
		}

		out << "Case #" << i + 1 << ": " << calc(x, y) << endl;
	}

	in.close();
	out.close();

	return 0;
}
