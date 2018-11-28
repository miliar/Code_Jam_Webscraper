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
		vector<int> cs;
		fscanf (f, " %d", &l);
		int j;
		for (j=0; j<l; j++)
		{
			int k;
			fscanf (f, " %d", &k);
			cs.push_back(k);
			//printf ("%d ", cs.back());
		}
		//printf ("\n");


		//search
		int n = 1<<cs.size();
		int min = -1;
		for (j=1; j<n-1; j++)
		{
			int sig[2];
			int sc[2];
			sig[0] = sig[1] = 0;
			sc[0] = sc[1] = 0;
			int k;
			for (k=0; k<cs.size(); k++)
			{
				int take = ( (j & (1<<k)) > 0);
				sig[take] ^= cs[k];
				sc[take] += cs[k];
			}
			if (sig[0] == sig[1] && sc[0] > min)
			{
				min = sc[0];
			}
		}
		
		
		
		if (min >= 0)
		{
			printf ("Case #%d: %d\n", i+1, min);
		}
		else
		{
			printf ("Case #%d: NO\n", i+1);
		}
	}
	return 0;
}


