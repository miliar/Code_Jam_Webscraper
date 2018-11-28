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
		fscanf (f, " %d", &l);
		vector<int> seq;
		int j;
		for (j=0; j<l; j++)
		{
			char c;
			fscanf (f, " %c", &c);
			int t;
			fscanf (f, " %d", &t);
			assert (t>= 1 && t<=100 && (c=='O' || c=='B'));
			if (c == 'O') seq.push_back(t);
			else seq.push_back(-t);
			//printf ("%d ", seq.back());
		}
		//printf ("\n");

		int t[2];
		int p[2];
		t[0] = t[1] = 0;
		p[0] = p[1] = 1;
		int curt = 0;

		for (j=0; j<seq.size(); j++)
		{
			if (seq[j] > 0)
			{
				int dif = abs(seq[j] - p[0]);
				int nt = t[0] + dif + 1;
				p[0] = seq[j];
				if (nt <= curt)  nt = curt+1;
				curt = nt;
				t[0] = nt;
			}
			else
			{
				int loc = -seq[j];
				int dif = abs(loc - p[1]);
				int nt = t[1] + dif + 1;
				p[1] = loc;
				if (nt <= curt)  nt = curt+1;
				curt = nt;
				t[1] = nt;
			}
		}
		printf ("Case #%d: %d\n", i+1, curt);
	}
	return 0;
}
