#include "stdlib.h"
#include "stdio.h"
#include "string.h"
#include "math.h"
#include "time.h"


//-- Main -----------------------------------------------------------------------
int main(int argc, char *argv[]) 
{
	FILE *f_in,*f_out;
	int T,C,D,N;
	char cStr[100][36][4],dStr[100][28][3],nStr[100][100];
	char outStr[100];
	int combine=0;
	
	f_out = fopen ("output.txt","w");
	f_in = fopen("input.txt","r");
	
	
	fscanf(f_in,"%d",&T);
	
	for(int i=0;i<T;i++)
	{
			
		fscanf(f_in,"%d",&C);
		
		for(int c=0;c<C;c++)
		{
			fscanf(f_in,"%s",cStr[i][c]);
		}
		fscanf(f_in,"%d",&D);
		for(int d=0;d<D;d++)
		{
			fscanf(f_in,"%s",dStr[i][d]);
		}
		fscanf(f_in,"%d",&N);
		fscanf(f_in,"%s",nStr[i]);
		
		
		int l=0; //Shows the last set char in output
		outStr[0]=nStr[i][0];
		for(int n=1;n<N;n++)
		{
			if(C==0)
			{
				l++;
				outStr[l]=nStr[i][n];
			}
			for(int c=0;c<C;c++)
			{
				if(nStr[i][n]==cStr[i][c][0])
				{
					if(outStr[l]==cStr[i][c][1])
					{
						outStr[l]=cStr[i][c][2];
						combine=1;
					}else
					{
						l++;
						outStr[l]=nStr[i][n];
					}
				}else if(nStr[i][n]==cStr[i][c][1])
				{
					if(outStr[l]==cStr[i][c][0])
					{
						outStr[l]=cStr[i][c][2];
						combine=1;
					}else
					{
						l++;
						outStr[l]=nStr[i][n];
					}
				}else
				{
					l++;
					outStr[l]=nStr[i][n];
				}
			}
			
			printf("OutStr: ");
			if(l>=0)
				printf("%c",outStr[0]);
			for(int nn=1;nn<=l;nn++)
			{
				printf(", %c",outStr[nn]);
			}
			printf("]\n");
			
			int detect=0;
			if(!combine){
			for(int d=0;d<D;d++)
			{
				if(nStr[i][n]==dStr[i][d][0])
				{
					for(int nn=0;nn<=l;nn++)
					{
						if(outStr[nn]==dStr[i][d][1])
						{
							detect=1;
							//outStr[0]=0;
						}
					}
				}
				if(nStr[i][n]==dStr[i][d][1])
				{
					for(int nn=0;nn<=l;nn++)
					{
						if(outStr[nn]==dStr[i][d][0])
						{
							detect=1;
							//outStr[0]=0;
						}
					}
					
				}
				if(detect==1)
				{
					l=-1;
					detect=0;
				}
			}
			}
			combine=0;
			
			/*printf("OutStr: ");
			if(l>=0)
				printf("%c",outStr[0]);
			for(int nn=1;nn<=l;nn++)
			{
				printf(", %c",outStr[nn]);
			}
			printf("]");*/
		}
		//printf("\n\n");
		
		fprintf(f_out,"Case #%d: [", i+1);
		if(l>=0)
			fprintf(f_out,"%c",outStr[0]);
		for(int nn=1;nn<=l;nn++)
		{
			fprintf(f_out,", %c",outStr[nn]);
		}
		fprintf(f_out,"]\n");
		l=0;
	}
	
	fclose(f_out);
	fclose(f_in);
};
