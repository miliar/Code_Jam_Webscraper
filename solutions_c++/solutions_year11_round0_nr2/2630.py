#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <assert.h>

using namespace std;

int main(int argc, char** argv) 
{
	FILE *f = fopen (argv[1], "rt");
	if (!f) return 0;
	
	int n;
	fscanf (f, "%d", &n);
	int i;
	for (i=0 ; i<n; i++)
	{
		int l;
		vector<vector<char> > trans;
		vector<vector<char> > disap;
		vector<char> train;

		fscanf (f, " %d", &l);
		int j;
		for (j=0; j<l; j++)
		{
			char c1,c2,c3;
			fscanf (f, " %c%c%c", &c1, &c2, &c3);
			vector<char> _t;
			_t.push_back(c1);
			_t.push_back(c2);
			_t.push_back(c3);
			trans.push_back (_t);
			//printf ("%c%c%c ", trans.back()[0], trans.back()[1], trans.back()[2]);
		}
		//printf ("\n");

		fscanf (f, " %d", &l);
		for (j=0; j<l; j++)
		{
			char c1,c2;
			fscanf (f, " %c%c", &c1, &c2);
			vector<char> _t;
			_t.push_back(c1);
			_t.push_back(c2);
			disap.push_back (_t);
			//printf ("%c%c ", disap.back()[0], disap.back()[1]);
		}
		//printf ("\n");

		fscanf (f, " %d", &l);
		char c1;
		fscanf (f, " %c", &c1);
		train.push_back (c1);
		//printf ("%c", train.back());
		for (j=1; j<l; j++)
		{
			fscanf (f, "%c", &c1);
			train.push_back (c1);
			//printf ("%c", train.back());
		}
		//printf ("\n");

		//run 
		vector<char> bch;
		for (j=0; j<train.size(); j++)
		{
			bch.push_back (train[j]);
			
			//trans
			while (true)
			{
				int k;
				bool transed = false;
				for (k=0; k<trans.size(); k++)
				{
					if (bch.size() >= 2 && 
						((bch.back() == trans[k][0] && bch[bch.size()-2] == trans[k][1]) |
						 (bch.back() == trans[k][1] && bch[bch.size()-2] == trans[k][0])))
					{
						bch.pop_back();
						bch.pop_back();
						bch.push_back (trans[k][2]);
						transed = true;
						break;
					} 
				}
				if (!transed) break;
			}

			//disap
			int k;
			assert (bch.size() > 0);
			for (k=0; k<disap.size(); k++)
			{
				if (disap[k][0] == bch.back() || disap[k][1] == bch.back())
				{
					char to = (disap[k][0] == bch.back()) ? disap[k][1] : disap[k][0];
					int l;
					for (l=0; l<bch.size()-1; l++)
					{
						if (to == bch[l])
						{
							bch.clear();
							break;
						}
					}
				}
				if (bch.size() == 0) break;
			}
		}


		printf ("Case #%d: [", i+1);
		for (j=0; j<bch.size(); j++)
			printf ("%s%c", j ? ", " : "", bch[j]);
		printf ("]\n");
	}
	return 0;
}
