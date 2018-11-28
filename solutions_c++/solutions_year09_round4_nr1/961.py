#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<map>
#include<utility>
#include<set>
#include<string>
#include<cstring>
#include<vector>
#include<sstream>
#include<complex>
#include<queue>
#include<stack>
#include<functional>
#include<algorithm>

using namespace std;

#define PB push_back
const double EPS = 1e-8;
typedef long long ll;


int main()
{
  vector<string> tab;
  vector<string> tabs;
  int t;
  cin>>t;

  for(int id = 1; id<=t; id++){
    tab.clear();
    tabs.clear();
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
      string tmp;
      cin>>tmp;
      tab.PB(tmp);
    }

    int ans = 0;

    for(int i=0;i<n-1;i++){
      bool flg = true;
      for(int k=i+1;k<n;k++){
	if( tab[i][k]=='1'){
	  flg=false;
	}
      }
      if(flg) continue;
      for(int j=i+1;j<n;j++){
	bool f = true;
	for(int k=i+1;k<n;k++){
	  if(tab[j][k]=='1'){
	    f=false;
	  }
	}
	if(f){
	  for(int k=j;k>i;k--){
	    swap(tab[k],tab[k-1]);
	    ans++;
	  }
	  break;
	}
      }
    }
    cout<<"Case #"<<id<<": "<<ans<<endl;

  }
  return 0;
}
