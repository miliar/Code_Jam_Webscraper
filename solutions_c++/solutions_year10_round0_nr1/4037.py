#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int exponential (int base, int power);

int main ()

{
ifstream in;
in.open("A-large.in");
ofstream out;
out.open("A-large.out");
   
   long long int N, K, cases;
   in >> cases;
    
   
   for (long long int cnumber = 1; cnumber <= cases; cnumber++)
     {
      in >> N;
      in >> K;
      long long int ans = 0;
      
      for (long long int a = 0; a < N; a++) 
           ans = ans + exponential (2,a);
      
      if ((K == 1 || K%2 ==1) && N == 1)
         out << "Case #" << cnumber << ": ON" << endl;
      else if (K%2 == 0 && N == 1)
         out << "Case #" << cnumber << ": OFF" << endl;  
      else 
      {
      long long int remain = K-ans;
      if (ans == K || (remain%(ans+1) == 0))
          out << "Case #" << cnumber << ": ON" << endl;
      
      else out << "Case #" << cnumber << ": OFF" << endl;
      } 
      }
}


int exponential (int base, int power)
{
    long long int answer = 1;
    for (long long int a = 0; a < power; a++)
       answer = answer * base;
    return answer;
}

