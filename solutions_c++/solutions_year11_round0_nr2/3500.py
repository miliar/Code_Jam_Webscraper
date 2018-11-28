#include <cstdio>
#include <cstdlib>
const int MAX_N = 128;
int combine[MAX_N][MAX_N];
int oppose[MAX_N][MAX_N];
char cur_list[500];
char input_list[500];
int main()
{
	FILE* ifid = fopen("in.txt","r");
	FILE* ofid = fopen("out.txt","w");
	int T;
	int cT;
	int oT;
	char str[10];
	fscanf(ifid,"%d",&T);
	for(int cc=1; cc<=T; ++cc)
	{
		for(int i=0; i<MAX_N; ++i)
		{
			for(int j=0; j<MAX_N; ++j)
			{
				combine[i][j] = -1;
				oppose[i][j] = 0;
			}
		}
		fscanf(ifid,"%d",&cT);
		for(int i=0; i<cT; ++i)
		{
			fscanf(ifid,"%s",str);
			combine[str[0]][str[1]] = str[2];
			combine[str[1]][str[0]] = str[2];
		}
		fscanf(ifid,"%d",&oT);
		for(int i=0; i<oT; ++i)
		{
			fscanf(ifid,"%s",str);
			oppose[str[0]][str[1]] = 1;
			oppose[str[1]][str[0]] = 1;
		}
		int input_len = 0;
		fscanf(ifid,"%d%s",&input_len,input_list);
		int len = 0;
		for(int i=0; i<input_len; ++i)
		{
			cur_list[len++] = input_list[i];
			if(len>=2)
			{
				int cb  = combine[cur_list[len-1]][cur_list[len-2]];
				if(cb>=0)
				{
					cur_list[len-2] = cb;
					len--;
				}
				else
				{
					for(int j=0; j<len-1; ++j)
					{
						int op = oppose[cur_list[j]][cur_list[len-1]];
						if(op == 1)
						{
							len = 0;
						}
					}
				}
			}
		}
		fprintf(ofid,"Case #%d: [",cc);
		for(int i=0; i<len; ++i)
		{
			fprintf(ofid,"%c",cur_list[i]);
			if(i< len-1)
			{
				fprintf(ofid,", ");
			}
		}
		fprintf(ofid,"]\n");
	}
	fclose(ofid);
	fclose(ifid);
	return 0;
}