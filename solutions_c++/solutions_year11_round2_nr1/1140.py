#include <stdio.h>


int a[200][200];

int main()
{
	int t, n;
	int cnt = 0;
	FILE *fout = fopen("out.out", "w");

	scanf("%d", &t);
	while(t--)
	{
		char chr[200];
		double wp[200], owp[200], oowp[200];
		int ww[200], ll[200];

		scanf("%d", &n);
		for(int i=0; i<n; i++)
		{
			scanf("%s", &chr);
			for (int j=0; j<n; j++)
				if (chr[j] == '1')
					a[i][j] = 1;
				else if (chr[j] == '0')
					a[i][j] = 0;
				else 
					a[i][j] = -1;
		}

// wp
		for (int i=0; i<n; i++)
		{
			int w = 0; int l = 0;
			for (int j=0; j<n; j++)
			{
				if (a[i][j] == 1) w++;
				if (a[i][j] == 0) l++;
			}

			if (w + l)
				wp[i] = (w * 1.0) / (w + l);
			else 
				wp[i] = 0;

			ww[i] = w;
			ll[i] = l;
		}
		
// owp
		for (int i=0; i<n; i++)
		{
			owp[i] = 0;
			int opponents = 0;
			for (int j=0; j<n; j++)
				if (a[i][j] != -1)
				{
					opponents++;
					if (a[i][j] == 0)
						owp[i] = owp[i] + (ww[j] - 1.0)  / (ww[j] + ll[j] - 1.0);
					else 
						owp[i] = owp[i] + ww[j]  / (ww[j] + ll[j] - 1.0);
				}
			if (opponents)
				owp[i] = owp[i] / opponents;
		}

// oowp
		for (int i=0; i<n; i++)
		{
			oowp[i] = 0;
			int opponents = 0;
			for (int j=0; j<n; j++)
				if (a[i][j] != -1)
				{
					opponents++;
					oowp[i] = oowp[i] + owp[j];
				}
			if (opponents)
				oowp[i] = oowp[i] / opponents;
		}

		fprintf(fout, "Case #%d:\n", ++cnt);
		for (int i=0; i<n; i++)
			fprintf(fout, "%0.10lf\n", wp[i] * 0.25 + 0.5 * owp[i] + 0.25 * oowp[i]);
	}

	fclose(fout);

	return 0;
}