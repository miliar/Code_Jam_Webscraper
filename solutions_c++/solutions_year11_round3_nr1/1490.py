   #include <algorithm>
    #include <cctype>
    #include <cmath>
    #include <cstdio>
    #include <cstdlib>
    #include <ctime>
    #include <functional>
    #include <numeric>
    #include <utility>
     
    #include <deque>
    #include <stack>
    #include <bitset>
    #include <map>
    #include <set>
    #include <string>
    #include <cstring>
    #include <vector>
    #include <queue>
    #include <list>
     
    #include <sstream>
    #include <iostream>
    #include <iomanip>
     
    using namespace std;

    #define pb push_back
    #define mp make_pair

    #define REP(i,b,n) for(int i=b;i<n;i++)
    #define rep(i,n)   REP(i,0,n)

int main(){
  
  int T;
  cin>>T;

  rep(i,T){
    int n,m;
    cin>>n>>m;
    
    vector<string> tile;
    rep(j,n){
      string str;
      cin>>str;
      tile.pb(str);
    }
    bool f=true;

    /*    rep(j,n){
      cout<<tile[j]<<endl;
      }*/

    rep(k,n){
      rep(l,m){
	if(tile[k][l]=='#'){
	  //	  cout<<"test"<<endl;
	  if(l+1<m && k+1 < n && tile[k][l+1]=='#' && tile[k+1][l]=='#' && tile[k+1][l+1] =='#'){
	    tile[k][l]='/';
	    tile[k][l+1]='\\';
	    tile[k+1][l]='\\';
	    tile[k+1][l+1]='/';
	  }else{
	    f=false;
	    break;
	  }
	}
      }
      if(!f)
	break;
    }

    if(!f){
      cout<<"Case #"<<i+1<<":"<<endl;
      cout<<"Impossible"<<endl;
    }else{
      cout<<"Case #"<<i+1<<":"<<endl;
      rep(j,n){
	cout<<tile[j]<<endl;
      }
    }

  }
  
   return 0;
}
