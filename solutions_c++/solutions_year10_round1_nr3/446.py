#include <stdio.h>
#include <iostream>
#include <math.h>
using namespace std;

int main() {
	int t,a1,a2,b1,b2;
	FILE *fp1, *fp2;
	int tempa,tempb,slt;

	fp1 = fopen("C-small.in", "r");
	fp2 = fopen("a.out.txt", "w+");

	int results, temp, count;
	fscanf(fp1, "%d", &t);
	for (int i = 1; i <= t; i++)
	{
		slt = 0;
		fscanf(fp1, "%d %d %d %d", &a1, &a2, &b1, &b2);
		for (int j = a1; j <= a2; j++)
		{
			for (int k = b1; k <= b2; k++)
			{
				tempa = j > k ? j : k;
				tempb = j > k ? k : j;
				count = 0;
				while (tempb > 0 && tempa > 0)
				{
					results = floor((float)tempa / (float)tempb);
					temp = tempb;
					tempb = tempa - results * temp;
					tempa = temp;
					count ++;
					if (count % 2 == 1 && results > 1)
					{
						slt++;
						break;
					}
					if (count % 2 == 0 && results > 1)
					{
						break;
					}
				}
			}
		}
		fprintf(fp2, "Case #%d: %d\n", i, slt);
	}
}