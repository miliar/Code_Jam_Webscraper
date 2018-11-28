#include <stdio.h>
#include <iostream.h>
#include <string>
#include <stdlib.h>
using std::string;

 int intcmp(const void *v1, const void *v2)
 {
     return (*(int *)v1 - *(int *)v2);
 }
main(int argc, char **argv){
   char fName[100],wName[100];
   char line[100],*pch;
   
   //---open files
   strcpy(fName,argv[1]);
   //strcpy(wName,argv[2]);
   FILE *fid,*wid;
   fid=fopen(fName,"r");
   //wid=fopen(wName,"w");

   //---Read no. of cases---
   int noCases;
   fgets(line,100,fid);   
   noCases=atoi(line); 
   //cout<<noCases<<endl;
   int i=0;
   while(i<noCases){
       //---for case i--------
       //---Read Turnaround time -----
       bzero(line,100); 
       fgets(line,100,fid);
       int tat;   
       tat=atoi(line); 
       //cout<<tat<<endl;
       //----Read A and B
       bzero(line,100); 
       fgets(line,100,fid);
       pch = strtok(line," ");
       int noT[2],j=0;        
       while(pch!=NULL){
           noT[j]=atoi(pch);
           pch = strtok(NULL," ");
           j++;
           if(pch==NULL)break;
       }
       //cout<<noT[0]<<" "<<noT[1]<<endl;
       //----Read A time table----       
       int aTb_a[noT[0]],aTb_b[noT[0]];
       char tempA[10],tempB[10];
       char *pch1;
       int temp;
       j=0;
       while(j<noT[0]){
           bzero(line,100); 
           fgets(line,100,fid);
           pch = strtok(line," ");
           strcpy(tempA,pch);
           while(pch!=NULL){
               pch = strtok(NULL," ");           
               if(pch==NULL)break;
               strcpy(tempB,pch);
           }
           pch1 = strtok(tempA,":");
           aTb_a[j]=atoi(pch1)*60;
           while(pch1!=NULL){
               pch1 = strtok(NULL,":");          
               if(pch1==NULL)break;
               aTb_a[j]+=atoi(pch1);
           }
           //cout<<aTb_a[j]<<endl;
           pch1 = strtok(tempB,":");
           aTb_b[j]=atoi(pch1)*60;
           while(pch1!=NULL){
               pch1 = strtok(NULL,":");          
               if(pch1==NULL)break;
               aTb_b[j]+=atoi(pch1);
           }
           //cout<<aTb_b[j]<<endl;
           j++;
       }
       //----Read B time table----       
       int bTa_a[noT[1]],bTa_b[noT[1]];
       j=0;
       while(j<noT[1]){
           bzero(line,100); 
           fgets(line,100,fid);
           pch = strtok(line," ");
           strcpy(tempA,pch);
           while(pch!=NULL){
               pch = strtok(NULL," ");           
               if(pch==NULL)break;
               strcpy(tempB,pch);
           }
           pch1 = strtok(tempA,":");
           bTa_b[j]=atoi(pch1)*60;
           while(pch1!=NULL){
               pch1 = strtok(NULL,":");          
               if(pch1==NULL)break;
               bTa_b[j]+=atoi(pch1);
           }
           //cout<<bTa_a[j]<<endl;
           pch1 = strtok(tempB,":");
           bTa_a[j]=atoi(pch1)*60;
           while(pch1!=NULL){
               pch1 = strtok(NULL,":");          
               if(pch1==NULL)break;
               bTa_a[j]+=atoi(pch1);
           }
           //cout<<bTa_b[j]<<endl;
           j++;
       }//---------A and B Train Time Table complete
       int flagA[noT[0]],flagB[noT[1]],k;
       j=0;
       while(j<noT[0]){
           flagA[j]=0;
           j++; 
       } 
       j=0;
       while(j<noT[1]){
           flagB[j]=0;
           j++;
       }
       j=0;
       qsort(bTa_b, noT[1], sizeof(bTa_b[0]), intcmp);
       qsort(aTb_b, noT[0], sizeof(aTb_b[0]), intcmp);
       while(j<noT[0]){
           k=0;
           while(k<noT[1]){
              if(bTa_b[k]>=aTb_b[j]+tat){
                  if(flagB[k]==0){
                      flagB[k]=1;
                      break;
                  }
              }
              k++;
           }       
           j++;
       }
       qsort(bTa_a, noT[1], sizeof(bTa_a[0]), intcmp);
       qsort(aTb_a, noT[0], sizeof(aTb_a[0]), intcmp);
       j=0;
       while(j<noT[1]){
           k=0;
           while(k<noT[0]){
              if(aTb_a[k]>=bTa_a[j]+tat){
                  if(flagA[k]==0){
                      flagA[k]=1;
                      break;
                  }
              }
              k++;
           }       
           j++;
       }
       j=0;
       int noTA=0,noTB=0;
       while(j<noT[0]){
           if(flagA[j]==1)noTA++;
           j++; 
       } 
       j=0;
       while(j<noT[1]){
           if(flagB[j]==1)noTB++;
           j++;
       } 
       cout<<"Case #"<<i+1<<": "<<noT[0]-noTA<<" "<<noT[1]-noTB<<endl;
       i++;
    }
}






