
#include "stdafx.h"
#include <algorithm>
#include <list>
#include <map>
#include <set>

int _tmain(int argc, _TCHAR* argv[])
{
    FILE * fIn = fopen("test.in", "r");
    FILE * fOut = fopen("test.out", "w");

    int nTests = 0;
    fscanf(fIn, "%d", &nTests);
    printf("%d tests\n", nTests);

    for (int iTest = 1; iTest <= nTests; iTest++)
    {
		printf ("\nTest %d:", iTest);
		
		// Clear data structures
		typedef std::map<char, char> TComb;
		typedef std::map<char, TComb> TCombs;
		TCombs Combs;
		typedef std::map<char, std::set<char>> TOpps;
		TOpps Opps;

		// Read input
		int c, d, n;
		fscanf(fIn, "%d", &c);
		for (int i = 0; i < c; ++i)
		{
			char C[4];
			fscanf(fIn, "%s", &C);
			Combs[C[0]][C[1]] = C[2];
			Combs[C[1]][C[0]] = C[2];
		}
		
		fscanf(fIn, "%d", &d);
		for (int i = 0; i < d; ++i)
		{
			char D[3];
			fscanf(fIn, "%s", &D);
			Opps[D[0]].insert(D[1]);
			Opps[D[1]].insert(D[0]);
		}
		
		fscanf(fIn, "%d", &n);
		printf ("(%d %d %d)\n", c, d, n);
		
		char N[100];
		fscanf(fIn, "%s", &N);
		
		// Invoke the string
		char out[101];
		memset(out, 0, 101);
		int iout = -1; // last char
		for (int i = 0; i < n; i++)
		{
			char ch = N[i];

			// Check for a combination
			bool bComb = false;
			TCombs::const_iterator citer1 = Combs.find(ch);
			if (citer1 != Combs.end() && i > 0) 
			{
				TComb::const_iterator citer2 = citer1->second.find(out[iout]);
				if (citer2 != citer1->second.end())
				{
					//printf("Replacing %c%c with %c\n", citer2->first, ch, citer2->second);
					out[iout] = citer2->second;
					bComb = true;
				}
			}
			// Append the char as is
			if (!bComb)
				out[++iout] = ch;
			//printf("New string: %s\n", out);

			// Check for an opposition
			TOpps::const_iterator oiter1 = Opps.find(out[iout]);
			if (oiter1 != Opps.end())
			{
				printf("Matched end %c\n", out[iout]);
				// We found the end, look for one of the possible beginnings
				for (std::set<char>::const_iterator setiter = oiter1->second.begin();
					setiter != oiter1->second.end(); setiter++)
				{
					// If we find a beginning, truncate the string
					char *first = strchr(out, *setiter);
					if (first)
					{
						//printf("Matched %c to %c. ", *first, out[iout]);
						//iout = first - out - 1;
						iout = -1;
						//printf("moving to %d\n", iout);
						memset(out + iout+1, 0, 99 - iout);
						//printf("New string: %s\n", out);
						break;
					}
				}
			}
		}

		fprintf(fOut, "Case #%d: [", iTest);
		for (char *ch = out; *ch; ch++)
		{
			if (ch != out) fprintf(fOut, ", ");
			fprintf(fOut, "%c", *ch);
		}
		fprintf(fOut, "]\n");
	}

	return 0;
}

