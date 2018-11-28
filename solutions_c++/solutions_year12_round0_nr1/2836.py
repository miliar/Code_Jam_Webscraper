#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <map>
using namespace std;

int main() {
 ifstream r1("input1");
 ifstream r2("input1_1");

 int T,j;
 string s1,s2;
 string::iterator it,it2;
 map<char,char> mymap;
 map<char,char>::iterator itm;
 char c;
 
 r1>>T;
 for(int i=0;i<=T;i++){
  getline(r1,s1);
  getline(r2,s2);
  if(i!=0){
//  cout<<s1<<endl;
  for( it=s1.begin(),it2=s2.begin(); it<s1.end() && it2<s2.end(); it++,it2++)
//   cout<<*it<<" "<<*it2<<endl;
   mymap[*it]=*it2;
//  cout<<endl;
  }
 }
 mymap['q']='z';
 mymap['z']='q';
// for(itm=mymap.begin();itm!=mymap.end();itm++)
//  cout<<(*itm).first<< " "<<(*itm).second<<endl;

 ifstream r3("A-small-attempt1.in");
 string s3;
 string::iterator it3;
 r3>>T;
 cout<<"Output"<<endl;
 for(int k=0;k<=T;k++){
  getline(r3,s3);
  if(k!=0){
//   cout<<s3<<endl;
   cout<<"Case #"<<k;
   cout<<": ";
   for(it3=s3.begin();it3<s3.end();it3++)
     cout<<mymap[*it3];
   cout<<endl;
   
  }
 }

 return 0;
}
