#include <stdio.h>
#include <string.h>

bool lastAppear(int engine_num, int array_len, int* array, int& index, int& position)
{
	int* array_count = new int [engine_num];

	int i, j;
	for(j=0; j<engine_num; j++)
	{
		for(i=0; i<array_len; i++)
		{
			if(array[i] == j)
				break;
		}
		if(i != array_len)
			array_count[j] = i;
		else
			array_count[j] = -1;
	}

	int max_index=-1, max_value=0;
	for(j=0; j<engine_num; j++)
	{
		if(array_count[j] == -1)
		{
			index = j;
			position = -1;
			return true;
		}
		if(array_count[j] > max_value)
		{
			max_index = j;
			max_value = array_count[j];
		}
	}
	index = max_index;
	position = max_value;

	delete[] array_count;
	return true;
}

int main(int argc, char** argv)
{
	if(argc < 2)
		return -1;
	char filename[100];
	strcpy(filename, argv[1]);
	FILE *ifile = fopen(filename, "r");
	FILE *ofile = fopen("test.txt", "w");

	int case_num;
	fscanf(ifile, "%d\n", &case_num);

	int i, j, k;
	for(i=0; i<case_num; i++)
	{

		if(i==8)
			i=i;

		// parse engine
		int engine_num;
		fscanf(ifile, "%d\n", &engine_num);
		char* engine_name[100];
//		printf("%d\n", engine_num);
		for(j=0; j<engine_num; j++)
		{
			char tempstr[101];
			fgets(tempstr, 101, ifile);
			engine_name[j] = new char [strlen(tempstr)+1];
			strcpy(engine_name[j], tempstr);
			engine_name[j][strlen(engine_name[j])-1] = '\0';
//			printf("%s\n", engine_name[j]);
		}

		// parse query
		int query_num;
		fscanf(ifile, "%d\n", &query_num);
		int query[1000];
		for(j=0; j<query_num; j++)
		{
			char tempstr[101];
			fgets(tempstr, 101, ifile);
			tempstr[strlen(tempstr)-1] = '\0';
			for(k=0; k<engine_num; k++)
			{
				if(strcmp(engine_name[k], tempstr)==0)
					break;
			}
			if(k!=engine_num)
				query[j] = k;
			else
			{
				printf("error!");
				return -1;
			}
		}

		// prepare
		int *engine_temp = new int[engine_num];
		int engine_count = engine_num;
		for(j=0; j<engine_num; j++)
			engine_temp[j] = 1;

		// go
		int try_count=0;
		int index, position, offset=0;
		do{
			lastAppear(engine_num, query_num-offset, query+offset, index, position);
			if(position != -1 )
			{
				offset += position;
				if(offset > query_num)
					break;
				try_count++;
			}
		}while(position != -1 && offset <= query_num);
		fprintf(ofile, "Case #%d: %d\n", i+1, try_count);

		// end
		delete[] engine_temp;
		for(j=0; j<engine_num; j++)
			delete[] engine_name[j];
	}

	fclose(ifile);
	fclose(ofile);
	return 1;
}