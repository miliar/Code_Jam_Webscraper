#include <iostream>

using namespace std;

int ans;
int data[15];
int n;

void dfs(int s, int p){
  if(p==n){
    bool first=true;
    int a;
    int b=0;
    int c=0;
    for(int i=0;i<p;i++){
      if(s>>i&1){
	if(first){
	  first=false;
	  a=data[i];
	}else{
	  a^=data[i];
	}
	c+=data[i];
      }else{
	b+=data[i];
      }
    }
    if(a==0 || b==0) return;
    //cout << a << ' ' << b << ' ' << c << endl;
    if(a==b){
      if(ans<c) ans=c;
    }
    return;
  }
  dfs(s, p+1);
  s|=1<<p;
  dfs(s, p+1);
}

main(){
  int t;
  cin >> t;
  for(int tc=0;tc<t;tc++){
    cin >> n;
    for(int i=0;i<n;i++){
      cin >> data[i];
    }
    ans=-1;
    dfs(0, 0);
    cout << "Case #" << tc+1 << ": ";
    if(ans==-1) cout << "NO" << endl;
    else cout << ans << endl;
  }
  return 0;
}
