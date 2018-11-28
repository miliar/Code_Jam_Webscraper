#include <iostream>
#include <stdio.h>
#include <set>
#include <map>
#include <list>
#include <algorithm>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int nTestCases;
	int i, j, k, l, m;
	int C, D, N, ostri;
	char tarr[256], tarr1[256];
	char ostr[512];

	map<string, char> combine;
	bool opposed[256][256];
	string tstr;

	scanf ("%d", &nTestCases);
	for (i=1; i<=nTestCases; ++i)
	{
		scanf ("%d", &C);
		combine.clear();
		
		memset(opposed, 0, sizeof(opposed));
		memset(ostr, 0, sizeof(ostr));

		for (j=0; j<C; ++j)
		{
			scanf ("%s", tarr);

			strcpy(tarr1, tarr);
			tarr1[2] = '\0';
			combine.insert(make_pair(string(tarr1), tarr[2]));
			tarr1[0] = tarr[1];
			tarr1[1] = tarr[0];
			combine.insert(make_pair(string(tarr1), tarr[2]));
		}

		scanf ("%d", &D);
		for (j=0; j<D; ++j)
		{
			scanf ("%s", tarr);

			opposed[tarr[0]][tarr[1]] = true;
			opposed[tarr[1]][tarr[0]] = true;

		}

		scanf ("%d", &N);
		scanf ("%s", tarr);

		ostr[0] = tarr[0];
		ostri = 0;
		for (j=1; j<N; ++j)
		{
			tarr1[0] = ostr[ostri];
			tarr1[1] = tarr[j];
			tarr1[2] = '\0';

			map<string, char>::iterator it=combine.find(tarr1);
			if (it != combine.end())
			{
				ostr[ostri] = (*it).second;
				continue;
			}

			for (k=0; k<=ostri; ++k)
			{
				if (opposed[ostr[k]][tarr[j]])
					break;
			}

			if (k <= ostri)
			{
				ostri=0;
				ostr[ostri] = '\0';

				if (j == N-1)
					break;

				ostr[ostri] = tarr[j+1];
				++j;
				continue;
			}

			ostr[++ostri] = tarr[j];
		}

		ostr[++ostri] = '\0';

		printf ("Case #%d: [", i);

		if (ostr[0] != '\0')
			printf ("%c", ostr[0]);
		for (j=1; j<ostri; ++j)
			printf (", %c", ostr[j]);

		printf ("]\n");
	}

	return 0;
}