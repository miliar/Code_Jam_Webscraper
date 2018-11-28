#include<iostream>
#include<fstream>
#include<algorithm>
#include<string>
#include<vector>
#include<numeric>
using namespace std;

main()
{
 ifstream fin;
 fin.open("C:\\data\\B-large.in");
 ofstream fout;
 fout.open("C:\\data\\B-large.out");
 int t;
 fin>>t;
 string str;
 for(int i=1;i<=t;++i)
 {
  fout<<"Case #"<<i<<": ";
  fin>>str;
  vector<char> A;
  for(int j=0;j<str.size();++j)
  A.push_back(str[j]);
  
  bool ok=next_permutation(A.begin(),A.end());
  if(ok)
  {
   for(int j=0;j<A.size();++j)fout<<A[j];      
  }
  else
  {
      string pr;
      sort(A.begin(),A.end());
      int cnt=0;
      for(int j=0;j<A.size();++j)if(A[j]=='0')cnt++; else pr+=A[j];
      cnt++;
      fout<<pr[0];
      while(cnt--)fout<<"0";
      for(int j=1;j<pr.size();++j)fout<<pr[j];
  }
  fout<<endl;        
 } 
 fin.close();
 fout.close();
}
