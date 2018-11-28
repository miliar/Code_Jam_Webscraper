#include <cstdio>
#include <cstring>

#include <memory.h>

#define INPUT_FILE "B-large.in"

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
		int num_cmb,num_opp,num_ivk;
		char cmb[36][10]={0};
		char opp[28][10]={0};
		char ivk[101];
		fscanf(fin,"%d",&num_cmb);
		for(int i=0;i<num_cmb;++i) fscanf(fin,"%s",cmb[i]);
		fscanf(fin,"%d",&num_opp);
		for(int i=0;i<num_opp;++i) fscanf(fin,"%s",opp[i]);
		fscanf(fin,"%d",&num_ivk);
		fscanf(fin,"%s",&ivk);

		int element_used['Z'+1]={0};
		char red[101];
		int num_red=0;
		for(int i=0;i<num_ivk;++i)
		{
			int j;
			if(num_red!=0)
			{
				for(j=0;j<num_cmb;++j)
				{
					if(	(cmb[j][0]==red[num_red-1] && cmb[j][1]==ivk[i]) ||
						(cmb[j][1]==red[num_red-1] && cmb[j][0]==ivk[i]))
					{
						--element_used[red[num_red-1]];
						red[num_red-1]=cmb[j][2];
						++element_used[red[num_red-1]];
						break;
					}
				}
				if(j!=num_cmb) continue;
				for(j=0;j<num_opp;++j)
				{
					if(	(element_used[opp[j][0]]!=0 && opp[j][1]==ivk[i]) ||
						(element_used[opp[j][1]]!=0 && opp[j][0]==ivk[i]))
					{
						num_red=0;
						red[0]=0;
						memset(element_used,0,sizeof(element_used));
						break;
					}
				}
				if(j!=num_opp) continue;
			}
			red[num_red++]=ivk[i];
			red[num_red]=0;
			element_used[ivk[i]]++;
		}
		printf("Case #%d: [",k+1);
		fprintf(fout,"Case #%d: [",k+1);
		for(int i=0;i<num_red;++i)
		{
			printf("%s%c",i==0?"":", ",red[i]);
			fprintf(fout,"%s%c",i==0?"":", ",red[i]);
		}
		printf("]\n");
		fprintf(fout,"]\n");
	}

	fclose(fout);
	fclose(fin);
	return 0;
}
