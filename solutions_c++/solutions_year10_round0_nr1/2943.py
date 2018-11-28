#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;
int main()
{
    ifstream in("C:\\A-large.in.txt");
    ofstream out("C:\\tr.txt");
    int t,n,k,i,j;
    in>>t; 
    int order = 1;   
    while(t--)
    {
         in>>n>>k;
         if((k + 1) % (int)pow(2,(double)n) == 0)
                {
                           out<<"Case #"<<order++<<": ON"<<endl;
                          // cout<<"Case #"<<order++<<": ON"<<endl;
                }
          else
                {
                           out<<"Case #"<<order++<<": OFF"<<endl;          
                           //cout<<"Case #"<<order++<<": OFF"<<endl;
                }
    }
    system("pause");
    return 0;
}
             
             
             
             
             
             
             
             
             
                 
                        
