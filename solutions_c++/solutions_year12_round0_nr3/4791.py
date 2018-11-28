#include<iostream>
#include<cstdio>

using namespace std;

bool valid(int j,int k) {
  int v[20];
  int n = 0;
  int o = j;
  while(j) {
    v[n] = j%10;
    j/=10;
    n++;
  }
  int st = -1;
  for(int i = 0;i<n;i++) {
    if(k%10==v[i]) {
      st = i;
  
      if(st==-1) continue;
      int l = 0;
      bool ok = true;
      int o = k;
      for(int s = st;k && l<n;l++,s = (s+1)%n) {
        if(k%10 != v[s]) {
          ok = false;
          break;
        }
        k/=10;
      }
      if(l!=n || k) {
        k = o;
        continue;
      }
      k = o;
      if(ok)
        return true;
    }
  }
  return false;
}

int main() {
  freopen("C-small-attempt0.in","r",stdin);
  freopen("p3.out","w",stdout);
  int T;
  cin>>T;
  for(int i=0;i<T;i++) {
    int A,B;
    cin>>A>>B;
    int cnt = 0;
    for(int j=A;j<B;j++) {
      for(int k=j+1;k<=B;k++) {
        if(valid(j,k)) {
          cnt++;
        }
      }
    }
    cout<<"Case #"<<(i+1)<<": "<<cnt<<"\n";
  }
  return 0;
}
