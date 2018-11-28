#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

inline bool doProblem(int N, unsigned int K)
{
   unsigned int p = pow(2,N);
   return (K % p) == (p - 1);
}

int main(int argc, char *argv[])
{
   ifstream input ("input.in", ifstream::in);
   ofstream output("output.out", ofstream::out);

   int caseNum;
   input >> caseNum;

   int c = 1;
   while (c <= caseNum)
   {
      int N;
      unsigned int K;
      input >> N >> K;
      const char *s;
      if (doProblem(N, K))
         s = "ON";
      else
         s = "OFF";
      output << "Case #" << c << ": " << s << endl;
      ++c;
   }

   input.close();
   output.close();
}
