#include <cstdio>
#include <climits>
#include <cstring>

#include <memory.h>

#define INPUT_FILE "C-large.in"

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
		int num_candies;
		int candy_value[10000];
		fscanf(fin,"%d",&num_candies);

		int total_xor=0,total_add=0,smallest=INT_MAX;
		for(int i=0;i<num_candies;++i)
		{
			fscanf(fin,"%d",&candy_value[i]);
			total_xor^=candy_value[i];
			total_add+=candy_value[i];
			if(smallest>candy_value[i]) smallest=candy_value[i];
		}

		if(total_xor==0)
		{
			printf("Case #%d: %d %d\n",k+1,total_add-smallest,smallest);
			fprintf(fout,"Case #%d: %d\n",k+1,total_add-smallest);
		} else {
			printf("Case #%d: NO\n",k+1);
			fprintf(fout,"Case #%d: NO\n",k+1);
		}
	}

	fclose(fout);
	fclose(fin);
	return 0;
}
