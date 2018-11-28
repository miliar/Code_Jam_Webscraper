#include <iostream>
#include <fstream>
#include<vector>
#include<string>
#include<cmath>
using namespace std;


int main(){
    ifstream in;
    ofstream out;
    int cases;
    out.open("out.txt");
    in.open("A-large.in");
    in>>cases;
    
    for(int i=0;i<cases;i++)
    {
      
         double n=1,k=1;
         in>>n;
         in>>k;
         if(k==0){out<<"Case #"<<i+1<<": OFF\n";continue;}
         if((int)k%(int)pow(2.0,n)==pow(2.0,n)-1){out<<"Case #"<<i+1<<": ON\n";}
         else
         {out<<"Case #"<<i+1<<": OFF\n";}
         
    }
         
         
 system("pause");
 return 0;   
}
