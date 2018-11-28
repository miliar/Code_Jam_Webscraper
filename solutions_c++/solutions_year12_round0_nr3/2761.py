#include<iostream>
#include<string>
#include<fstream>
#include<cstring>
#include<map>
using namespace std;

int B,A;
map<pair<int,int>, int> M;
void solve(int n)
{
 if(n<10)return;
 int b=10,ret=0,b1=10;
 while(n/b1>0){b1*=10;}b1/=10;
 while(n/b>0)
 {
  int p2 = n%b;
  int p1 = n/b;
  
  if(p2>=b/10)
  {
   int m = p2*b1+p1;
   if(m <=B && m>n)M[make_pair(n,m)]++;
  }
  
  b*=10;
  b1/=10;
 }    
}

int main()
{
 //ifstream fin("C:\\data\\gcj2012\\C-small-attempt0.in");
 //ofstream fout("C:\\data\\gcj2012\\C-small-attempt0.txt");
 ifstream fin("C:\\data\\gcj2012\\C-large.in");
 ofstream fout("C:\\data\\gcj2012\\C-large.txt");
 int testcases;
 fin>>testcases;
 for(int testcase=1;testcase<=testcases;++testcase)
 {
  M.clear();
  int ret=0;
  fin>>A>>B;
  for(int i=A;i<B;++i)
   solve(i);
  ret=M.size();
  fout<<"Case #"<<testcase<<": "<<ret<<endl;
 }
 fin.close();
 fout.close();
 return 0;    
}
