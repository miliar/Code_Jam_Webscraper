#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

int compkey(int num, int max)
{
  stringstream ssA;
  stringstream ssB;
  stringstream ssM;
  string KA;
  string KB;
  int dig;
  int i, j;
  int ret = 0;
  int VA, VB;
//num=1234;

  ssA << num;
  ssB << num;
  ssM << max;

  dig = ssA.str().length();

  KA = ssA.str() + ssA.str().substr(0, dig-1);
  KB = ssB.str() + ssB.str().substr(0, dig-1);
  for(i=0; i<dig; i++)
  {
    if(KA.substr(i,dig) >= ssA.str())
    {
      for(j=0; j<dig; j++)
      {
        if((KA.substr(i,dig) < KB.substr(j,dig)) && (KB.substr(j,dig)<=ssM.str()))
        {
          ret++;
//          cout<<KA.substr(i,dig)<<" "<<KB.substr(j,dig)<<endl;
          j=dig; // Unique pairs...
        }
      }
    }
  }

  return ret;
}

int main()
{
  ifstream input;
  string line;
  short N;
  int min;
  int ans;
  int dig;
  int i, j, k;
  int A, B;

  short keyI[10], keyJ[10];

  input.open("C-small-attempt0.in");
  getline(input, line);
  N = atoi(line.c_str());

  for(int run=1; run<N+1; run++)
  {
    input >> A;
    input >> B;

    ans = 0;
    dig = 1;

    if(A>1000000)
      dig=7;
    else if(A>=100000)
      dig=6;
    else if(A>=10000)
      dig=5;
    else if(A>=1000)
      dig=4;
    else if(A>=100)
      dig=3;
    else if(A>=10)
      dig=2;

    if(dig!=1)
    {
      for(j=A; j<B; j++)
      {
        ans+=compkey(j, B);
      }
    }

#if(0)
4
1 9 (0)
10 40 (3)
100 500 (156)
1111 2222 (287)
#endif

    std::cout << "Case #" << run << ": " << ans << std::endl;
  }
  return 0;
}
