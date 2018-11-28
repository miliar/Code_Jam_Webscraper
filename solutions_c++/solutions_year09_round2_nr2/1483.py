#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

int main(){
    int t;
    cin>>t;
    for(int cont=0; cont<t; cont++){
       unsigned long long n,i,j;
       cin>>n;
       stringstream foo;
       foo<<n;
       string str=foo.str();
       vector<int> digits(10,0);
       for(i=0; i<str.size(); i++)
          digits[str[i]-'0']++;       
       if(digits[0]==str.size()-1){          
          cout<<"Case #"<<cont+1<<": "<<n*10<<endl;
          continue;
       }  
       if(count(digits.begin()+1,digits.end(),0)==8){
          for(j=1; j<10; j++)
             if(digits[j]!=0)
                break;
          if(digits[0]==str.size()){          
             cout<<"Case #"<<cont+1<<": "<<n*10<<endl;
             continue;
          }
       }                                              
       for(i=n+1; ; i++){          
          stringstream bar;
          bar<<i;
          string str2=bar.str();
          vector<int> digits2(10,0);
          for(j=0; j<str2.size(); j++)
             digits2[str2[j]-'0']++;
          bool equal=true;
          for(j=1; j<10; j++)
             if(digits2[j]!=digits[j])
                equal=false;
          if(equal){
             cout<<"Case #"<<cont+1<<": "<<i<<endl;
             break;
          }
       }       
    }
    return 0;
}
