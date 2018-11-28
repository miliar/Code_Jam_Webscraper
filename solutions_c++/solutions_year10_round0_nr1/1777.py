#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <climits>
#include <algorithm>
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int T, n, k;
	FILE *in=fopen("infile.txt", "r");
	FILE *out=fopen("outfile.txt", "w");
	fscanf(in, "%d", &T);
	for(int i=0; i<T; i++)
	{
		fscanf(in, "%d%d", &n, &k);
		bool on=true;
		for(int j=0; j<n; j++)
		{
			if(k%2==0)
				on=false;
			k/=2;
		}
		if(on)
		{
			fprintf(out, "Case #%d: ON\n", i+1);
		}
		else
			fprintf(out, "Case #%d: OFF\n", i+1);
	}
	return 0;
}