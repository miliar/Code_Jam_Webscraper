#include <cstdio>
#include <cstring>

#define INPUT_FILE "D-large.in"

using namespace std;

int main()
{
	FILE* fin=fopen(INPUT_FILE,"r");
	char output_file[1024];
	strcpy(output_file,INPUT_FILE);
	strcpy(strrchr(output_file,'.'),".out");
	FILE* fout=fopen(output_file,"w");

	int num_cases;
	fscanf(fin,"%d",&num_cases);
	for(int k=0;k<num_cases;++k)
	{
		int num_elements,not_in_place=0;
		fscanf(fin,"%d",&num_elements);

		for(int i=1;i<=num_elements;++i)
		{
			int elem;
			fscanf(fin,"%d",&elem);
			if(elem!=i) ++not_in_place;
		}

		fprintf(fout,"Case #%d: %d.000000\n",k+1,not_in_place);
		printf("Case #%d: %d.000000\n",k+1,not_in_place);
	}

	fclose(fout);
	fclose(fin);
	return 0;
}
