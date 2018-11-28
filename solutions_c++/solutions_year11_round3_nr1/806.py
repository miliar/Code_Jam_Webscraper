#include <cstdio>
#include <climits>
#include <cstring>

#include <memory.h>

#define INPUT_FILE "A-large.in"

using namespace std;

char (*g_map)[50];
char (*g_tile)[51];
int g_r,g_c,g_tile_cnt;

bool pre_check()
{
	/*for(int i=0;i<g_r;++i) for(int j=0;j<g_c;++j)
	{
	}*/
	return true;
}

bool try_fill(int cr,int cc)
{
	while(1)
	{
		if(g_tile_cnt==0) return true;

		while(g_map[cr][cc]!=1)
		{
			++cc;
			if(cc==g_c-1)
			{
				++cr;
				if(cr==g_r-1) return false;
				cc=0;
			}
		}
		// assured that g_map[cr][cc]=1, cr<r-1, cc<c-1

		if(g_map[cr][cc+1]==1 && g_map[cr+1][cc]==1 && g_map[cr+1][cc+1]==1)
		{
			g_map[cr][cc]=2;
			g_map[cr+1][cc]=2;
			g_map[cr][cc+1]=2;
			g_map[cr+1][cc+1]=2;

			g_tile[cr][cc]='/';
			g_tile[cr+1][cc]='\\';
			g_tile[cr][cc+1]='\\';
			g_tile[cr+1][cc+1]='/';

			g_tile_cnt-=4;
		} else {
			return false;
		}
	}
	return true;
}

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
		char map[50][50],tile[50][51]={0};
		int r,c,tile_cnt=0;
		fscanf(fin,"%d %d",&r,&c);
		for(int i=0;i<r;++i)
		{
			char buf[60];
			fscanf(fin,"%s",buf);
			for(int j=0;j<c;++j)
			{
				if(buf[j]=='#')
				{
					map[i][j]=1;
					++tile_cnt;
				}
				else map[i][j]=0;
				tile[i][j]='.';
			}
			tile[i][c]=0;
		}
		g_map=map;
		g_tile=tile;
		g_r=r;
		g_c=c;
		g_tile_cnt=tile_cnt;
		if(tile_cnt%4==0 && pre_check() && try_fill(0,0))
		{
			printf("Case #%d:\n",k+1);
			fprintf(fout,"Case #%d:\n",k+1);
			for(int i=0;i<g_r;++i)
			{
				printf("%s\n",tile[i]);
				fprintf(fout,"%s\n",tile[i]);
			}
		} else {
			printf("Case #%d:\nImpossible\n",k+1);
			fprintf(fout,"Case #%d:\nImpossible\n",k+1);
		}
	}
	fclose(flog);
	fclose(fout);
	fclose(fin);
}
