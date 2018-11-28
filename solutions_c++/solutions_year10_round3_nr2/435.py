#include<iostream>
#include<vector>
#include<fstream>
using namespace std;

int main()
{
    
    fstream input;
    string s;
    cin>>s;
    
    input.open(s.c_str(),ios::in);
    int T;
    input>>T;
    
    
    fstream output;
    output.open("output.txt",ios::out);
  
    for(int testcase=0;testcase<T;testcase++)
    {
            long long  L,P,C;
            input>>L>>P>>C;
            long long  cnt=0;
while(P>L) {
cnt++;
if (P%C==0) P=P/C;
else P=(P/C)+1;
}
--cnt;
long long  ans=0;
long long  st=1;
while(st<=cnt) { st*=2;ans++;}
//cout<<ans<<endl;

      
            output<<"Case #"<<testcase+1<<": "<<ans<<endl;

            
            
            
            
    }  
   
   
   
   
   
   
    input.close();
    output.close();
    system("pause");
    return 0;
    
        
    
    
    
}
