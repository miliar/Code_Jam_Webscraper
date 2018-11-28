#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <string>
using namespace std;


int main()
{
      unsigned int T, N, M, tCase;
      int i, j;
      int *A, *B, cuts;
      ifstream inFile;
      ofstream outFile;
      inFile.open("C:\\Documents and Settings\\Administrator\\Desktop\\A-small.in");
      outFile.open("C:\\Documents and Settings\\Administrator\\Desktop\\A-small-out.txt");

      inFile >> T;
      for (tCase=1; tCase <= T; tCase++)
      {
          inFile >> N;
          A = new int[N];
          B = new int[N];
          for (i=0; i < N; i++)
          {
              inFile >> A[i];
              inFile >> B[i];
          }
          cuts = 0;
          for (i=0; i < N; i++)
          {
              for (j=i+1; j < N; j++)
              {
                  if ((A[i] == A[j]) || (B[i] == B[j]))
                     continue;
                  if ((A[i] >= A[j]) && (B[i] >= B[j]))
                     continue;
                  if ((A[i] > A[j]) && (B[i] < B[j]))
                     cuts++;
                  if ((A[i] < A[j]) && (B[i] > B[j]))
                     cuts++;
              }
          }
          outFile << "Case #" << tCase << ": " << cuts << "\n";
      }

}
