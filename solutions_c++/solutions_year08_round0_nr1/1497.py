//#include "stdafx.h"

#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	ifstream f("p1.in");
	int nt;
	f >> nt;
	for (int t = 0; t < nt; t++)
	{
		int ns, nq;
		vector<string> s, q;
		string tmp;

		f >> ns;
		f.ignore(1, '\n');
		for (int i = 0; i < ns; i++)
		{
			getline(f, tmp);
			s.push_back(tmp);
		}
		f >> nq;
		f.ignore(1, '\n');
		for (int i = 0; i < nq; i++)
		{
			getline(f, tmp);
			q.push_back(tmp);
		}

		if (nq > 0)
		{
			int c[100][1000], min;
			for (int i = 0; i < ns; i++)
				c[i][0] = q[0] == s[i];
			for (int i = 1; i < nq; i++)
				for (int j = 0; j < ns; j++)
					if (q[i] != s[j])
						c[j][i] = c[j][i - 1];
					else
					{
						min = 1001;
						for (int k = 0; k < ns; k++)
							if (k != j && c[k][i - 1] < min)
								min = c[k][i - 1];
						c[j][i] = min + 1;
					}

			min = 1001;
			for (int i = 0; i < ns; i++)
				if (c[i][nq - 1] < min)
					min = c[i][nq - 1];

			cout << "Case #" << t + 1 << ": " << min << endl;
		}
		else
			cout << "Case #" << t + 1 << ": " << 0 << endl;
	}
}
