//code for Saving the Universe problem
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VII;
typedef vector<double> VD;
typedef vector<LD> VLD;
typedef vector<LL> VLL;
typedef vector<bool> VB;


long MakeCase(FILE *A_file)
{
   if(!A_file)
      return 0;

   long nResult  = 0;
   long P  = 0;
   long K  = 0;
   long L  = 0;
   long tmp  = 0;
   vector<long>  vec;

   fscanf(A_file, "%ld", &P);
   fscanf(A_file, "%ld", &K);
   fscanf(A_file, "%ld", &L);

   for(long nInd = 0; nInd < L; ++nInd)
   {
      fscanf(A_file, "%ld", &tmp);
      vec.push_back(tmp);
   }

   sort(vec.begin( ), vec.end( ), greater<long>());

   int x = 0;
   for(long j = 1; j <= P; ++j)
   {
      for(long i = 0; i < K; ++i)
      {
         nResult += vec[x++] * j;
         if(x == L)
            break;
      }
      if(x == L)
         break;
   }

   return nResult;
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
