using namespace std;
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <sstream>

int upper_limit(int n)
{
   if(n>=0 && n<=9) return 9;
   else if(n>=10 && n<=99) return 99;
   else if(n>=100 && n<=999) return 999;
   else if(n>=1000 && n<=9999) return 9999;
}

string convert_string(int n)
{
       stringstream ss;
       ss<<n;
       return ss.str();
}

int main()
{
      string str1, str2;
      int testcase,t,a,b,ul,total;
      cin>>t; 
      testcase=0;
      while(t--){
              testcase++;  
              cin>>a>>b;
              total=0;
              for(int n=a; n<=b;n++){
                      ul=upper_limit(n);
                      for(int m=n+1;m<=ul && m<=b;m++){
                              str1=convert_string(n)+convert_string(n);
                              str2=convert_string(m);
                              size_t found=str1.find(str2);
                              if (found!=string::npos){              
                                     total++;
                              }
                      }
              }
              cout<<"Case #"<<testcase<<": "<<total<<endl;
      }
      return 0;
}
