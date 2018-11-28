#include <fstream>
#include <vector>

using namespace std;

int main()
{
	ifstream in ("b.in");
	ofstream out ("b.out");

	int t, n, s, p;

	in >> t;

	for (int i = 0; i < t; i++)
	{
		int result = 0;
		int possibles = 0;
		in >> n >> s >> p;

		vector<int> vec(n);

		for(int j = 0; j < n; j++)
		{
			in >> vec[j];
		}

		for(int j = 0; j < n; j++)
		{
			if (vec[j] == 0)
			{
				if (p == 0)
				{
					result ++;
				}
				continue;
			}

			if (vec[j] == 1)
			{
				if (p <= 1)
				{
					result ++;
				}
				continue;
			}

			if (vec[j] == 2)
			{
				if (p <= 1)
				{
					result ++;
					continue;
				}
				if (p <= 2)
				{
					possibles++;
					continue;
				}
				continue;
			}

			double ost = vec[j] / 3.;
			if (ost + 0.9 > p)
			{
				result++;
				continue;
			}
			if (ost + 1.5 >=p)
			{
				possibles++;
			}
		}

		result += min(s, possibles);

		out << "Case #" << i+1 << ": " << result << endl;
	}

	in.close();
	out.close();

	return 0;
}