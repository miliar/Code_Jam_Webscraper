#include<iostream>
#include<fstream>
#include<cstdlib>
using namespace std;


int main()
{
    fstream input,output;
    input.open("in.txt",ios::in);    
    output.open("out.txt",ios::out);    
    
    unsigned long long int t,T,N,i,j,k,min;
    unsigned long long int temp,yes;
    unsigned long long int ans;
    input>>T;
    for(t=1;t<=T;t++) {
      input>>N;
      yes=0;
      ans=0;
      for(i=0;i<N;++i) {
         input>>temp;
         if(i==0) min=temp;
         else if(temp<min) min=temp;
         ans+=temp;
         yes=yes^temp;
      }
      
      ans=ans-min;
//      cout<<yes;
      if(yes==0)
      output<<"Case #"<<t<<": "<<ans<<endl;
      else
      output<<"Case #"<<t<<": NO"<<endl;
    }
    
    system("pause");
    return 0;
    
}
