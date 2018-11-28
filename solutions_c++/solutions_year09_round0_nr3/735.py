#include <iostream>
#include <cstring>


#define MAX_N 100
#define MAX_L 500
#define MAGIC_PHRASE "welcome to code jam"
#define MAGIC_PHRASE_LETTER_COUNT 19


int N; //Test cases count
int count; //Answer
using namespace std;

FILE *fin = fopen("C-small.in", "r");
FILE *fout = fopen("result.txt", "w");

void dpSearch(char * str, int length)
{
   int dpArray[MAX_L+1][MAGIC_PHRASE_LETTER_COUNT+1];
   memset(dpArray, 0, sizeof(dpArray));
   
   for (int i = 0; i <= length; i++)
   {
      dpArray[i][MAGIC_PHRASE_LETTER_COUNT] = 1;
   }
   for (int i = length-1; i >= 0; i--)
   {
      for (int j = MAGIC_PHRASE_LETTER_COUNT - 1; j >= 0; j--)
      {
         dpArray[i][j] = dpArray[i+1][j];
         
         if (MAGIC_PHRASE[j] == str[i])
         {
            dpArray[i][j] += dpArray[i][j+1];
            dpArray[i][j] %= 10000;
         }
      }
   }
   
   count = dpArray[0][0];
}
void printAnswerWithZeros(int caseNo)
{
   if (count < 10) fprintf(fout, "Case #%d: 000%d\n", caseNo+1, count);
   else if (count < 100) fprintf(fout, "Case #%d: 00%d\n", caseNo+1, count);
   else if (count < 1000) fprintf(fout, "Case #%d: 0%d\n", caseNo+1, count);
   else fprintf(fout, "Case #%d: %d\n", caseNo+1, count);
}
int main ()
{
   fscanf(fin, "%d\n", &N);
   
   for (int k=0; k < N; k++)
   {
      count = 0;
      
      char str[MAX_L];
      int i = 0;
      for (; ; i++)
      {
         char tmp;
         fscanf(fin, "%c", &tmp);
         if (tmp == '\n') break;
         else
         {
            str[i] = tmp;           
         }
      }

      
      
      dpSearch(str, i);
      printAnswerWithZeros(k);
   }
   
   
   fclose(fin);
   fclose(fout);
   
   return 0;
}
