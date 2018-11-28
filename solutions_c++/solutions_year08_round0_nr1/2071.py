//---------------------------------------------------------------------------
#pragma hdrstop
//---------------------------------------------------------------------------
#pragma argsused
#include <stdio.h>
#include <conio.h>
#include <string.h>
#include <fstream.h>
#define TASK "A"
#define SIZE "large"
//---------------------------------------------------------------------------
int main(int argc, char* argv[])
{
	/* get i/o file names, open files */
	FILE *in,*out;

	char* str = new char[256];
	str = TASK;
	strcat(str,"-");
	strcat(str,SIZE);
	strcat(str,".in");

	char* str2 = new char[256];
	str2 = TASK;
	strcat(str2,"-");
	strcat(str2,SIZE);
	strcat(str2,".out");

	in = fopen(str,"r");
	out = fopen(str2,"w");

	/* code */

	int N; // number of cases
	int S; // number of systems
	int Q; // number of queries


	fscanf(in,"%d",&N);
	char* buf = new char[100];
	for(int i=0; i<N; i++)
	{
		/* reading each case */
		fscanf(in,"%d",&S);
		char **Sys = new char*[S];
		fgets(buf,100,in);
		for(int j=0; j<S; j++)
		{
			Sys[j] = new char[100];
			fgets(Sys[j],100,in);
		}
		fscanf(in,"%d",&Q);
		char **Que = new char*[Q];
		fgets(buf,100,in);
		for(int j=0; j<Q; j++)
		{
			Que[j] = new char[100];
			fgets(Que[j],100,in);
		}
		/* array of switches */
		int* Res = new int[S];

		/* for each system */
		for(int j=0; j<S; j++)
		{
			int switches = 0;
			//  try to request
			int p=j;
			for(int k=0; k<Q; k++)
			{
				if(!strcmp(Sys[p],Que[k])) // if system == request
				{
						switches++;

						/* calculate next optimal system */
						int* opt = new int[S];
						for(int x=0; x<S; x++)
						{
                            opt[x] = 1000;
                        }
						for(int x = 0; x<S; x++)
						{
							for(int y = k; y<Q; y++)
							{
								if(!strcmp(Sys[x],Que[y]))
								{
									if(strcmp(Sys[x],Sys[p]))
									{
										opt[x]=y;
										break;
									}
									else
									{
										opt[x] = 0;
										break;
									}
								}
							}
						}
						int m = opt[0];
						int I = 0;
						for(int x=0; x<S; x++)
						{
							if(opt[x]>m)
							{
								m = opt[x];
								I = x;
                            }
						}
						p = I;
						k--;
                }
			}
			Res[j]=switches;
		}
		int min = Res[0];
		for(int z=0; z<S; z++)
		{
			if(Res[z]<min)
			{
				min = Res[z];
			}
		}

		fprintf(out,"Case #%d: %d\n",i+1,min);
	}

	fclose(in);
	fclose(out);
	return 0;
}
//---------------------------------------------------------------------------

