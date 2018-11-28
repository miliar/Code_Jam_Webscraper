#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "math.h"

int CCount;

struct caseInfo
   {
   int maxLabelsPerKey; int totalKeys; int maxLabels;
   int *labelFreq;
   };
struct caseInfo * C;

char* readString (FILE * inFile)
   {
   char *str=(char *) malloc (sizeof(char)*100);
   int index=0;
   char ch=fgetc(inFile);
   while (!((ch == '\n') || (ch == ' ')))
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
   FILE * inFile = fopen("c:/MNtestfile.txt", "r");
   char str1[100];
   strcpy(str1,  readString(inFile));
   CCount = atoi(str1);   
   C = (struct caseInfo *) malloc(sizeof(struct caseInfo) * CCount);
   for (int i =0; i<CCount; i++)
      {
      strcpy(str1,  readString(inFile));
      C[i].maxLabelsPerKey = atoi(str1);

      strcpy(str1,  readString(inFile));
      C[i].totalKeys = atoi(str1);
      strcpy(str1,  readString(inFile));
      C[i].maxLabels = atoi(str1);
      C[i].labelFreq = (int*) malloc(sizeof(int)*C[i].maxLabels);
      for (int j=0; j<C[i].maxLabels; j++)
         {
         strcpy(str1,  readString(inFile));
         C[i].labelFreq[j] = atoi(str1);         
         }
      }
   }


int maxIndex (int * data, int startIndex, int endIndex)
   {
   int minVal = data[startIndex]; int minValIndex = startIndex;
   for (int i = startIndex+1; i <=endIndex; i++)
      {
      if (minVal < data[i]) 
         {
         minVal = data[i];
         minValIndex = i;
         }
      }
   return (minValIndex);
   }

int* sortList(int data[1000], int length)
   {
   int *newData = (int*) malloc(sizeof(int)*length);
   int newIndex = 0;
   for (int i = 0; i < length; i++)
      {
      int newPlace = maxIndex(data, i, length-1);
      int temp = data[i];
      data[i] = data[newPlace];
      data[newPlace] = temp;
      }
   return (data);
   }



   


int main()
   {
   FILE * resultFile  = fopen ("c:/resultfile.txt", "w");
   readFile();
   for (int i=0; i<CCount; i++)
      {
      if ((C[i].maxLabelsPerKey * C[i].totalKeys ) < C[i].maxLabels)
         {
         printf ("Case #%d: Impossible\n", (i+1));
         fprintf (resultFile, "Case #%d: Impossible\n", (i+1));
         continue;
         }
      int * b = sortList(C[i].labelFreq, C[i].maxLabels);
      int * pressFreq = (int *) malloc(sizeof(int) * C[i].maxLabels);
      int pressCount = 1; int labelIndex = 0; int totalPressCount = 0;
      for (int j=0; j < C[i].maxLabels; j+= C[i].totalKeys)
         {
         for (int k=0; k <C[i].totalKeys; k++)
            {
            if (labelIndex == C[i].maxLabels) break;
            totalPressCount += b[labelIndex]* pressCount;
            labelIndex ++;
            }
         pressCount++;
         }
      printf ("Case #%d: %d\n", (i+1), totalPressCount);
      fprintf (resultFile, "Case #%d: %d\n", (i+1), totalPressCount);
      }
   getchar();
   }
