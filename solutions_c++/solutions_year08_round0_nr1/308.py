//code for Saving the Universe problem
#include <stdio.h>
#include <set>
#include <string>
using namespace std;

#define MAX_NAME  100

void ReadLineFromFile(FILE *A_file, char *A_strLine)
{
   if(!A_file)
      return;

   int         nIndex   = 0;
   char        ch       = 0;

   ch = fgetc(A_file);
   while(nIndex < MAX_NAME && ch != '\n' && !feof(A_file))
   {
      A_strLine[nIndex++] = ch;
      ch = fgetc(A_file);
   }
   A_strLine[nIndex] = 0;
};


long MakeCase(FILE *A_file)
{
   if(!A_file)
      return -1;
   set<string>       setServers;
   long              nServerNumber        = 0;
   long              nSwitches            = 0;
   long              nQueryNumber         = 0;
   long              ind                  = 0;
   char              strServerName[MAX_NAME + 1];
   char              chEL;

   fscanf(A_file, "%ld%c", &nServerNumber, &chEL);
   for(ind = 0; ind < nServerNumber; ++ind)
      ReadLineFromFile(A_file, strServerName);

   fscanf(A_file, "%ld%c", &nQueryNumber, &chEL);
   for(ind = 0; ind < nQueryNumber; ++ind)
   {
      ReadLineFromFile(A_file, strServerName);
      setServers.insert(strServerName);
      if(setServers.size() == nServerNumber)
      {
         setServers.clear();
         ++nSwitches;
      }
      setServers.insert(strServerName);
   }

   return nSwitches;
};

int main()
{
   long              nCases            = 0;
   long              nCurrentCase      = 0;
   FILE             *fileInput         = NULL;
   FILE             *fileOutput        = NULL;

   fileInput = fopen("input.txt", "r");
   if(!fileInput)
      return -1;

   fileOutput = fopen("output.txt", "w");
   if(!fileInput)
      return -1;

   fscanf(fileInput, "%ld", &nCases);
   for(nCurrentCase = 1; nCurrentCase <= nCases; ++nCurrentCase)
   {
      fprintf(fileOutput, "Case #%ld: %ld\n", nCurrentCase, MakeCase(fileInput));
   }
   fclose(fileInput);
   fclose(fileOutput);
   return 0;
}