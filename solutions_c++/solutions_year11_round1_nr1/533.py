#include<iostream>
#include<fstream>
#include<cstdlib>
using namespace std;


int main()
{
    fstream input,output;
    input.open("1.txt",ios::in);    
    output.open("2.txt",ios::out);    
    
    long long int t,T,N,pd,pg;
    string ans;
    
    input>>T;
    for(t=1;t<=T;t++) {
      input>>N>>pd>>pg;
      if((pg==100 && pd!=100)||(pg==0&&pd!=0))
      {
         cout<<"boundry\n";
         ans="Broken";
      } else if(pd==0)
      {
         cout<<"pd=0\n"   ;
         ans = "Possible";
      } else
      {
         int d;
         for(d=pd;d>1;d--) if(pd%d==0 && 100%d==0) break;
         int p = 100 / d;
         cout<<"p="<<p<<" N="<<N<<endl;
         p<=N ? ans="Possible" : ans="Broken";
      }

      cout<<"Case #"<<t<<": "<<ans<<endl;
      output<<"Case #"<<t<<": "<<ans<<endl;
    }
    
    system("pause");
    return 0;
    
}
