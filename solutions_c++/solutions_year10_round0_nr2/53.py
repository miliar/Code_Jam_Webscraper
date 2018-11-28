#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <map>
#include <cstdio>
#include <queue>
#define vec vector<long long>
#define mod 100000
#define ll long long
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define f(i,x,y) for(int i=x;i<y;i++)
#define fd(i,y,x) for(int i=y;i>=x;i--)

using namespace std;

vec A[1000];
void impr(vec C){
   printf("%lld",C.back());
   for(int i=C.size()-2;i>=0;i--) printf("%05lld",C[i]);
   printf("\n");
}

vec operator*(vec a,vec b){
   int m=a.size(),n=b.size();
   vec c(m+n); 
   ll s=0;
   f(i,0,m+n){
      int ini=max(0,i-n+1);
      int fin=min(i+1,m);
      f(j,ini,fin)s+=a[j]*b[i-j];
      int k=i;
      while(s){
         c[k]+=s%mod; s=s/mod;
         if(c[k]>=mod){ c[k]-=mod; c[k+1]++;}
         k++;
      }
   }
   if(c.back()==0)c.pop_back();
   return c;
}
vec operator+ (vec a,vec b){
   int m=a.size(),n=b.size();
   if(m<n) swap(a,b), swap(m,n);
   vec c(m+1); 
   f(i,0,m){
      ll s=a[i];
      if(i<n)s+=b[i];
      if(c[i]+s>=mod) c[i+1]++, s-=mod;
      c[i]+=s;
   }
   if(c.back()==0)c.pop_back();
   return c;
}
vec operator- (vec a,vec b){
   int m=a.size(), n=b.size();
   vec c(m);
   f(i,0,m){
      ll r=a[i];
      if(i<n) r-=b[i];
      if(c[i]+r<0) c[i+1]--, r+=mod;
      c[i]+=r;
   }

   while(c.size()>1 && c.back()==0)c.pop_back();
   //cout<<"y ahora "; impr(c);
   return c;
}
int comp(vec A,vec B){
   int m=A.size(), n=B.size();
   if(m<n) return -1;
   if(m>n) return 1;
   fd(i,m-1,0){
      if(A[i]<B[i])return -1;
      if(A[i]>B[i])return 1;
   }
   return 0;
}
pair<vec,vec> div (vec A, vec B){
   int m=A.size(), n=B.size();
   if(comp(A,B)<0)return make_pair(vec(1,0),A);
   vec a(A); vec b(B);
   vec d(n+1); fd(i,n-1,0) d[i]=a[i+m-n];
   vec c(m-n+1);
   fd(i,m-n,0){
      ll cand=(d[n]*mod+d[n-1]) /b.back();
      if(d.back()==0 &&d.size()>1) d.pop_back();
      if(cand>=mod) cand=mod-1;
      vec q(1,cand ); //cout<<q[0]<<endl;
      while(comp(q*b, d) >0 && q[0]>0 ) q[0]--;
      c[i]=q[0];  //cout<<"q0="<<q[0]<<endl<<endl;
      //cout<<"d es";impr(d); impr(q*b); cout<<endl;
      d=d-q*b;  //cout<<"la resta es"; impr(d);
      if(i){
         if(d.size()==n+1) d.pop_back();
         d.insert(d.begin(),a[i-1]);
      }     
      //cout<<"residuo:";impr(d); 
   }
   pair<vec,vec> res;
   res.first=c; res.second=d;
   return res;
}
vec gcd(vec a,vec b){
   //impr(a),impr(b); cout<<endl;
   if(b.back()==0) return a;
   if(a.back()==0) return b;
   pair<vec,vec> x=div(a,b);
   return gcd(b,x.second);
}
bool op(vec A,vec B){
   //impr(A); cout<<" <"<<endl; impr(B);
   return comp(A,B)<0;
}
void leer(vec &A){
   string cad; cin>>cad;
   int n=cad.size();
   int r=n%5;
   if(r) cad=string(5-r,'0')+cad, n+=5-r;
   reverse(all(cad)); 
   int k=0;
   while(k+5<=n){
      string ss=cad.substr(k,5); 
      while(ss.size() && ss[ss.size()-1]==0) ss.erase(ss.end()-1);
      reverse(all(ss));
      
      istringstream iss(ss);
      ll m;
      iss>>m;
      A.push_back(m);
      k+=5;
   }
}
int main(){
   int T,n;
   cin>>T;
   f(t,1,T+1){
      f(i,0,1000) A[i].clear();
      cin>>n;
      f(i,0,n) leer(A[i]);
      //f(i,0,n) cin>>A[i];
      sort(A,A+n,op);
      //f(i,0,n) impr(A[i]);
      vec d=A[1]-A[0]; 
      f(i,1,n-1){
         d=gcd(d,A[i+1]-A[i]); //cout<<"d=";impr(d);
      }
      //impr(d);
      pair<vec,vec> x=div(A[0],d);
      vec r=x.second; vec res; //impr(r);
      if(r.back()==0)res=vec(1,0);
      else res=d-r;
      cout<<"Case #"<<t<<": ";
      impr(res);
      vec v1(2); v1[0]=42881; v1[1]=1;
      vec v2(1,2946);
      x=div(v1,v2);
      //impr(x.first);impr(x.second);
   }
}
