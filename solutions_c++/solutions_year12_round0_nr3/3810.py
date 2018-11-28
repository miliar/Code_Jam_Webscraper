#include <fstream>
#include <iostream>
using namespace std;

ifstream fin ("3.in");
ofstream fout("3.out");

int A,B;

int ord(int n)
{
  if(n==0)
    return 1;
  return 10*ord(n/10);
} 

int cnt(int n)
{
  int p=ord(n)/10,copy=(n%10)*p+(n/10),count=0;
  while(copy!=n)
  {
    if(copy>n&&copy<=B)
      count++;
    copy=(copy%10)*p+(copy/10);
  }
  return count;
}

int main()
{
  int k,t;
  fin >> t;
  for(k=1;k<=t;k++)
  {
    fin >> A >> B;
    int i,count=0;
    for(i=A;i<B;i++)
      count+=cnt(i);
    fout << "Case #" << k << ": " << count << endl;
  }
}