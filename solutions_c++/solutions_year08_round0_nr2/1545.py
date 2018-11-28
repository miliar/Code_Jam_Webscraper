#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TYPE_NA  1
#define TYPE_NB  2

struct train_line
{
	int start;
	int end;
	int type;
	bool reuse;
};

int main(void)
{
	FILE *fp1;
	char oneword[100];
	char *c;
	int num_test;
	int test;
	int i, j, index = 0, ptr = 0;

	int turn_around = 0, NA, NB;
	int start_m, start_s, end_m, end_s;
	struct train_line lines[200];
	struct train_line tmp;
	int num_na, num_nb;

	fp1 = fopen("in.txt", "r");
	if (fp1 == NULL)
	{
		printf("File failed to open\n");
		exit (EXIT_FAILURE);
	}

	fscanf(fp1, "%d", &num_test);
	for (test=0; test<num_test; test++)
	{
		fscanf(fp1, "%d", &turn_around);
		c = fgets(oneword, 100, fp1);  /* get one line from the file */
		fscanf(fp1, "%d %d", &NA, &NB);
		c = fgets(oneword, 100, fp1);  /* get one line from the file */
		index = 0;
		for (i=0; i<NA; i++)
		{
			fscanf(fp1, "%d:%d %d:%d", &start_m, &start_s, &end_m, &end_s);
			c = fgets(oneword, 100, fp1);  /* get one line from the file */
			lines[index].start = start_m*60 + start_s;
			lines[index].end = end_m*60 + end_s;
			lines[index].type = TYPE_NA;
			lines[index].reuse = false;
			index++;
		}
		for (i=0; i<NB; i++)
		{
			fscanf(fp1, "%d:%d %d:%d", &start_m, &start_s, &end_m, &end_s);
			c = fgets(oneword, 100, fp1);  /* get one line from the file */
			lines[index].start = start_m*60 + start_s;
			lines[index].end = end_m*60 + end_s;
			lines[index].type = TYPE_NB;
			lines[index].reuse = false;
			index++;
		}

		// sort lines, bubble sort
		for (i=0; i<index; i++)
		{
			for (int j=index-1; j>=i+1; j--)
			{
				if ( lines[j-1].start > lines[j].start )
				{
					//swap
					tmp = lines[j];
					lines[j] = lines[j-1];
					lines[j-1] = tmp;
				}
			}
		}

		index = 0;
		while ( index < (NA+NB) )
		{
			if ( lines[index].reuse )
			{
				index++;
				continue;
			}
			ptr = index;
			for (i=ptr+1; i<(NA+NB); i++)
			{
				if ( lines[i].reuse )
				{
					continue;
				}
				if ( lines[ptr].type == lines[i].type )
				{
					continue;
				}
				if ( (lines[ptr].end + turn_around) <= lines[i].start )
				{
					lines[i].reuse = true;
					ptr = i;
				}
			}
			index++;
		}

		num_na = 0;
		num_nb = 0;
		for (i=0; i<(NA+NB); i++)
		{
			if ( lines[i].reuse == false )
			{
				if ( lines[i].type == TYPE_NA )
				{
					num_na++;
				}
				else if ( lines[i].type == TYPE_NB )
				{
					num_nb++;
				}
			}
		}

		printf("Case #%d: %d %d\n", test+1, num_na, num_nb);
	}

	fclose(fp1);

	return 0;
}
