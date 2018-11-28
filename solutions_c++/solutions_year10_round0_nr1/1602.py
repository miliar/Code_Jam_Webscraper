#include <stdio.h>

void main()
{
	FILE* fp = NULL;
	FILE* outfp = NULL;
	fopen_s(&fp, "A-large.in", "r");
	fopen_s(&outfp, "A-large.out", "w");
	if(fp)
	{
		int T;
		fscanf_s(fp, "%d", &T);
		for(int i=0;i<T;++i)
		{
			int N, K;
			fscanf_s(fp, "%d %d", &N, &K);
			int Mask = 1;
			Mask <<= N;
			Mask -= 1;
			if(Mask == (K & Mask))
			{
				fprintf(outfp, "Case #%d: ON\n", i+1);
			}
			else
			{
				fprintf(outfp, "Case #%d: OFF\n", i+1);
			}
		}
		fclose(fp);
		fclose(outfp);
	}
}

