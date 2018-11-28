#include <cstdio>
#include <cstring>
#include <cmath>
#include <set>
#include <string>

#define INPUT_FILE "A-large.in"

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
		int moves;
		fscanf(fin,"%d",&moves);

		int pos_o=1,pos_b=1;
		int at_o=0,at_b=0,time=0;
		for(int i=0;i<moves;++i)
		{
			char who[20];
			int button_pos,req_time;
			fscanf(fin,"%s %d",who,&button_pos);

			int* rob_pos;
			int* rob_at;
			if(who[0]=='O')
			{
				rob_pos=&pos_o;
				rob_at=&at_o;
			} else {
				rob_pos=&pos_b;
				rob_at=&at_b;
			}

			req_time=abs(*rob_pos-button_pos);
			printf("robot %c pos=%d at=%d\n",who[0],*rob_pos,*rob_at);
			if((*rob_at)+req_time>time)
			{
				time=(*rob_at)+req_time+1;
				(*rob_at)=time;
				*rob_pos=button_pos;
				printf("time=%d : robot %c move to pos %d\n",time-1,who[0],button_pos);
				printf("time=%d : robot %c prees button %d\n",time,who[0],button_pos);
			} else {
				time++;
				(*rob_at)=time;
				*rob_pos=button_pos;
				printf("time=%d : robot %c move to pos %d\n",(*rob_at)+req_time,who[0],button_pos);
				printf("time=%d : robot %c prees button %d\n",time,who[0],button_pos);
			}
		}
		printf("Case #%d: %d\n",k+1,time);
		fprintf(fout,"Case #%d: %d\n",k+1,time);
	}

	return 0;
}