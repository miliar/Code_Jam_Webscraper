#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
using namespace std;
#define REP(i,b,n) for(int i=b;i<n;i++)
#define rep(i,n)   REP(i,0,n)
typedef long long ll;


main(){
  int te;
  int tc=1;
  cin>>te;
  while(te--){
    string a;
    cin>>a;
    set<char>S;
    vector<int > tmp;
    rep(i,a.size())S.insert(a[i]);
    ll base = S.size();
    if ( S.size() == 1)base=2;
    
    map<char,int>M;    
    int assigned[100]={0};
    rep(i,a.size()){
      if ( M.find(a[i]) != M.end()){tmp.push_back(M[a[i]]);continue;}
      rep(j,base){
	if ( assigned[j] == 1)continue;
	if (i == 0 && j == 0)continue;
	else {
	  M[a[i]]=j;
	  tmp.push_back(j);
	  assigned[j]=1;
	  break;
	}
      }
    }

   
    reverse(tmp.begin(),tmp.end());
    ll ans =0,mul=1;
   
    rep(i,tmp.size()){
      ans+= tmp[i]*mul;
      mul*=base;
    }
    cout << "Case #"<<tc++ << ": "<< ans <<endl;
  }
  return false;
}
