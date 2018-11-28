#include <stdio.h>
#include <math.h>

void main()
{
	FILE * input = fopen("input.in","r");
	FILE * output = fopen("output.out","w");
	int n;
	fscanf(input,"%d",&n);
	for(int i=0;i<n;i++)
	{
		int k;
		int posBlue=1;
		int posOrange=1;
		int currentTarget=0;
		fscanf(input,"%d",&k);
		bool * rob = new bool[k];
		int * pos = new int[k];
		for(int j=0;j<k;j++)
		{	
			char bot;
			fscanf(input, "%c", &bot);
			fscanf(input, "%c", &bot);
			if(bot=='O')
				rob[j]=true;
			else
				rob[j]=false;
			fscanf(input,"%d",&pos[j]);
		}
		int time = 0;
		for(int j=0;j<k;j++)
		{
			//get target for blue robot
			int m=j;
			while(rob[m] && m<k) m++;
			//get target for orange robot
			int p=j;
			int dtime;
			while(!rob[p] && p<k) p++;
			if(m<p)
			{
				dtime=abs(pos[m]-posBlue)+1;
				posBlue = pos[m];
				time+=dtime;
				//move orange robot
				int delta = pos[p]-posOrange;
				//time is anough to move orange robot to target
				if(abs(delta)<dtime)
					posOrange = pos[p];
				else
				{
					if(delta>0)
						posOrange+=dtime;
					else
						posOrange-=dtime;
				}
			}
			else
			{
				//similiar actions for blue robot
				dtime = abs(pos[p]-posOrange)+1;
				posOrange = pos[p];
				time += dtime;
				//move blue robot
				int delta = pos[m]-posBlue;
				//time is anough to move orange robot to target
				if(abs(delta)<dtime)
					posBlue = pos[m];
				else
				{
					if(delta>0)
						posBlue+=dtime;
					else
						posBlue-=dtime;
				}
			}
		}
		delete[] rob;
		delete[] pos;
		fprintf(output,"Case #%d: %d\n",i+1,time);
	}
	fclose(input);
	fclose(output);
}