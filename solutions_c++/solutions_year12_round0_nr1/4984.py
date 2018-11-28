#include "stdlib.h"
#include "stdio.h"
#include "string.h"
#include "math.h"
#include "time.h"
#include "iostream.h"
#include "fstream.h"




//-- Main -----------------------------------------------------------------------
int main(int argc, char *argv[]) 
{
	FILE *f_out,*f_in;
	ifstream fp_in;
	int T,index;
	char inputChar[120],outputChar[100];
	char first[135]=   "zy qee ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	char firstOut[135]="qa zoo our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	
	
	
	f_out =fopen ("output.txt","w");
	f_in  =fopen ("input.txt","r");

	
	
		fscanf(f_in,"%d", &T);
		printf("T:%d \n",T);
		fgets(inputChar, 100, f_in);
		
		for(int i=0;i<T;i++)
		{
			
			fgets(inputChar, 120, f_in);
			
			cout << inputChar;
			
			int j=0;
			while(j<100)
			{
				
				if(inputChar[j]!='\n')
				{
					for(int k=0;k<135;k++)
					{
						if(inputChar[j]==first[k]){
							outputChar[j]= firstOut[k];
							
						}
			
					}
				}else {
					if (inputChar[j]>='a' && inputChar[j]>='z') {
						outputChar[j]=inputChar[j];
					}else {
						outputChar[j]= NULL;
					}
				}

					j++;
			
			}
			
		
			fprintf(f_out,"Case #%d: %s\n",i+1,outputChar);
			
	
		}//T: Test Cases
		
		
		
		
	
	fclose(f_out);
	fclose(f_in); 
};
