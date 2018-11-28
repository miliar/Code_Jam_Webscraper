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
    int N,L,H;
    
    cin>>N>>L>>H;
    
    vector<int> s;
    rep(j,N){
      int temp;
      cin>>temp;
      s.pb(temp);
    }
    
    bool flag=false;
    int res;
    for(int k=L;k<=H;k++){
      bool f=true;
      for(int p=0;p<s.size();p++){
	if(s[p]%k == 0 || k%s[p] ==0){
	  ;
	}else{
	  f=false;
	  break;
	}
      }
      if(f){
	res=k;
	flag=true;
	break;
      }
    }
    if(!flag){
      cout<<"Case #"<<i+1<<": NO"<<endl;
    }else{
      cout<<"Case #"<<i+1<<": "<<res<<endl;
    }
  }
   return 0;
}
