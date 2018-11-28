#include <iostream>
#include <stdio.h>
#include <fstream>
using namespace std;

int main()
{
	FILE* in = fopen("in", "r");
	FILE* out = fopen("out.txt", "w+");

	int t;
	int data[105][105];
	double wp[105];
	int wpn[105];
	double owp[105];
	double oowp[105];
	fscanf(in, "%d", &t);
	char ch;
	for (int cas = 1; cas <= t; cas++)
	{
		int n;
		fscanf(in, "%d", &n);
		for (int i = 0; i < n; i++)
		{
			//getchar();
			fscanf(in, "%c", &ch);
			for (int j = 0; j < n; j++)
			{
				//char ch = getchar();
				fscanf(in, "%c", &ch);
				if (ch == '1')
					data[i][j] = 1;
				else if (ch == '0')
					data[i][j] = 0;
				else
					data[i][j] = -1;
			}
		}

		for (int i = 0; i < n; i++)
		{
			int a = 0;
			int b = 0;
			for (int j = 0; j < n; j++)
			{
				if (data[i][j] == 1)
				{
					a++;
					b++;
				}
				else if (data[i][j] == 0)
				{
					b++;
				}
			}
			wpn[i] = b;
			wp[i] = (double)a/b;
		}
		for (int i = 0; i < n; i++)
		{
			double a = 0;
			int b = 0;
			for (int j = 0; j < n; j++)
			{
				if (data[i][j] != -1)
				{
					if (data[i][j] == 1)
						a+=wp[j]*(wpn[j])/(wpn[j] - 1);
					else
						a+=(wp[j]*(wpn[j]) - 1)/(wpn[j] - 1);
					b++;
				}
			}
			owp[i] = a/b;
		}
		for (int i = 0; i < n; i++)
		{
			double a = 0;
			int b = 0;
			for (int j = 0; j < n; j++)
			{
				if (data[i][j] != -1)
				{
					a+=owp[j];
					b++;
				}
			}
			oowp[i] = a/b;
		}
		fprintf(out, "Case #%d:\n", cas);
		for (int i = 0; i < n; i++)
			fprintf(out, "%.6f\n", (0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]));
	}
	
	fclose(in);
	fclose(out);

	printf("sefse\n");
	return 0;
}