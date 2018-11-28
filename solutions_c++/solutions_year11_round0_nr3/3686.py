#include<iostream>
#include<cstdio>
using namespace std;

#define loop(i,n) for(i=1; i<=n; i++)

int T,N,i,x,m,s;

int main ()
{
  freopen("C-large.in","r",stdin);
  freopen("output.txt","w",stdout);
  cin >> T; int n,i,t;
  loop(t, T) {
    x=0; s=0; m=1000000; cin >> N; loop(n,N) {
      cin >> i; x=x xor i; s=s+i; if(i<m) { m=i; }
    }
    cout << "Case #" << t << ": ";
    if(x!=0) { cout << "NO" << endl; } else {  cout << s-m << endl; }
  }
  return 0;
}