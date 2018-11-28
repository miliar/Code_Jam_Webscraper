#include<iostream>
#include<cstdlib>
#include<algorithm>
#include<vector>
using namespace std;
template <class T> void pp(T &a,int p){for(int i=0;i<p;i++)cout << a[i]<<" ";  cout << endl;}

char m[127][127];

void isclear(vector<pair<char,char> >&ng,vector<char> &in){
  for(int k=0;k<ng.size();k++){
    for(int i=0;i<in.size();i++){
      for(int j=0;j<in.size();j++){
	if (i != j && in[i] == ng[k].first && in[j] == ng[k].second){
	  in.clear();
	  return;
	}
      }
    }
  }
}

main(){
  int te;
  cin>>te;
  for(int tc=1;tc<=te;tc++){
    vector<char> ans;
    fill(&m[0][0],&m[127][0],0);
    int n;
    cin>>n;
    for(int i=0;i<n;i++){char a,b,c;cin>>a>>b>>c;m[a][b]=c;m[b][a]=c;    }
    cin>>n;
    vector<pair<char,char> > ng(n);
    for(int i=0;i<n;i++){
      char a,b;
      cin>>a>>b;
      ng.push_back(make_pair(a,b));
    }
    cin>>n;
    for(int i=0;i<n;i++){
      char a;cin>>a;
      if (ans.size()&&m[a][ans.back()]!=0){
	ans.back()=m[a][ans.back()];
      }else ans.push_back(a);
      isclear(ng,ans);
    }
    cout <<"Case #" << tc << ": ";
    cout <<"[";
    for(int i=0;i<ans.size();i++){
      if (i)cout << ", ";
      cout << ans[i];
    }
    cout <<"]"<<endl;
  }
  return false;
}
