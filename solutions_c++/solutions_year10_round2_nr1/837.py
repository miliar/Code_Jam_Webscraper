#include<iostream>
#include<cstdio>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<vector>

using namespace std;

int main(){
  int t;
  cin >> t;
  for(int xx=1;xx<=t;xx++){
    printf("Case #%d: ",xx);
    set<string> st;
    int cnt=0;
    int n,m;
    cin >> n >> m;
    string dir;
    for(int i=0;i<n;i++){
      cin >> dir;
      st.insert(dir);
    }
    for(int j=0;j<m;j++){
      cin >> dir;
      string s="";
      for(int k=0;k<=dir.length();k++){
	if(k!=0&&(dir[k]=='\0'||dir[k]=='/')){
	  if(st.count(s)==0){
	    cnt++,st.insert(s);
	  }
	}
	s+=dir[k];
      }
    }
    cout << cnt << endl;
  }
  return 0;
}
