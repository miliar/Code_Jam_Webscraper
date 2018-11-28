#include <iostream.h>
#include <stdlib.h>
#include <stdio.h>

int runServers(char aWords[1010][100],int iPos, int maxWords, int maxServers, FILE *pfDebug){
    int countWords,countAuxServers=0;
    int result = 0;
    char aAuxServers[110][100];
    int tamAuxServers = 0;
    int bServerFound = 0;
    for (countWords = iPos; countWords<maxWords;countWords++){
        bServerFound = 0;
        fprintf(pfDebug, "Sigo con: %s (%d)",aWords[countWords],countWords);
        fprintf(pfDebug, "SERVERS VISTOS:\n");
        for (countAuxServers=0;countAuxServers<tamAuxServers;countAuxServers++){
            fprintf(pfDebug, "%s",aAuxServers[countAuxServers]);
        }
        for (countAuxServers=0;countAuxServers<tamAuxServers;countAuxServers++){
            //fprintf(pfDebug, "Comparo %s CON %s",aAuxServers[countAuxServers],aWords[countWords]);
           if (strcmp(aAuxServers[countAuxServers],aWords[countWords])==0){
            //fprintf(pfDebug, "IGUALES");
             bServerFound=1;
           }//else             //fprintf(pfDebug, "DISTINTOS");
        }
        if (bServerFound==0){
           aAuxServers[tamAuxServers] = aWords[countWords];
           tamAuxServers++;
        }
        if (tamAuxServers==maxServers && result==0){
           result = countWords;
        }

    }
    return result;
}

int main(){
    FILE *pfIn, *pfOut, *pfDebug;
    int iCases=0,iServers = 0, iWords =0, iChanges = 0;
    char aServers[110][100];
    char aWords[1010][100];

    int iCountCases,iCountServers,iCountWords;
    int iPos = 0;
    int numChanges = 0, noChange = -1;
    pfIn = fopen("C:\\Words\\A-large.in","r");
    pfOut = fopen("C:\\Words\\A-large.out","w");
    pfDebug = fopen("C:\\Words\\A-debug.out","w");
    if (pfIn!=NULL){

       fscanf(pfIn,"%d\n\r",&iCases);
       for(iCountCases=0;iCountCases<iCases;iCountCases++){
           numChanges = 0;
           noChange = -1;
           iPos = 0;
           fscanf(pfIn,"%d\n\r",&iServers);
           fprintf(pfDebug,"Case: %d\n",iCountCases+1);
           for(iCountServers=0;iCountServers<iServers;iCountServers++){
               fgets(aServers[iCountServers],100,pfIn);
               //fprintf(pfDebug,"Server: %s",aServers[iCountServers]);
           }

           fscanf(pfIn,"%d\n\r",&iWords);
           for(iCountWords=0;iCountWords<iWords;iCountWords++){
               fgets(aWords[iCountWords],100,pfIn);
               //fprintf(pfDebug,"Word: %s",aWords[iCountWords]);
           }
           fprintf(pfDebug,"Case #%d: %d,%d\n\r",iCountCases+1,iServers,iWords);
           while (iPos<iWords && noChange == -1){
                 fprintf(pfDebug,"Empiezo por: %s (%d)",aWords[iPos],iPos);
                 noChange = runServers(aWords,iPos,iWords,iServers,pfDebug);
                 fprintf(pfDebug,"Me he quedado en: %s (%d)",aWords[noChange],noChange);
                 //fprintf(pfDebug,"Word: %s",aWords[iCountWords]);
                 if (noChange!=0){
                    numChanges++;
                    iPos = noChange;
                    noChange = -1;
                 }else{

                 }

           }
           fprintf(pfOut,"Case #%d: %d\n",iCountCases+1,numChanges);

      }
      }
      fclose(pfIn);
      fclose(pfOut);
      fclose(pfDebug);
      return 0;
}
