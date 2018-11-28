#include <cmath>
#include <fstream>

int main()
{
      unsigned long T;
      unsigned long K, state;
      unsigned long N, tCase;
      ifstream inFile;
      ofstream outFile;


      inFile.open("C:\\Documents and Settings\\Administrator\\Desktop\\A-small.in");
      outFile.open("C:\\Documents and Settings\\Administrator\\Desktop\\A-small-out.txt");

      inFile >> T;
      for (tCase=1; tCase <= T; tCase++)
      {
          inFile >> N;
          inFile >> K;
          outFile << "Case #" << tCase << ": ";

          if ((K+1)% ((unsigned long)pow(2,N)) == 0)
             outFile << "ON\n";
          else
             outFile << "OFF\n";
      }

      inFile.close();
      outFile.close();
      return 0;
}
