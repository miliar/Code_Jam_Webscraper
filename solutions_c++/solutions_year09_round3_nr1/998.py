#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <memory.h>
#include <string.h>
#include <math.h>
/*********** GLOBAL VARIABLES ********************************************************/
char word[62];
double  wordAux[62];
char distinct[62];
int distinctValue[62];
/*********** GLOBAL VARIABLES ********************************************************/

/*********** METHODS *****************************************************************/
void resetCase(){
}
/*********** METHODS *****************************************************************/

int checkDistinctChar(char a, int tam){
     int res = -1;
     for (int i=0;i<tam;i++){
         if (distinct[i] == a){
               res = i;
         }
     }
     return res;
}

int main(){
    char *file = "A-small-attempt1";    
    FILE *fileIn, *fileOut;
    char inFile[32], outFile[32];
    strcpy(inFile, file); strcpy(outFile, file);
	strcat(inFile, ".in"); strcat(outFile, ".out");
	fileIn=fopen(inFile, "r");
	fileOut=fopen(outFile, "w");
	
    /*********** BODY ********************************************************/
    int numCases=0;
    fscanf(fileIn,"%d\n",&numCases);
    float decimal = 0;
        
    for (int iCase=0;iCase<numCases;iCase++){
            double decimal = 0;
            int minBase = 0;
            memset(distinct,-1,62);
            memset(wordAux,0,62);
            memset(word,0,62);
            fscanf(fileIn,"%s\n",word); 
            

            for (int i=0;i<strlen(word);i++){                
                int distinctchar = checkDistinctChar(word[i],minBase);
                if (distinctchar==-1){

                   distinct[minBase] = word[i];

                   minBase++;
                   if (minBase==1)
                      wordAux[i] = 1;
                   else if (minBase==2)   
                        wordAux[i] = 0;
                   else wordAux[i] = minBase-1;
                    distinctValue[minBase-1] = wordAux[i]; 

                }else{

                   //wordAux[i] = distinctchar;
                   wordAux[i] = distinctValue[distinctchar];
                   //fprintf(fileOut,"wordAux[%d] = %d\n",i,wordAux[i]);                                                          


                }

            } 
            if (minBase==1){
                            minBase++;
            }
            for (int i=strlen(word)-1;i>=0;i--){

                decimal += wordAux[i]*pow(minBase,strlen(word)-1-i);
            } 
            
        
        
            fprintf(fileOut,"Case #%d: %.0f\n",iCase+1,decimal); 
    }


    /*********** BODY ********************************************************/
    fclose(fileIn);
    fclose(fileOut);
    return 0;  
}


/*********************************************************
TYPICAL RUN

TYPICAL RUN
int numCases=0;
fscanf(fileIn,"%d\n",&numCases);

        
for (int iCase=0;iCase<numCases;iCase++){
    fprintf(fileOut,"Case #%d:\n",iCase+1); 
}


fgets(linea,100,fileIn);
ptr = strtok (linea," ");
while (ptr != NULL)
{      
       bases[numBases] = atoi(ptr);
       ptr = strtok (NULL, " ");
       numBases++;
}
  

**********************************************************/
