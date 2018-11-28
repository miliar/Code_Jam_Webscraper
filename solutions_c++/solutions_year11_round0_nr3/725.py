#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const int MAX = 1005;
int n;

int main()
{
	FILE *f1 = fopen("input.in", "r");
	FILE *f2 = fopen("out.in", "w");
	int numcas;
	fscanf(f1, "%d", &numcas);
	for(int cas = 1; cas <= numcas; cas ++)
	{
		fscanf(f1, "%d", &n);
		int value, minvalue = -1, totvalue = 0, sumxor = 0;
		for(int i = 0; i < n; i ++)
		{
			fscanf(f1, "%d", &value);
			totvalue += value;
			if(minvalue == -1 || minvalue > value)
				minvalue = value;
			sumxor ^= value;
		}
		fprintf(f2, "Case #%d: ", cas);
		if(sumxor != 0)
			fprintf(f2, "NO\n");
		else
			fprintf(f2, "%d\n", totvalue-minvalue);
	}
	fclose(f1);
	fclose(f2);

	return 0;
}