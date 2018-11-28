#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE *fp,*fp1;
    fp = fopen("B-large.in","r");
    fp1 = fopen("output.txt","w");
     if(fp == NULL || fp1 == NULL){
     exit(0);
    }
     int T;

    fscanf(fp,"%d",&T);
    int count = T-1;
    int tCount = T;
	
	int nDancer ;
	int p = 0 ;
	int *scores ;
	int S = 0 ;
	int output = 0 ;
	 while( tCount > 0 ){
		output = 0 ;  //Reset output
		fscanf(fp,"%d",&nDancer);
		fscanf(fp,"%d",&S);
		fscanf(fp,"%d",&p);
		scores = (int*)malloc(sizeof(int)*nDancer);
		for( int j = 0 ; j < nDancer ; j++ ){
		  fscanf(fp,"%d",&scores[j]);
			if( scores[j] >= 3*p ){
				output++ ;
            }
			else{
                if( scores[j] < p ){
					continue;
                }
				int diffence = scores[j] - p ;
				if( diffence/2 == p+1 || diffence/2 == p-1 ){
					output++ ;
                }
				else if( S > 0 && ((diffence/2 == p+2) || (diffence/2 == p-2))){
					output++ ;
					S-- ;
				}
			}
			
		}
	    fprintf(fp1,"Case #%d: %d\n",(T-count),output);
        count--;
        tCount--;
		free(scores);
	}	
	fclose(fp);
	fclose(fp1);
	return 1;
}
