#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

int main(){
 ifstream cin("B-large.in");
 ofstream cout("B-large.out");
 int N;
 string T;
 cin>>N;
 int caso=1;
 while(N--){
   cin>>T;
   string num = T;
    istringstream te(T);
    int elt;
    te >>elt;
   if(next_permutation(num.begin(),num.end())){
      cout<<"Case #"<<caso<<": "<<num<<endl;
   }
   else
    {
      num = num.substr(0,1)  + "0" + num.substr(1);
      /*int tmp;
      while(true){
        istringstream is(num);
        is >> tmp;
        if(tmp>elt)
          break;
        next_permutation(num.begin(),num.end());
      }*/
      int in=-1;
      for(int i=0;i<num.length();i++){
       if(num[i]=='0'){
          in = i;  
       }else{
         if(in== -1 )break;
         
         string ceros;
         for(int h=0;h<=in;h++)
          ceros = ceros + "0";
          
         num = num[i]  + ceros + num.substr(i+1);
         break;
       }      
      }
      
      cout<<"Case #"<<caso<<": "<<num<<endl;
    
    }
    caso++;   
 }
 return 0;   
}
