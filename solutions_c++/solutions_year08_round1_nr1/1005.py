#include <stdio.h>
#include <conio.h>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	FILE *fin = fopen("A-small-attempt1.in", "rt");
	FILE *fout = fopen("A-small-attempt1.out", "wt");

	int T;
	fscanf(fin, "%d", &T);

	for (int c = 0; c < T; c++)
	{
		vector<int> v1, v2;

		int n;
		fscanf(fin, "%d", &n);
		v1.resize(n);
		v2.resize(n);

		for (int i = 0; i < n; i++)
			fscanf(fin, "%d", &v1[i]);
		for (int i = 0; i < n; i++)
			fscanf(fin, "%d", &v2[i]);

		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());

		int v1first = 0, v1last = n - 1;
		int v2first = 0, v2last = n - 1;

		long long scalar = 0;
		while (v1first <= v1last)
		{
			if (v1[v1first] < 0)
			{
				scalar += v1[v1first] * v2[v2last];
				v1first++; v2last--;
			}
			else if (v1[v1first] >= 0)
			{
				scalar += v1[v1last] * v2[v2first];
				v1last--;
				v2first++;
				/*v1.pop_back();
				v2.erase(v2.begin());*/
			}
		}

		//fprintf(stdout, "Case #%d: %lld\n", c+1, scalar);
		fprintf(fout, "Case #%d: %lld\n", c+1, scalar);
	}

	fclose(fin);
	fclose(fout);
}