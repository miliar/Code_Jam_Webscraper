#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef vector<string> vs;

vi parsevi(string s){
  int k;
  vi v;
  istringstream sin(s);
  while(sin>>k){
   v.push_back(k);
  }
  return v;
}
   
main()
{
  string s;
  int t;
  cin>>t;
  getline(cin,s);

  int test_case_num=1;
  while(test_case_num<=t){
   getline(cin,s);
   if(next_permutation(s.begin(),s.end())==false){
     sort(s.begin(),s.end());
     char c;
     for(string::iterator it1=s.begin();it1!=s.end();it1++){
       if(*it1 != '0'){
         c=*it1;
         break;
       }
     }
     string temp;
     temp.push_back(c);
     temp.push_back('0');
     temp.append(s);
     string::iterator it= find(temp.begin()+1,temp.end(),c);
     temp.erase(it);
     s.clear();
     s = temp;
   }
   cout<<"Case #"<<test_case_num<<": "<<s<<endl;
   test_case_num++;
  }
}
