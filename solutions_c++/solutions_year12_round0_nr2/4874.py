#include "stdlib.h"
#include "stdio.h"
#include "string.h"
#include "math.h"
#include "time.h"





//-- Main -----------------------------------------------------------------------
int main(int argc, char *argv[]) 
{
	FILE *f_in,*f_out;
	int T, N,S,P,*score,surp,num;
	score=new int[P];

	
	
	f_out =fopen ("output.txt","w");
	f_in = fopen ("input.txt","r");
	
	
		fscanf(f_in,"%d", &T);
		printf("T:%d \n",T);
		

				
		// R
		for(int i=0;i<T;i++)
		{
			fscanf(f_in,"%d %d %d",&N,&S,&P);
			num=0;
			surp=0;
			for (int j=0; j<N; j++) {
				fscanf(f_in,"%d",&score[j]);
				//printf("Score: %d\n",score[j]);

			
				if(P==0)
				{
					num++;
				}else if(P==1)
				{
					if(score[j]>=1)
						num++;
				}
				else if(score[j]-(3*P)>-3)
				{
					num++;
				}else if((score[j]-3*P==-4) || (score[j]-3*P==-3))
				{
					surp++;
				}
				
				
			
			
			}

			if(surp>S)
			{
				num=num+S;
			}
			else {
				num=num+surp;
			}

			
			fprintf(f_out,"Case #%d: %d\n",i+1,num);
			// Printing Output
			
	
		}//T: Test Cases
		
		
		
		
	
	fclose(f_out);
	fclose(f_in);
};
