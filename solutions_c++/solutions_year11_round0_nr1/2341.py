#include <stdio.h>
#include<iostream>
#include<fstream>
using namespace std;

int botTrust(int bt[][2],int count);
int botTrust(char path[],int ot[],int bt[],int count);

int main()
{
	FILE *fPtr;
	FILE *fOut;
	int line;

	fstream flie;
	fOut=fopen("b.out","w");
	if((fPtr=fopen("b.in","r"))==NULL)
		printf("file can not be open");
	else
	{
		fscanf(fPtr,"%d",&line);
		printf("%d\n",line);
		int count;
		for(int i=0;i<line;i++)
		{
			fscanf(fPtr,"%d",&count);
			printf("%d ",count);
			char path[100];
			int ot[100];
			int bt[100];
			int oi=0,bi=0;
			int tmp;
			for(int j=0;j<count;j++)
			{
				fscanf(fPtr," %c %d",&path[j],&tmp);
				path[j]=='O'?ot[oi++]=tmp:bt[bi++]=tmp;
			}
			int omax=oi;
			int bmax=bi;
			int time =0,ol=1,bl=1;
			oi=bi=0;

//==========================¼ÆËã=========================
			for(int k=0;k<count;k++)
			{
				int step=0;
				if(path[k]=='O')
				{
					step=abs(ot[oi]-ol)+1;
					ol=ot[oi++];
					if(bi<bmax)
					{
						if(abs(bt[bi]-bl)>step)
							bl=(bt[bi]>bl)?bl+step:bl-step;
						else bl=bt[bi];
					}
				}
				else
				{
					step=abs(bt[bi]-bl)+1;
					bl=bt[bi++];
					if(oi<omax)
					{
						if(abs(ot[oi]-ol)>step)
							ol=(ot[oi]>ol)?ol+step:ol-step;
						else ol=ot[oi];
					}
				}
				time+=step;
			}

//========================================================

			//int y = botTrust(path,ot,bt,count);
			fprintf(fOut,"Case #%d: %d\n",i+1,time);
			printf("Case #%d: %d",i+1,time);
			printf("\n");
		}
	}
	printf("done");
	getchar();
	fclose(fPtr);
	return 0;
}
int botTrust(char path[],int ot[],int bt[],int count)
{
	int ol=1,bl=1,time=0;
	for(int i=0;i<count;i++)
	{
		printf("%d ",ot[i]);
		/*if(path[i]=='O')
		{

		}
		else
		{

		}*/
	}
	return time;

}
int botTrust(int bt[][2],int count)
{
	int ol,bl;
	ol=bl=1;
	for(int i=0;i<count;i++)
	{
		if(bt[i][0]==0)
		{

		}
		else
		{
		}
	}


	return 4;
}