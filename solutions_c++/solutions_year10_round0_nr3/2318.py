#include<stdio.h>
#include<iostream>
#include<fstream>
#include <vector>
using namespace std;
int main()
{
  ifstream in("C-small-attempt1.in");
  ofstream out("output.out");
  int t;
  in >> t;
  for(int i=1;i<=t;i++)
  {
      long long r ,k,n;
     in >>  r >> k >> n;
     vector<int> qu;
     for(long long j=0;j<n;j++)
     {
         int  g;
         in >> g;
         qu.push_back(g);
     }
     long long sum=0;
     long long  flag=0;
     for(long long j=0;j<r;j++)
     {
         long long count=0;
         for(long long l=0;l<n;l++)
         {
             if(qu[flag]+count > k) break;
             count+=qu[flag];flag=(flag+1)%n;
         }
         sum+=count;
     }
    out << "Case #" << i << ": " << sum << endl;
  }
  out.close();
  in.close();
  return 0;
}

