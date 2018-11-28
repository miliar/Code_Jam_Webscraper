#include <cstdio>
#include <climits>
#include <cstring>

#include <memory.h>

#define INPUT_FILE "A-large.in"

using namespace std;

int main()
{
	FILE* fin=fopen(INPUT_FILE,"r");
	char output_file[1024];
	char log_file[1024];
	strcpy(output_file,INPUT_FILE);
	strcpy(strrchr(output_file,'.'),".out");
	strcpy(log_file,INPUT_FILE);
	strcpy(strrchr(log_file,'.'),".log");
	FILE* fout=fopen(output_file,"w");
	FILE* flog=fopen(log_file,"w");

	int num_cases;
	fscanf(fin,"%d",&num_cases);
	for(int k=0;k<num_cases;++k)
	{
		int num_teams;
		fscanf(fin,"%d",&num_teams);

		int wins[100]={0},games[100]={0},matrix[100][100]={0};
		// matrix[i][j]=i against j: 1 win, 0 lose, -1 no game
		for(int i=0;i<num_teams;++i)
		{
			char buf[1024];
			fscanf(fin,"%s",buf);

			for(int j=0;j<num_teams;++j)
			{
				if(buf[j]=='1')
				{
					++wins[i];
					++games[i];
					matrix[i][j]=1;
				}
				if(buf[j]=='0')
				{
					++games[i];
					matrix[i][j]=0;
				}
				if(buf[j]=='.')
				{
					matrix[i][j]=-1;
				}
			}
		}

		double owp[100]={0};
		for(int i=0;i<num_teams;++i)
		{
			double s=0;
			int div=0;
			for(int j=0;j<num_teams;++j) if(matrix[j][i]!=-1)
			{
				s+=(wins[j]-matrix[j][i])/(double)(games[j]-1);
				++div;
			}
			owp[i]=s/div;
		}

		printf("Case #%d:\n",k+1);
		fprintf(fout,"Case #%d:\n",k+1);
		for(int i=0;i<num_teams;++i)
		{
			double rpi=0;
			int div=0;
			for(int j=0;j<num_teams;++j) if(i!=j && matrix[i][j]!=-1)
			{
				rpi+=owp[j]/4;
				++div;
			}
			rpi/=div;
			rpi+=wins[i]/(double)games[i]/4+owp[i]/2;
			printf("%.7lf\n",rpi);
			fprintf(fout,"%.7lf\n",rpi);
		}
	}
	fclose(flog);
	fclose(fout);
	fclose(fin);
}
