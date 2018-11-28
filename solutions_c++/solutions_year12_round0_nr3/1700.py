#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>

using namespace std;

int quant[9] = {0, 1, 3, 6, 10, 15, 21, 28, 36};

int main()
{
	int a, b, t;
	ifstream in;
	ofstream out;
	in.open("C-large.in");
	out.open("C-large.out");
	in >> t;
	bool tt[2000001];
	for (int caseN = 1; caseN <= t; ++caseN)
	{
		cout << caseN << endl;
		memset(tt, 0, sizeof(tt));
		long long result = 0;
		in >> a >> b;
		for (int cur = a; cur <= b; ++cur)
		{
			if (tt[cur])
				continue;
			tt[cur] = true;
			int q = 0;
			int dig = 0;
			int temp = cur;
			while (temp /= 10)
				++dig;
			temp = cur;
			for (int curDig = 0; curDig < dig; ++curDig)
			{
				int d = temp % 10;
				if (d)
				{
					temp = temp / 10 + d * pow(10, dig);
					if (temp >= a && temp <= b && !tt[temp])
					{
						tt[temp] = true;
						++q;
					}
				}
				else
					temp = temp / 10;
			}
			if (q)
				result += quant[q];
		}


		out << "Case #" << caseN << ": " << result << endl;
	}

	out.close();
	in.close();
}

