//*** Problem B - Dancing with Googlers
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int T,N,s,p,score,result;     

int main()
{
 string line;     

 ifstream fin ("input.in");
 ofstream fout ("output");

 fin>>line;
 T=atoi(line.c_str());

for (int i=0;i<T;i++)
 {
  fin>>line;
  N=atoi(line.c_str());
  fin>>line;
  s=atoi(line.c_str());
  fin>>line;
  p=atoi(line.c_str());
  
  score=0;
  result=0;
  for(int j=0;j<N;j++)
  {
   fin>>line;
   score=atoi(line.c_str());
    if ((score!=0) || (p==0))
    {
     if ((score/3)+((score%3)==0?0:1)>=p)
     result++;
     else
      if ((s>0) && ((score/3)+((score%3)==2?2:0)+((score%3)==0?1:0)>=p))
       {
        result++;
        s--;         
       }     
    }
   }
  fout<<"Case #"<<i+1<<": "<<result<<endl;
  
 }

fin.close();
fout.close();

system("pause");

 }

