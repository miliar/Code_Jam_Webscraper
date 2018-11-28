#include <stdio.h>
#include <string.h>
#include <stdlib.h>

	int counter[10], rcount[10];

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int t;
	int tc, it, ir;
	int val;
	int rc;
	fscanf(fp, "%d", &tc);
	for(t=1;t<=tc;t++)
	{
		fscanf(fp, "%d", &val);
		int jt=val;
		while(jt != 0)
		{
			it = jt % 10;
			if(it != 0)
				counter[it]++;
			jt = jt / 10;
		}
		for(rc=val+1; ; rc++)
		{
			int rt = rc;
			while(rt != 0)
			{
				ir = rt % 10;
				if(ir != 0)
					rcount[ir]++;
				rt = rt / 10;
			}
			int r = memcmp(rcount, counter, sizeof(int)*10);
			memset(rcount, 0, sizeof(int)*10);
			if( r == 0 )
				break;
		}
		fprintf(ofp, "Case #%d: %d\n", t, rc );
		memset(counter, 0, sizeof(int)*10);
	}
}