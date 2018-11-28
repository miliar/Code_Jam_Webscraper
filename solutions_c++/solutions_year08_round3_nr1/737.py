#include <stdio.h>
#include <iostream>

int GetMax(int *ar, int leng)
{
	int max_num = -1, max_index = -1;
	int i;
	for(i=0; i<leng; i++)
	{
		if(ar[i] > max_num)
		{
			max_num = ar[i];
			max_index = i;
		}
	}
	ar[max_index] = -1;
	return max_num;
}

bool BadSort(int *ar, int leng)
{
	int *temp_ar = new int [leng];
	int i;
	for(i=0; i<leng; i++)
		temp_ar[i] = GetMax(ar, leng);
	for(i=0; i<leng; i++)
		ar[i] = temp_ar[i];
	return true;
}

int main(int argv, char** argc)
{
	if( argv < 2 )
		return -1;
	FILE *ifile = fopen(argc[1], "r");
	FILE *ofile = fopen("temp.txt", "w");

	int casenum;
	int i,j,k;
	fscanf(ifile, "%d\n", &casenum);

	for(i=0; i<casenum; i++)
	{
		int l_k, keys, letter;
		fscanf(ifile, "%d %d %d\n", &l_k, &keys, &letter);

		int *letters = new int[letter];
		for(j=0; j<letter; j++)
			fscanf(ifile, "%d", &letters[j]);
		BadSort(letters, letter);

		int key_stoke = 0;
		for(j=0; j<letter; j++)
			key_stoke += letters[j]*(j/keys+1);
		fprintf(ofile, "Case #%d: %d\n", i+1, key_stoke);
	}

	fclose(ifile);
	fclose(ofile);
}
