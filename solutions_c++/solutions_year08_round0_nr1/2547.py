#include "stdio.h"
#include "stdlib.h"
#include "string.h"

struct cases{
   char SE[100][100];
   char QR[1000][100];
   };

int SECount[20];
int QRCount[20];

int distance[100];

struct cases C[20];
int CCount = 0;

char* readString (FILE * inFile)
   {
   char *str=(char *) malloc (sizeof(char)*100);
   int index=0;
   char ch=fgetc(inFile);
   while (ch != '\n')
      { 
      if (feof(inFile))
         break;
      str[index++]=ch;
      ch=fgetc(inFile);
      }
   str[index]='\0';
   return str;
   }
   
void readFile()
   {
   FILE * inFile = fopen("./testfile.txt", "r");
   char str1[100];
   strcpy(str1,  readString(inFile));
   CCount = atoi(str1);
   for (int i =0; i<CCount; i++)
      {
      strcpy(str1,  readString(inFile));
      SECount[i] = atoi(str1);
      for (int j = 0; j<SECount[i]; j++)
         strcpy(C[i].SE[j], readString(inFile));
      strcpy(str1,  readString(inFile));
      QRCount[i] = atoi(str1);
      for (int j = 0; j<QRCount[i]; j++)
         strcpy(C[i].QR[j],  readString(inFile));
      }
   }

int getDistance(int caseId, int QRIndex, char str[100])
   {
   int count = -1; int matched = 0;
   for (int j=QRIndex; j< QRCount[caseId]; j++)
      {
      count = count + 1;
      if (!(strcmp(C[caseId].QR[j], str)))
         {
	 matched = 1;
         break;}
      }
   if (matched == 0)
      return (QRCount[caseId] + 1);
   else
      return(count);
   }

int getSwitchCount(int caseId)
   {
   int count = -1;
   int QRIndex = 0;
   if (QRCount[caseId]==0) return (0);
   while (QRIndex < QRCount[caseId])
      {
      int maxDist = -1; int maxDistSE = -1;
      // compute the distance of all SE for current QR index
      for (int i = 0; i < SECount[caseId]; i++)
         {
         int d = getDistance(caseId, QRIndex, C[caseId].SE[i]);
         if (d > maxDist)
            {
            maxDist = d;
            maxDistSE = i;
            }
         }
      count = count + 1;
      QRIndex += maxDist;      
      }
   return (count);
   }

int main()
   {
   readFile();
   for (int i = 0; i<CCount; i++)
      {
      int count = getSwitchCount(i);
      printf ("Case #%d: %d\n", i+1, count);
      }
   }

