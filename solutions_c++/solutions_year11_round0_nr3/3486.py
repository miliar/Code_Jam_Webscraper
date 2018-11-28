//*** Problem A - Bot Trust
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
int min, numXor, numCur, T, N;
long numTot;

string line;     
ifstream fin ("input.in");
ofstream fout ("output");

fin>>line; //No. of test cases
T = atoi(line.c_str());
for (int i=0;i<T;i++)
{
  
  min=1000001; //10^6+1
  numXor=0; numCur=0;
  numTot=0;
    
  fin>>line; //No. of numbers
  N = atoi(line.c_str());
  for(int j=0; j<N ; j++)
  {
    fin>>line;
    numCur=atoi(line.c_str());
    numXor^=numCur;
    if ((min>numCur)||(j==0)) min=numCur;
    numTot+=numCur;
  }          
   numTot-=min;
   if (numXor==0) fout<<"Case #"<<i+1<<": "<<numTot<<endl;
   else fout<<"Case #"<<i+1<<": "<<"NO"<<endl;
}

fin.close();
fout.close();

system("pause");
}

