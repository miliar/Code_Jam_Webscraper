#include<stdio.h>
#include<string.h>
#define MAX_STRING 100
#define MAX_INPUT 100
#define MAX_QUERY 1000
int query[MAX_QUERY];
int engine_count, query_count;

int beginSearch()
{
	int pass_count[MAX_INPUT];
	
	int i,j, all_count = 0;
	int switch_time = 0;
	for(i = 0; i < engine_count; i++)
	{
		pass_count[i] = 0;
	}
	for(i = 0; i < query_count; i++)
	{
		if(pass_count[query[i]] == 0)
		{
			pass_count[query[i]] = 1;
			all_count++;
			if(all_count >= engine_count)
			{
				switch_time++;
				for(j = 0; j < engine_count; j++)
					pass_count[j] = 0;
				pass_count[query[i]] = 1;
				all_count = 1;
			}
		}
	}
	return switch_time;
}

int main()
{
	FILE *fin, *fout;
	int i,j,k,n,l;
	char seng_name[MAX_INPUT][MAX_STRING + 1];
	char temp[MAX_STRING + 1];
	

	fin = fopen("A-large.in", "r");
	fout = fopen("out.out", "w");
	fscanf(fin, "%d", &n);

	for(i = 0; i < n; i++)
	{
		fscanf(fin, "%d", &engine_count);
		fgets(seng_name[0], MAX_STRING, fin);
		for(j = 0; j < engine_count; j++)
		{
			//fscanf(fin, "%s\n", seng_name[j]);
			fgets(seng_name[j], MAX_STRING, fin);
		}

		fscanf(fin, "%d", &query_count);
		fgets(temp, MAX_STRING, fin);
		for(j = 0; j < query_count; j++)
		{
			//fscanf(fin, "%s", temp);
			fgets(temp, MAX_STRING, fin);
			for(k = 0; k < engine_count; k++)
			{
				l = strcmp(seng_name[k], temp);
				if(l == 0)
				{
					query[j] = k;
					break;
				}
			}
		}
		for(j = 0; j < engine_count; j++)
			printf("%s\n", seng_name[j]);
		for(j = 0; j < query_count; j++)
			printf("%d ", query[j]);
		printf("\n");
		//printf("Switch time = %d\n", beginSearch());
		fprintf(fout, "Case #%d: %d\n", i + 1,beginSearch());
	}
	fclose(fout);
	fclose(fin);
}