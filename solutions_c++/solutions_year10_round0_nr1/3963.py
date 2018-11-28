#include <iostream>
#include <ios>
#include <iomanip>
#include <sstream>
#include <cmath>
int main()
{
   std::string s;
   getline(std::cin, s);
   int numCases;
   {
      std::istringstream iss(s);
      iss >> numCases;
   }
   std::cerr << "Expecting " << numCases << " cases" << std::endl;
   int gotCases=0;
   while ( getline(std::cin,s) )
   {
      std::istringstream iss(s);
      int N, K;
      if(iss >> N >> K)
      {
         gotCases++;
         const int criterion = std::pow(2,N);
         const bool lightstatus = ((K % criterion) == criterion-1);
         std::cerr << "N: " << N << " K: " << K << " Light: " << ( lightstatus ? "true" : "false" )<< " HEX:" << std::hex << K << std::endl;
         std::cout << "Case #" << gotCases << ( lightstatus ? ": ON" : ": OFF" ) << std::endl;
      }

   }
   if(gotCases!=numCases)
   {
      std::cerr << "Warning expected " << numCases << " but got " << gotCases << std::endl;
   }
   return 0;
}
