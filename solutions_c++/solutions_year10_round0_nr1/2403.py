#include<stdio.h>
#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
int main()
{
  ifstream in("A-large.in");
  ofstream out("output.out");
  int t;
  in >> t;
  for(int i=1;i<=t;i++)
  {

      long long n ,k;
      in >> n >> k;
      int j;
      long long l= (1 << n ) -1;
      j=1;
      bool flag=true;
      do
      {
          if(l == k)
          {
              out << "Case #"<< i << ": ON" << endl;
              flag=false;
              break;
          }
          j++;
          l=((1 << n) -1)*j+(j-1);
      }while(l<=k);
      if(flag)
      out << "Case #" << i <<": OFF" << endl;
  }
  out.close();
  in.close();
  return 0;
}

