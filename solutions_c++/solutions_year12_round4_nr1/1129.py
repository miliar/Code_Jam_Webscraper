#include<iostream>
#include<string>
#include<algorithm>
#include<stack>
#include<queue>
#include<set>
#include<complex>
#include<map>
#include<list>
#include<deque>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
using namespace std;

int main(){
  int testcase;
  int n,D,d[10010],l[10010];
  int v[10010],ma;
  
  cin >> testcase;
  for(int casenum=1;casenum<=testcase;casenum++){
    cin >> n;
    for(int i=0;i<n;i++){
      cin >> d[i] >> l[i];
      v[i] = 0;
    }
    cin >> D;

    v[0] = d[0];
    ma = 0;
    for(int i=0;i<n;i++){
      if(!v[i])break;
      ma = max(ma,d[i] + v[i]);
      for(int j=i+1;j<n;j++){
	if(d[j]<=d[i] + v[i]){
	  v[j] = max(v[j],min(d[j]-d[i],l[j]));
	}else{
	  break;
	}
      }
    }
 
    cout << "Case #" << casenum << ": ";
    if(D <= ma)cout << "YES" << endl;
    else cout << "NO" << endl;
  }
}
