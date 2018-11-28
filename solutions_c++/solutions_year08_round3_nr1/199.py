#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	FILE *fin = fopen("a.in", "r");
	ofstream fout("a.out");
	
	int T;
	fscanf(fin, "%d ", &T);

	for (int t = 1 ; t <= T ; ++t)
	{
		int p, k, l;
		vector<int> f;
		f.clear();

		fscanf(fin, "%d %d %d ", &p, &k, &l);

		for (int i = 0 ; i < l ; ++i)
		{
			int a;
			fscanf(fin, "%d ", &a);
			f.push_back(a);
		}

		if (p*k >= l)
		{
			sort(f.begin(), f.end(), greater<int>());
		
			long long result = 0;

			int freq = 0;
			for (int i = 0 ; i < l ; ++i)
			{
				if (i%k == 0)
					++freq;

				result += (long long)freq*(long long)f[i];
			}

			fout << "Case #" << t << ": " << result << endl;
		}
		else
		{
			fout << "Case #" << t << ": Impossible" << endl;
		}
	}

	fclose(fin);
	fout.close();
}
