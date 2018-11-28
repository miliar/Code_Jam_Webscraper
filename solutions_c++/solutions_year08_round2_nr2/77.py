#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;

bool isprime[1000001];

bool _isprime(int n){
  if(n<=1) return false;
  for(int i=2; i*i<=n; i++){
    if(n%i==0) return false;
  }
  return true;
}

void mkprime(){
  for(int i=0; i<=1000000; i++){
    isprime[i]=_isprime(i);
  }
}

int solve(ll A, int len, ll P){
  if(P>len) P=len;
  vector<int> uft(len);
  //vector<int> cnt(len);
  for(int i=0; i<len; i++){
    uft[i]=i;
    //cnt[i]=1;
  }
  for(; P<len; P++){
    if(!isprime[P]) continue;
  //cout<<P<<":"<<endl;
    ll st=(A+P-1)/P *P - A;
    if(st>=len) continue;
    for(int i=st+P; i<len; i+=P){
      int a=st;
      int b=i;
  //cout<<a<<" "<<b<<endl;
      vector<int> path;
      while(uft[a]!=a){
	path.push_back(a);
	a=uft[a];
      }
      while(uft[b]!=b){
	path.push_back(b);
	b=uft[b];
      }
      /*
      if(cnt[a]<cnt[b]){
	int t=a;
	a=b;
	b=t;
      }
      cnt[a]+=cnt[b];
      */
      uft[b]=a;
      for(int i=0; i<path.size(); i++){
	uft[path[i]] = a;
      }
    }
  }
  int res=0;
  for(int i=0; i<len; i++){
    if(uft[i]==i) res++;
    //cout<<uft[i]<<endl;
  }
  return res;
}

int main(){
  int C;
  cin>>C;
  mkprime();
  for(int c=1; c<=C; c++){
    ll A,B,P;
    cin>>A>>B>>P;
    cout<<"Case #"<<c<<": "<<solve(A,B-A+1,P)<<endl;
  }
  return 0;
}

