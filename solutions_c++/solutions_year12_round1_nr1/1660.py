#include <stdio.h>
#include <malloc.h>

#define FEXIST() do { \
	if(fip) fclose(fip);\
	if(fop) fclose(fop);\
	if(proper) free(proper);\
	if(rightproper) free(rightproper);\
} while(0)

const int limits = 100;

float runcase(FILE *fip, float *errorproper)
{
	int typed, total;
	fscanf(fip, "%d%d", &typed, &total);
	errorproper[0] = 0;

	float tmp;
	for(int i = 1; i <= typed; ++i)
	{
		fscanf(fip, "%f", &tmp);
		errorproper[i] = 1.f - tmp * (1 - errorproper[i - 1]);
	}

	int complete = total + 1;
	float pmin = 1 + complete - (total - typed + 1);
	int index = -1;
	for (int i = 0; i <= typed; ++i)
	{
		tmp = 2 * i + errorproper[typed - i] * complete;
		if(tmp < pmin)
		{
			index = i;
			pmin = tmp;
		}
	}

	return pmin + total - typed + 1;
}

int main(int argc, char*argv[])
{
	FILE *fip, *fop;
	float *proper, *rightproper;

	rightproper = proper = NULL;
	fip = fop = NULL;

	if(argc != 3)
		return -1;

	if(!(fip = fopen(argv[1], "r")))
		return -1;

	if(!(fop = fopen(argv[2], "w")))
	{
		FEXIST();
		return -1;
	}

	proper = (float*)malloc(limits * sizeof(float));
	for(int i = 0; i < limits; ++i)
		proper[i] = 0.f;

	int cases;
	fscanf(fip, "%d", &cases);
	for(int i = 1; i <= cases; ++i)
	{
		fprintf(fop, "Case #%d: %f\n", i, runcase(fip, proper));
	}

	FEXIST();
	return 0;
}
