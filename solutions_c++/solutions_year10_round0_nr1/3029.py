
#include <stdio.h>
#include <stdlib.h>

int main()
{
	int n=2, k=4, isOn=1, t=0;

	FILE *fl = fopen("A-small-in.in", "r");
	fscanf(fl, "%d", &t);
	
	FILE *fl2 = fopen("A-small.out", "w");

	for (int p=0; p < t; p++)
	{
	
		fscanf(fl, "%d", &n);
		fscanf(fl, "%d", &k);

		int w=1;
		for (int i=0; i < n; i++)
			w *= 2;
		if ((k % w) == (w-1))
			isOn = 1;
		else
			isOn = 0;

		if (isOn)
			fprintf(fl2, "Case #%d: ON\n", p+1);
		else
			fprintf(fl2, "Case #%d: OFF\n", p+1);
	}


	return 0;
}
