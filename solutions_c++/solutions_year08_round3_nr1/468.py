#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cctype>
#include <string>

using namespace std;
bool gt(long long i,long long j) { return (i>j); }
int main(int argc,char *argv[])
{
  int N,P,K,L;
  register int newno;
  long long nomin;
  vector<long long> freq;
  ifstream ifile(argv[1]);
  ofstream ofile(argv[2]);
  ifile>>N;
  cout<<N;
  for(int i=1;i<=N;i++)
  {
    ofile<<"Case #"<<i<<": ";
    cout<<"Case #"<<i<<": ";
    nomin=0;
    ifile>>P>>K>>L;
    freq.clear();
    for(register int j=0;j<L;j++)
    {
      ifile>>newno;
      freq.push_back(newno);
    }
    sort(freq.begin(),freq.end(),gt);
    for(register int p=1,j=0;p<=P && j<L;p++)
    {
      for(register int k=1;k<=K && j<L;j++,k++)
	nomin+=p*freq[j];
    }
    ofile<<nomin<<endl;
    cout<<nomin<<endl;
  }
  ifile.close();
  ofile.close();
  return 0;
}