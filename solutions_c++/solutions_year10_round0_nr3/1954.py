#include <fstream>

int main()
{
      unsigned int T, N, tCase;
      unsigned long R, repeatRounds, remainingRounds;
      unsigned long long totEuros, K, *cumEuros, repeatEuros;
      unsigned long long *group;
      unsigned long long tmpCap;
      unsigned long startGrpIndex;
      unsigned long  *lastGroupInARound;
      ifstream inFile;
      ofstream outFile;


      inFile.open("C:\\Documents and Settings\\Administrator\\Desktop\\C-large.in");
      outFile.open("C:\\Documents and Settings\\Administrator\\Desktop\\C-large-out.txt");

      inFile >> T;
      for (tCase=1; tCase <= T; tCase++)
      {
          inFile >> R;
          inFile >> K;
          inFile >> N;
          group = new unsigned long long[N];
          for (unsigned long i=0; i<N; i++)
              inFile >> group[i];
          lastGroupInARound =  new unsigned long[N];
          for (unsigned long j=0; j<N; j++)
             lastGroupInARound[j] = 0;
          cumEuros = new unsigned long long[N];
          for (unsigned long l=0; l<N; l++)
             cumEuros[l] = 0;
          unsigned long nxtGrp=0;
          unsigned long prvGrp=0;
          totEuros=0;
          for (unsigned long round=1; round <=R; round++)
          {
              tmpCap=0;
              startGrpIndex =nxtGrp;
              while (1)
              {
                if (tmpCap+group[nxtGrp] <= K)
                   tmpCap+= group[nxtGrp];
                else
                {
                    if (lastGroupInARound[prvGrp] != 0)
                       break;
                    lastGroupInARound[prvGrp] = round;
                    break;
                }
                prvGrp = nxtGrp;
                nxtGrp = (nxtGrp+1)%N;
                if (nxtGrp == startGrpIndex)
                {
                   if (lastGroupInARound[prvGrp] != 0)
                       break;
                   lastGroupInARound[prvGrp] = round;
                   break;
                }
              }
              totEuros+= tmpCap;
              if (lastGroupInARound[prvGrp] == round)
                 cumEuros[prvGrp] = totEuros;
              else if (lastGroupInARound[prvGrp] != 0)
              {
                   repeatRounds = round-lastGroupInARound[prvGrp];
                   repeatEuros = totEuros-cumEuros[prvGrp];
                   remainingRounds=R-round;
                   if (remainingRounds >= repeatRounds)
                   {
                      totEuros += repeatEuros*(remainingRounds/repeatRounds);
                      round += (remainingRounds/repeatRounds)*repeatRounds;
                   }
              }
          }

          outFile << "Case #" << tCase << ": " << totEuros << "\n";
          delete []group;
          delete []lastGroupInARound;
      }

      inFile.close();
      outFile.close();
      return 0;
}

