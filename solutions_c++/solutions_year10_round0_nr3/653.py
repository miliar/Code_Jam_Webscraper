#include<iostream>
using namespace std;
int main(void){ 
  long long t,r,k,n,g[1005],next[1005],val[1005],sum,visit[1005];
  long long ans, len, ssum, head, asum;
  int count = 1;
  for(cin>>t;t>0;--t){
    cin>>r>>k>>n;
    asum = 0;
    for(int i=0;i<n;++i){
      cin>>g[i];
      asum += g[i];
      visit[i] = -1;
    }
    sum = g[0];
    for(int i=0,j=1;i<n;++i){
      if(j==n) j=0;
      while(sum < asum && sum + g[j] <= k){
        sum += g[j++];
        if(j>=n) j=0;
      }
      next[i] = j;
      val[i] = sum;
      sum -= g[i];
    }
    len=0; 
    int now = 0;
    while(1){      
      visit[now] = len;
      now = next[now];

      len++;
      if(visit[now] >= 0){
        len = len - visit[now];
        head = now;
        break;
      }
    }
    now = head;
    ssum=0;
    while(1){
      ssum += val[now];
      now = next[now];
      if(now == head)
        break;
    }
    ans = 0;
    for(int j=0;j!=head && r>0;--r){
      ans += val[j];
      j = next[j];
    }
    if(r >= len){
      ans += (r/len) * ssum;
      r %= len;
    }
    for(int i=0,j=head;i<r;++i){
      ans += val[j];
      j = next[j];
    }
    cout<<"Case #"<<count++<<": "<<ans<<endl;
  }
  return 0;
}
