#include <iostream.h>
#include <stdlib.h>
#include <stdio.h>

int checkTrain(int,int,int,int[110][3],FILE *);

int main()
{
      FILE *pfIn, *pfOut, *pfDebug;
      int totalATrains = 0, totalBTrains =0;
      int auxTrain[2];
      int iCases, iATrain, iBTrain, iTurnaround;
      int iCountCases,iCountTrains, iCountTrains2;
      int aTrainA[110][3], aTrainB[110][3];
      int aTimeAHour, aTimeAMinute, aTimeBHour, aTimeBMinute;
      pfIn = fopen("C:\\Trains\\B-large.in","r");
      pfOut = fopen("C:\\Trains\\B-large.out","w");
      pfDebug = fopen("C:\\Trains\\B-debug.out","w");
      if (pfIn!=NULL){
           fscanf(pfIn,"%d\n\r",&iCases);
           for(iCountCases=0;iCountCases<iCases;iCountCases++){
              fscanf(pfIn,"%d\n\r",&iTurnaround);
              fscanf(pfIn,"%d %d\n\r",&iATrain,&iBTrain);
              fprintf(pfDebug,"Case #%d: Numero de trenes A: %d, Numero de trenes B: %d\n\r",iCountCases,iATrain,iBTrain);
              for(iCountTrains=0;iCountTrains<iATrain;iCountTrains++){
                 fscanf(pfIn,"%d:%d %d:%d\n\r",&aTimeAHour,&aTimeAMinute,&aTimeBHour,&aTimeBMinute);

                 aTrainA[iCountTrains][0] = aTimeAHour*60+aTimeAMinute;
                 aTrainA[iCountTrains][1] = aTimeBHour*60+aTimeBMinute;
                 aTrainA[iCountTrains][2] = 0;
                 fprintf(pfDebug,"Tren A: %d (%d,%d)\n\r",iCountTrains+1,aTrainA[iCountTrains][0],aTrainA[iCountTrains][1]);

              }
              for(iCountTrains=0;iCountTrains<iBTrain;iCountTrains++){
                 fscanf(pfIn,"%d:%d %d:%d\n\r",&aTimeAHour,&aTimeAMinute,&aTimeBHour,&aTimeBMinute);
                 aTrainB[iCountTrains][0] = aTimeAHour*60+aTimeAMinute;
                 aTrainB[iCountTrains][1] = aTimeBHour*60+aTimeBMinute;
                 aTrainB[iCountTrains][2] = 0;
                 fprintf(pfDebug,"Tren B: %d (%d,%d)\n\r",iCountTrains+1,aTrainB[iCountTrains][0],aTrainB[iCountTrains][1]);

              }

              for(iCountTrains=0;iCountTrains<(iATrain-1);iCountTrains++){
                for(iCountTrains2=iCountTrains+1;iCountTrains2<iATrain;iCountTrains2++){
                    if (aTrainA[iCountTrains][1]<aTrainA[iCountTrains2][1]){
                       auxTrain[0] = aTrainA[iCountTrains][0];
                       auxTrain[1] = aTrainA[iCountTrains][1];
                       aTrainA[iCountTrains][0] = aTrainA[iCountTrains2][0];
                       aTrainA[iCountTrains][1] = aTrainA[iCountTrains2][1];
                       aTrainA[iCountTrains2][0] = auxTrain[0];
                       aTrainA[iCountTrains2][1] = auxTrain[1];
                    }
                }
              }

              for(iCountTrains=0;iCountTrains<(iBTrain-1);iCountTrains++){
                for(iCountTrains2=iCountTrains+1;iCountTrains2<iBTrain;iCountTrains2++){
                    if (aTrainB[iCountTrains][1]<aTrainB[iCountTrains2][1]){
                       auxTrain[0] = aTrainB[iCountTrains][0];
                       auxTrain[1] = aTrainB[iCountTrains][1];
                       aTrainB[iCountTrains][0] = aTrainB[iCountTrains2][0];
                       aTrainB[iCountTrains][1] = aTrainB[iCountTrains2][1];
                       aTrainB[iCountTrains2][0] = auxTrain[0];
                       aTrainB[iCountTrains2][1] = auxTrain[1];
                    }
                }
              }


              totalATrains = 0;
              totalBTrains = 0;
              for (iCountTrains=0;iCountTrains<iATrain;iCountTrains++){
                fprintf(pfDebug,"A: Tren: %d\n\r",aTrainA[iCountTrains][0]);
                if (checkTrain(aTrainA[iCountTrains][0],iBTrain,iTurnaround,aTrainB,pfDebug)==0){
                   totalATrains++;
                   fprintf(pfDebug,"\n\r");
                } else fprintf(pfDebug,"COMBINACION\n\r");
              }

              for (iCountTrains=0;iCountTrains<iBTrain;iCountTrains++){
                fprintf(pfDebug,"B: Tren: %d\n\r",aTrainB[iCountTrains][0]);
                if (checkTrain(aTrainB[iCountTrains][0],iATrain,iTurnaround,aTrainA,pfDebug)==0){
                   totalBTrains++;
                                      fprintf(pfDebug,"\n\r");
                }  else fprintf(pfDebug,"COMBINACION\n\r");
              }


              fprintf(pfOut,"Case #%d: %d %d\n",iCountCases+1,totalATrains, totalBTrains);
            }

      }
      fclose(pfIn);
      fclose(pfOut);
      fclose(pfDebug);


      return 0;
}

int checkTrain(int timeIn, int numberTrainB, int timearound,int trainB[110][3], FILE *pfDebug){
    int countTrain=0;
    int result = 0;
    for (countTrain =0;countTrain<numberTrainB;countTrain++){
        fprintf(pfDebug,"Comparo con %d (TimeIn: %d, TimeArrive: %d\n\r",countTrain,timeIn, trainB[countTrain][1]+timearound);
        if (((trainB[countTrain][1]+timearound)<=timeIn) && trainB[countTrain][2]==0 && ((trainB[countTrain][1]+timearound)<24*60) && result==0){
           result = 1;
           trainB[countTrain][2] = 1;
           }
    }
    return result;
}



