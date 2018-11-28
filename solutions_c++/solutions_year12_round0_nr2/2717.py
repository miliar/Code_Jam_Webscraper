#include<iostream>
#include<string>
#include<fstream>
#include<cstring>
using namespace std;

int a[110];

int main()
{
 ifstream fin("C:\\data\\gcj2012\\B-small-attempt0.in");
 ofstream fout("C:\\data\\gcj2012\\B-small-attempt0.txt");
 int testcases;
 fin>>testcases;
 for(int testcase=1;testcase<=testcases;++testcase)
 {
  int n,s,p,ret=0;
  fin>>n>>s>>p;
  
  for(int i=0;i<n;++i)
  {
   fin>>a[i];
   int c1=a[i]/3;
   int c2=a[i]%3;
   
   if((c1 + ((c2>0)?1:0))>=p)
   {
    ret++;
   }
   else if(s>0 && a[i]>=3)
   {
    if((c1+1 + (c2==2))>=p)
    {
     ret++;
     s--;
    }
   }
  }
    
  fout<<"Case #"<<testcase<<": "<<ret<<endl;
 }
 fin.close();
 fout.close();
 return 0;    
}
