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
	int i, j, k, l, m, cnt, t;
	char type[8];

	struct tnode
	{
		char type;
		int pos;
	};

	vector<tnode> seq;

	scanf ("%d", &nTestCases);
	for (i=1; i<=nTestCases; ++i)
	{
		scanf ("%d", &cnt);

		seq.clear();

		for (j=0; j<cnt; ++j)
		{
			tnode n;
			scanf ("%s%d", type, &t);

			n.type = 'B';
			if (type[0] == 'O')
				n.type = 'O';
			n.pos = t;

			seq.push_back(n);
		}

		int opos=1, bpos=1, cmove=0, totaltime=0;
		vector<tnode>::iterator it=seq.begin();

		char pm=(*it).type, cm=(*it).type;
		for (; it!=seq.end(); ++it)
		{
			cm = (*it).type;
			t=0;
			if ((*it).type == 'O')
			{
				t += abs((*it).pos - opos) + 1;
				if (pm == cm)
					cmove += abs((*it).pos - opos) + 1;
				else
				{
					t -= std::min(cmove, abs((*it).pos - opos));
					cmove = t;//abs((*it).pos - opos) + 1;
				}

				totaltime += t;

				opos = (*it).pos;
			}
			else
			{
				t += abs((*it).pos - bpos) + 1;
				if (pm == cm)
					cmove += abs((*it).pos - bpos) + 1;
				else				
				{
					t -= std::min(cmove, abs((*it).pos - bpos));
					cmove = t;//abs((*it).pos - bpos) + 1;
				}
				
				totaltime += t;

				bpos = (*it).pos;
			}

			if (pm != cm)
			{
				//totaltime -= cmove;
				//cmove = 0;
			}

			pm = cm;
		}



		printf ("Case #%d: %d\n", i, totaltime); 
	}

	return 0;
}

