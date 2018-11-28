#include <stdio.h>
#include <math.h>

bool prob1(int nN, int nK);

int main(void)
{
	FILE *fp;
	FILE *fpo;
	
	int nT;
	int nN;
	int nK;

	int i;
	bool flag;

	fp = fopen("A-large.in.txt", "r");
	fpo = fopen("output_inwq_prob1_large.out.txt", "w");


	fscanf(fp, "%d\a", &nT);

	for (i = 0; i < nT; i++)
	{
		fscanf(fp, "%d %d\n", &nN, &nK);
		flag = prob1(nN, nK);
		if (flag)
		{
			fprintf(fpo, "Case #%d: ON\n", i+1);
		}
		else
		{
			fprintf(fpo, "Case #%d: OFF\n", i+1);
		}
	}

	fclose(fp);
	fclose(fpo);

	return 0;
}

bool prob1(int nN, int nK)
{
	int fN;
	int rt;

	fN = int(pow(2, nN));
	rt = nK % fN;

	if (rt == fN-1)
	{
		return true;
	}
	else
	{
		return false;
	}
}
