#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int t, n, s, p;
	ifstream in;
	ofstream out;
	in.open("B-large.in");
	out.open("B-large.out");
	in >> t;
	for (int caseN = 1; caseN <= t; ++caseN)
	{
		int result = 0;
		int ss = 0;
		in >> n >> s >> p;
		vector<int> sum;
		int temp;
		for ( int i = 0; i < n; ++i )
		{
			in >> temp;
			sum.push_back(temp);
		}
		for (int i = 0; i < sum.size(); ++i)
		{
			int cur = sum[i];
			if (cur < p)
				continue;
			cur -= p;
			if (cur >= (p - 1) * 2)
				++result;
			else
			{
				if (cur >= (p - 2) * 2)
					++ss;
			}
		}
		result += min(ss, s);

		out << "Case #" << caseN << ": " << result << endl;
	}

	out.close();
	in.close();
}

