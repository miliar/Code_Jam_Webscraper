#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
FILE *fout;
FILE *fin;
int compare (const void * a, const void * b){
  return ( *(int*)b - *(int*)a );
}
int main(){
    char string[500];
    int scores[500];
    int totLines;
    fin=fopen("dancingGooglersLarge.in","r");
    fout=fopen("dancingGooglersLarge.out","w");
    int nums[2][31];
    nums[0][0]=0;
    for(int i=1;i<=30;i++){
        nums[0][i]=(int)((i+2)/3);
    }
    nums[1][0]=-1;
    for(int i=1;i<=30;i++){
        if((i%3)==1){nums[1][i]=-1;}
        else{
            nums[1][i]=(int)((i+4)/3);
        }
    }
    fgets(string,500,fin);
    totLines=atoi(string);
    for(int i=0;i<totLines;i++){
        fprintf(fout,"Case #%d: ",i+1);
        int numGooglers, numSurprises, targetVal;
        int totCount=0;
        fgets(string,500,fin);
        char * pch;
        pch = strtok (string," ");
        numGooglers=atoi(pch);
        pch = strtok (NULL," ");
        numSurprises=atoi(pch);
        pch = strtok (NULL," ");
        targetVal=atoi(pch);
        for(int i=0;i<numGooglers;i++){
            pch = strtok (NULL," ");
            scores[i]=atoi(pch);
        }   
        qsort(scores,numGooglers,sizeof(int),compare);
        for(int i=0;i<numGooglers;i++){
            if(nums[0][scores[i]]>=targetVal){
                totCount++;
            }
            else if(nums[1][scores[i]]>=targetVal&&numSurprises>0){
                numSurprises--;
                totCount++;
            }
        }
        fprintf(fout,"%d\n",totCount);
    }
}
    
