#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

int main() {
  int i,t,j;
  cin>>t;
  
  vector<string> ans;
  int alpha[]={'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
    
  for(i=0;i<t+1;i++) {
    string s;
    getline (cin, s);
  
    if(!s.empty()){
      istringstream iss(s);      
      ans.push_back(iss.str());      
    }
  }
  
  for(i=0;i<ans.size();i++) {
      string s = ans[i];
      
      for(j=0;j<s.size();j++) {
	if(s[j]!=' '){
	  s[j] = alpha[s[j]-'a'];
	}
      }
      cout<<"Case #"<<i+1<<": "<<s<<endl;
  }
  
  return 0;
}