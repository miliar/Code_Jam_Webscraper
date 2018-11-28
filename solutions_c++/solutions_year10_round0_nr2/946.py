#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int NOD(unsigned long long a,unsigned long long b)
{
  while(a!=0 && b!=0)
  {
    if(a>=b) a=a%b;
    else b=b%a;
  }
  return a+b;
}

int main () {
  ifstream file("B-small-attempt0.in");
  ofstream file2("B-small-attempt0.out");
  if (file.is_open() && file2.is_open())
  {
    int T, N;
    file >> T;
    for (int i = 0; i < T; i++)
    {
      file >> N;
      unsigned long long *t = new unsigned long long[N]; 
      unsigned long long *t2 = new unsigned long long[N];
      
      for (int h=0;h<N; h++)
      {
        file >> t[h];
      }
      t2[0] = abs(t[0] - t[1]);
      for (int h=1;h<N-1; h++)
        t2[h] = abs(t[h] - t[h+1]);

      if (N > 2)
      {
        unsigned long long tmp = NOD(t2[0],t2[1]);
        for (int j=1;j<N-1; j++)
        {
          tmp = NOD(t2[j],tmp);
        }
        t2[0] = tmp;
      }

      unsigned long long mintime = t[0];
      for (int h=1; h < N; h++)
      {
        if (t[h] < mintime)
          mintime = t[h];
      }

      unsigned long long res = (mintime%t2[0] != 0) ? t2[0] - (mintime%t2[0]) : 0;

      cout << "case" << i+1 << endl;
      file2 << "Case #" << i+1 << ": " << res;
      if (i != T - 1)
        file2 << endl;

      delete[] t;
      delete[] t2;
    }
    
    file2.close();
    file.close();
  }
  else cout << "Unable to open file"; 

  return 0;
}