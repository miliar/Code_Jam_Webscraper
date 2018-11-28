#include<iostream>
#include<iomanip>
#include<algorithm>
#include<vector>
#include<cstring>
#include<cstdio>
#include<cmath>

using namespace std;

#define FOR(i,a,b) for(int i = a ; i < b ; ++i)

int A, B, n, m, p, ans, arr[20], tp;

int main(){
  
  int T;
  
  cin>>T;
  FOR(j,0,T){
    cin>>A>>B;
    ans = 0;
    FOR(n,A,B){
      p = 1;
      for(int t = n ; t ; p *= 10, t /= 10);
      tp = 0;
      for(int t = 10 ; t < p ; t *= 10){
	m = n%t*(p/t) + n/t;
	if((n < m)&&(m <= B)){
	  arr[tp++] = m;
//	  cout<<n<<" "<<m<<endl;
	}
      }
      sort(arr, arr+tp);
      if(tp)
	++ans;
      FOR(i,1,tp)
	if(arr[i] != arr[i-1])
	  ++ans;
    }
    printf("Case #%d: %d\n", j+1, ans);
  }
  
  return 0;
  
}