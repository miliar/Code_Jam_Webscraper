#include <iostream>
#include <vector>
using namespace std;

int main() {
  int t, r;
  cin>>t;
  
  for(r=0;r<t;r++) {
    int n, s, p, i;
    int ans=0, diff=0;
    cin>>n>>s>>p;
    
    
    vector<int> g(n);
    vector<int> avg(n);
    
    for(i=0;i<n;i++) {
      cin>>g[i];
      avg[i] = (g[i]);
      avg[i]/=3;
    }
    
    
    if(p==0) {
      cout<<"Case #"<<r+1<<": "<<n<<endl;
      continue;
    }
    
    for(i=0;i<n;i++) {
      if(g[i]==0) {
	continue;
      }
      
      if(g[i]%3==0) {
	if((avg[i]-p)>=0) {
	  ans++;
	}
	else if((p-avg[i])==1 && s>0)  {
	  s--;
	  diff++;
	  ans++;
	}
      }
      
      else if(g[i]%3==1) {
	if(((avg[i]+1)-p)>=0) {
	  ans++;
	}
      }
      
      else if(g[i]%3==2) {
	if(((avg[i]+1)-p)>=0){
	  ans++;
	}
	else if((p-avg[i])==2 && s>0) {
	  s--;
	  diff++;
	  ans++;
	}
      }
    }
    
    cout<<"Case #"<<r+1<<": "<<ans<<" "<<endl;
  }
  return 0;
}