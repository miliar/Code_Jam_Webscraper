// next_permutation
#include <fstream>
#include <iostream>
#include <algorithm>
using namespace std;

int main () {
    

    
    fstream cin("B-large.in");
     ofstream cout("B-large.out");
   
    int casos;
    cin>>casos;
    
    
    
    for(int i=0;i<casos;i++)
    {
         string s;
         cin>>s;
         string s2=s;
         cout<<"Case #"<<i+1<<": ";
         if(next_permutation(s.begin(),s.end()))
            cout<<s;
         else{
              
              sort(s2.begin(),s2.end());
              int min=s2.size()-1;
              for(int j=0;j<s2.size();j++)
              {
                  if(s2[j]!='0'){min=j;break;}                           
              }
              
             cout<<s2[min]<<"0"<<s2.substr(0,min)<<s2.substr(min+1,s2.size()-min-1);
         } 
             
            cout<<endl;
    }
  return 0;
}

