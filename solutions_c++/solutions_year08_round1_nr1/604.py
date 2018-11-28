#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#include <algorithm>
using namespace std;

_int64 product(_int64 * v1, _int64 * v2, int size)
{
	_int64 re = 0;
	int i = 0;
	for(; i < size; i++)
		re += *(v1+i) * (*(v2+i));
	return re;
}
bool desc(_int64 a, _int64 b)
{
	return a > b;
}
_int64 permute(_int64 * v1, _int64 * v2, int size)
{
	_int64 x, y;
	sort(v1, v1+size);
	sort(v2, v2+size, desc);
	x = product(v1, v2, size);
	sort(v1, v1+size, desc);
	sort(v2, v2+size);
	y = product(v1, v2, size);
	return min(x, y);
}
int main()
{
	FILE * fin, * fout;
	int T, i, j, size;
	_int64 * v1, * v2;
	_int64 result;
	fin = fopen("A-large.in", "r");
	fout = fopen("A-large.out", "w");
	fscanf(fin, "%d", &T);
	for(i = 0; i < T; i++)
	{
		fscanf(fin, "%d", &size);
		v1 = (_int64 *)malloc(sizeof(_int64) * size);
		v2 = (_int64 *)malloc(sizeof(_int64) * size);
		for(j = 0; j < size; j++)
			fscanf(fin, "%I64d", v1+j);
		for(j = 0; j < size; j++)
			fscanf(fin, "%I64d", v2+j);
		result = permute(v1, v2, size);
		fprintf(fout, "Case #%d: %I64d\n", i+1, result); 
		free(v1);
		free(v2);
	}

	fclose(fin);
	fclose(fout);
	return 0;
}