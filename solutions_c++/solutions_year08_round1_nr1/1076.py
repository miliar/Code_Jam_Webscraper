#include "stdio.h"
#include "stdlib.h"
#include "string.h"

int CCount;
int VLength[1000];
int VXData[1000][1000];
int VYData[1000][1000];
int VRes[1000];


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
   FILE * inFile = fopen("c:/testfile.txt", "r");
   char str1[100];
   strcpy(str1,  readString(inFile));
   CCount = atoi(str1);
   for (int i =0; i<CCount; i++)
      {
      strcpy(str1,  readString(inFile));
      VLength[i] = atoi(str1);
      for (int j = 0; j<VLength[i]; j++)
         {
         strcpy(str1,  readString(inFile));
         VXData[i][j] = atoi(str1); 
         }
      for (int j = 0; j<VLength[i]; j++)
         VYData[i][j] = atoi(readString(inFile));
      }
   }

int minIndex (int * data, int startIndex, int endIndex)
   {
   int minVal = data[startIndex]; int minValIndex = startIndex;
   for (int i = startIndex+1; i <=endIndex; i++)
      {
      if (minVal > data[i]) 
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
      int newPlace = minIndex(data, i, length-1);
      int temp = data[i];
      data[i] = data[newPlace];
      data[newPlace] = temp;
      }
   return (data);
   }


int main()
   {
   readFile();
   FILE * outFile = fopen("c:/resultfile.txt", "w");
   for (int i=0; i<CCount; i++)
      {
      int prod = 0;
      int *tempX;
      tempX = sortList(VXData[i], VLength[i]);
      for (int j=0; j<VLength[i]; j++)
         {VXData[i][j] = tempX[j];}
      tempX = sortList(VYData[i], VLength[i]);
      for (int j=0; j<VLength[i]; j++)
         VYData[i][j] = tempX[j];

      for (int j=0; j < VLength[i]; j++)
          prod += VXData[i][j]*VYData[i][VLength[i] - 1 - j];

      printf ("%d \n", prod);
      fprintf (outFile, "Case #%d: %d \n", i+1, prod);
      //writeString (outFile, prodString);
      }


   getchar();
   }
