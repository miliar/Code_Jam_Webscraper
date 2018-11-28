#include <stdio.h>

int f[1000];

int kkk = 0;
int b[100];

void set(int n, int l)
{
	int i;

	if (n==l)
	{
		int k=l;
		int cnt;
		while (1)
		{
			cnt=0;
			for (int j=2; j<=k; j++)
				cnt += b[j];
			if (b[cnt]==1)
				k=cnt;
			else break;
		}
		if (cnt==1)
		{
			kkk++;
		}

		return;
	}

	for (int i=0; i<2; i++)
	{
		b[n]=i;
		set(n+1, l);
	}
}

int main()
{
	FILE *fout = fopen("c.out","w");
	int caseN;
	scanf("%d",&caseN);

	for (int i=2; i<=25; i++) {
		kkk = 0;
		b[i] = 1;
		set(2, i);
		f[i] = kkk % 100003;
	}
	for (int caseID=1; caseID<=caseN; caseID++)
	{
		int n;
		scanf("%d",&n);

		fprintf(fout, "Case #%d: %d\n", caseID, f[n]);
	}

	fclose(fout);
	return 0;
}