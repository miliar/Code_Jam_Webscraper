#include<iostream>
#include<math.h>
#include<fstream.h>
using namespace std;

int main()
{
    int T = 0,N = 0,Ci, r_xor = 0, sum = 0;
    long long small = 1000000 + 1;
    int i = 0;
    
    ofstream out;
    ifstream in;
    in.open("in.txt");
    out.open("out.txt");
    in>>T;
    for( i=1; i<=T; i++)
    //while(T)
    {
      cout<<"Test case:" << T<<"\n";
      in>>N;
      //Ci = new int[N];
      Ci = 0;
      r_xor = sum = 0 ;
      small = 1000000 + 1;
      while(N)
      {
        in>>Ci;
        cout<<Ci<<" ";
        r_xor = r_xor^Ci;
        if(Ci<small)
          small = Ci;
        sum+=Ci;
        N--;
      }
      cout<<"Sum: "<< sum<<" Xor result:" <<r_xor;
      if(r_xor == 0)
      {
        out<<"Case #"<<i<<": "<<sum-small<<"\n";
        
      } else
      {
            out<<"Case #"<<i<<": "<<"NO"<<"\n";
      }
      cout<<"\n";
      //delete []Ci;
      //T--;
    }
    getchar();  
      
}
