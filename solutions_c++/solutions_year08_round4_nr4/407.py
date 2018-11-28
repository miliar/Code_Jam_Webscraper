#include<algorithm>
#include<vector>
#include<iostream>
#include<string>

using namespace std;

int main(){
  int Q;
  cin >>Q;
  for(int q=1;q<=Q;q++){
    int k;
    string s;
    cin >> k >> s;
    vector<int> perm;
    for(int i=0;i<k;i++){
      perm.push_back(i);
    }
    int mini = s.size();
    do{
      string w = s;
      int ind = 0;
      while(ind<s.size()){
	for(int i=0;i<perm.size();i++){
	  w[i+ind]=s[ind+perm[i]];
	}
	ind += k;
      };
      int cs = 1;
      for(int i=1;i<w.size();i++){
	if(w[i]!=w[i-1]){cs++;}
      }
      mini = min(cs,mini);
    }while(next_permutation(perm.begin(),perm.end()));
    cout<<"Case #"<<q<<": "<<mini<<endl;
  }
  return 0;
}
