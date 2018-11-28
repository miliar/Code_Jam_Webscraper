#include <cstdio>
#include <cstdlib>
char rtype[10];
int main(int argc, char **argv)
{
    FILE* fid = fopen("in.txt","r");
	FILE* ofid = fopen("out.txt","w");
	int casenum  = 0;
	int stepnum = 0;
	fscanf(fid,"%d",&casenum);
	for(int i=1; i<=casenum; ++i)
	{
		int opos = 1;
		int otime = 0;
		int bpos = 1;
		int btime = 0;
		int time = 0;
		int pos = 0;
		fscanf(fid,"%d",&stepnum);
		for(int j=1; j<=stepnum; ++j)
		{
			fscanf(fid,"%s%d",rtype,&pos);
			if(rtype[0] == 'O')
			{
				if(otime >= abs(pos-opos))
				{
					time += 1;
					btime += 1;
					otime = 0;
				}
				else
				{
					time += abs(pos-opos) - otime + 1;
					btime += abs(pos-opos) - otime + 1;
					otime = 0;
				}
				opos = pos;
			}
			else
			{
				if(btime >= abs(pos-bpos))
				{
					time += 1;
					otime += 1;
					btime = 0;
				}
				else
				{
					time += abs(pos-bpos) - btime + 1;
					otime += abs(pos-bpos) - btime + 1;
					btime = 0;
				}
				bpos = pos;
			}
		}
		fprintf(ofid,"Case #%d: %d\n",i,time);
	}
	fclose(fid);
	fclose(ofid);
	return 0;
}
