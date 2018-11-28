#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
using namespace std;

typedef long long int64;

int64 power(int64 x,int64 k,int64 p) {
  int r=1;
  while (k) {
    if (k&1)
      r=((int64)r*x)%p;
    k>>=1;
    x=((int64)x*x)%p;
  }
  return r;
}

int64 alfa,beta;

int64 gcd(int64 a,int64 b) {
  if (!b) {
    alfa=1;
    beta=0;
    return a;
  }
  int64 d=gcd(b,a%b),z=beta;
  //alfa*b+(a-a/b*b)*beta=beta*a+(alfa-a/b*beta)*b
  beta=alfa-a/b*beta;
  alfa=z;
  return d;
}

int64 inverse(int64 a,int64 n) {
  gcd(a,n);
  return (n+alfa%n)%n;
}

#define ALL(t) t.begin(),t.end()
#define FOR(i,n) for (int i=0;i<(int)(n);i++)
#define FOREACH(i,t) for (typeof(t.begin())i=t.begin();i!=t.end();i++)
typedef vector<int> vi;
typedef long long int64;

#define INF 1000000000
int64 r,K,a[110];
#define MAX 1100000
bool p[MAX];
void update(int64 cur){
  if(r==-1)r=cur;
  else if(r>=0&&r!=cur)r=-2;  
}
void check(int64 p,int64 A){
//  cout<<"check "<<p<<" "<<A<<endl;
  int64 B=((a[1]-A*a[0])%p+p)%p,cur=a[0];
  FOR(i,K-1){
    cur=(A*cur+B)%p;
    if(cur!=a[i+1])return; 
  }
  cur=(A*cur+B)%p;
  update(cur);
}
main(){
  for(int i=2;i<MAX;i++)p[i]=1;
  for(int i=2;i<MAX;i++)if(p[i])for(int j=2*i;j<MAX;j+=i)p[j]=0;
  int C,D;cin>>C;
  for(int c=1;c<=C;c++){
    r=-1;
    cin>>D>>K;
//    memset(a,0,sizeof(a));
    FOR(i,K)cin>>a[i];
    int m=1;
    while(D--)m*=10;
    assert(m<MAX);
//    if(K==1)cout<<D<<" "<<a[0]<<endl;
//    cout<<m<<endl;
    if(K>1)for(int k=2;k<=m;k++)if(p[k]){
      int pos=0;
      FOR(i,K)if(a[i]>=k)goto fail;
      while(pos+2<K&&a[pos]==a[pos+1])pos++;
      if(pos+2<K){
        int64 A=(int64)(a[pos+1]+k-a[pos+2])*inverse(a[pos]+k-a[pos+1],k)%k;
        check(k,A);
      }else if(K==2){
        if(a[0]==a[1])update(a[0]);else r=-2;
      }else{
        FOR(i,K)if(a[i]!=a[0]){
          puts("dupa");
          return 1;
          goto fail;
        }
//        cout<<"update "<<a[0]<<endl;
        update(a[0]); 
      }
fail:;
    }
    cout<<"Case #"<<c<<": ";
    if(r<0)cout<<"I don't know."<<endl;
    else cout<<r<<endl;
  }
}
