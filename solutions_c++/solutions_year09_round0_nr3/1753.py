#include <stdio.h>
#include <conio.h>

#include <string.h>




long int count[19][500][2];
char word[502];
int length;

char *sentence = "welcome to code jam";

int minSentence[19];
int maxSentence[19];


void getOcurrences();
void getSum();
void resetCase();


int main(){
     FILE *fileIn, *fileOut;
	fileIn=fopen("C:\\GCJ\\Q\\C-small.in", "r");
	fileOut=fopen("C:\\GCJ\\Q\\C-small.out", "w");
	int wordLength;
	if (fileIn!=NULL) {
     
        
        fscanf(fileIn,"%d\n",&wordLength);
            printf("Palabras %d\n",wordLength);
        for (int iWord=0;iWord<wordLength;iWord++){

            fgets(word,51,fileIn);
            length = strlen(word)-1;
            resetCase();            
            //printf("Palabra %d: %d caracteres",iWord, length);
            getOcurrences();
            getSum();
            /**      
            printf("Ocurrencias\n");
            for (int j=0;j<19;j++){
              for (int i=0;i<length;i++){
                  printf("%d ",count[j][i][0]);
              }
              printf("\n");
            }
            //printf("Suma\n");
            //for (int j=0;j<19;j++){
              for (int i=0;i<length;i++){
                  printf("%d ",count[j][i][1]);
              }
              printf("\n");
            }*/
            fprintf(fileOut,"Case #%d: %04d\n",iWord+1,count[0][0][1]);
        }
        //scanf("N");
        
        
    }
    fclose(fileIn);
    fclose(fileOut);
    return 0;  
}

void getOcurrences(){
     for (int i=0;i<length;i++){
         for (int j=0;j<19;j++){
             if (word[i]==sentence[j]){
                count[j][i][0] = 1;                          
             }else count[j][i][0] = 0;
         }
     }
}

void getSum(){
     for (int j=18;j>=0;j--){
          for (int i=(length-1);i>=0;i--){
              
              if (i!=(length-1)){
                 count[j][i][1] = count[j][i+1][1];
              }
              if (j!=18){
                 count[j][i][1] = (count[j][i][0]*count[j+1][i][1]+count[j][i][1])%1000;
              }else{
                 count[j][i][1] = (count[j][i][0]+count[j][i][1])%1000;   
              }
          }
     }
}


void resetCase(){
    for (int i=0;i<length;i++){
         for (int j=0;j<19;j++){
             
             count[j][i][0] = 0;                          
             count[j][i][1] = 0;
         }
     }
}
