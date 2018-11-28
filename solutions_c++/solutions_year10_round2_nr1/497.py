#include <iostream>
#include <map>
using namespace std;

int main(){
  
  int t;
  cin >> t;
  
  int o = t;
  while (t--){
    map<string,bool> a;
    a.clear();
    cout << "Case #"<<o-t <<": ";
    int n,m,ans=0;
    cin >> n >> m;
    string s,t="";
    a[""] = true;
    a["/"] = true;
    for (int i = 0; i < n; ++i){
      cin >> s;
      t="";
      for (int j = 0; j < s.length(); ++j){
	if (s[j]=='/'){
	  if (a.find(t)==a.end())
	    a[t] = true;
	}
	t+=s[j];
      }      
      if (a.find(t)==a.end() && t[t.length()-1]!='/')
	a[t] = true;
    }    
    for (int i = 0; i < m; ++i){
      cin >> s;
      t = "";
      for (int j = 0; j < s.length(); ++j){
	if (s[j]=='/'){
	  if (a.find(t)==a.end()){
	    a[t] = true;
	    ++ans;
	  }
	}
	t+=s[j];
      }
      if (a.find(t)==a.end() && t[t.length()-1]!='/'){
	a[t] = true;
	++ans;
      }
    }
    cout << ans <<endl;
  }
}

