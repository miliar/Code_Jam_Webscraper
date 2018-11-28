
#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;


int main(int ac, char ** av)
{
  ifstream file;
  char * filename = av[1];
  file.open(filename);
  int num,N,K;
  file >> num;
  for(int i=0; i<num; i++)
    {
      file >> N;
      file >> K;  
      cout << "Case #" << (i+1) << ": ";
      long n = pow(2,N);

      if(K % n == n-1)
        {
          cout << "ON";
        }
      else
        {
          cout << "OFF";
        }
      cout << "\n";
    }
  }
