#include <stdio.h>
#include <iostream>
#include <math.h>
using namespace std;

int main() {
	int t,n;
	FILE *fp1, *fp2;
	int a[1000],b[1000],iscount;
	fp1 = fopen("C:\\Users\\zerosumi\\Project\\gcj2010\\Debug\\C-large.in", "r");
	fp2 = fopen("C:\\Users\\zerosumi\\Project\\gcj2010\\Debug\\a.out.txt", "w+");

	fscanf(fp1, "%d", &t);
	for (int i = 1; i <= t; i++)
	{
		iscount = 0;
		fscanf(fp1, "%d", &n);
		for (int j = 0; j < n; j++)
		{
			fscanf(fp1, "%d %d", &a[j], &b[j]);
			for (int k = 0; k < j; k++)
			{
				if ( (a[j]-a[k]) * (b[j]-b[k]) < 0 )
				{
					iscount++;
				}
			}
		}
		fprintf(fp2, "Case #%d: %d\n", i, iscount);
	}
}