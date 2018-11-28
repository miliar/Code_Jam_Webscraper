#include <iostream>
#include <queue>
using namespace std;
long long l,t,n,c,a[1005],tt;
priority_queue<long long > q;
int main(){
  cin >> tt;
  long long ans,tp;
  for (long long kk = 1; kk<=tt;++kk){
    cout <<"Case #"<<kk<<": ";
    cin >> l >> t >> n >> c;
    for (int i = 0; i < c; ++ i)
      cin >> a[i];
    ans = 0;
    tp = 0;
    int i;
    while (!q.empty())
      q.pop();
    //    cout << l << " " << t <<" " << n << " " << c << " ";
    for (i = 0; i <n;++i){
      ans += 2*a[i%c];
      tp+=a[i%c]*2;
      if (tp>=t){
	if (tp-t>0){
	  q.push((tp-t)/2);
	  ans-=(tp-t);
	}
	for (int j = i+1; j<n;++j){
	  q.push(a[j%c]);
	}
	break;
      }      
    }
    while (l>0 && q.size()>0){
      ans += q.top();
      //      cout <<"ans = "<< ans << " q.top() = " << q.top()<<" ";
      q.pop();
      l--;
    }
    while (q.size()>0){
      ans+=q.top()*2;
      //      cout <<"ans = "<< ans << " q.top() = " << q.top()<<" ";
      q.pop();
    }
    cout << ans <<endl;
  }  
}
