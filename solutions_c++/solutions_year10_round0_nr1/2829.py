#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;
int main()
{
    int cases,num,div;
    double temp,clicks;
    ifstream in("A-large.in");
    ofstream out("A-smallout.txt");
    in>>cases;
    for(int i=1;i<=cases;i++)
            {
              out<<"Case #"<<i<<": ";
             in>>num;
             temp=pow(2,num);
             in>>clicks;
             
             div=int((clicks+1))%int(temp);
             if(div==0)
             out<<"ON";
             else
             out<<"OFF";
             out<<endl;
            }
  in.close();
  out.close();  
    }
    
