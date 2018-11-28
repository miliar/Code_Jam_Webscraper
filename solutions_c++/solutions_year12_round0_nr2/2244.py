#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cstdlib>

#define rep(i,n) for(int i=0;i<n;i++)
#define rp(i,n) for(i=0;i<n;i++)
#define pr(i) cout<<i<<endl

using namespace std;

int n,s,p,t[200],r,m;

int main(){

  cin>>m;

  rep(ii,m){
    cin>>n>>s>>p;rep(i,n)cin>>t[i];
    r=0;sort(t,t+n,greater<int>());
    rep(i,n){
      if(t[i]%3==0){
	if(t[i]/3>=p){r++;continue;}
	if(t[i]/3+1>=p&&t[i]/3+1<=10&&t[i]/3-1>=0&&s>0){
	  s--;r++;
	}
      }
      else if(t[i]%3==1){
	if(t[i]/3+1>=p)r++;
      }
      else {
	if(t[i]/3+1>=p){r++;continue;}
	if(t[i]/3+2>=p&&t[i]/3+2<=10&&s>0){
	  r++;s--;
	}
      }
    }
    cout<<"Case #"<<ii+1<<": "<<r<<endl;

  }
  return 0;

}
