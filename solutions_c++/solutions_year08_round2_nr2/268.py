#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<algorithm>
#include<cmath>
#include<queue>
#include<set>
#include<map>

#define x first
#define y second

#define rep(i,n) for(ll i=0;i<ll(n);i++)

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pii;
typedef vector<ll>  vll;

vll p;
vll p2;
vll v;

void prim(int N) {
   v = vll(N+1,0);
   p.push_back(2);
   p2.push_back(4);
   for (ll i = 3; i <=N; i++) {
      if (v[i] == 0) {
         p.push_back(i);
         p2.push_back(i*i);
         for (ll j=i*i; j <= N; j+=2*i) {
            v[j]=1;
         }
      }
   }
}

struct particio{
   vector<ll> p;
   particio(ll n){
       p.resize(n);
       for(int i=0;i<n;i++) p[i]=i;                  
   }
   ll iden(ll x){
       if(p[x]!=x) p[x]=iden(p[x]);
       return p[x];         
   }
   void unir(ll x,ll y){
       p[iden(x)]=y;
   }
};


int main() {
   int N;
   cin >> N;
   prim(1100000);
   for (ll Nc = 1; Nc <= N; Nc++) {
      ll A, B, P;
      cin >> A >> B >> P;
      int start = -1;
      particio Par(B-A+1);
      map<ll,ll> M;
      for (ll i = A; i <= B; i++) {
         ll n = i;
         for (int j = 0; p2[j] <= i; j++) {
            if (n % p[j] == 0) {
               if (p[j] >= P) {
                  if (M.find(p[j])!=M.end()) {
                     if (Par.iden(M[p[j]]-A) != Par.iden(i-A)) {
                        Par.unir(M[p[j]]-A,i-A);
                     }
                  }
                  else {
                     M[p[j]] = i;
                  }               
               }
               while (n%p[j]==0) {
                  n/=p[j];
               }
            }
         }
         if (n != 1 and n>=P) {
            if (M.find(n)!=M.end()) {
               if (Par.iden(M[n]-A) != Par.iden(i-A)) {
                  Par.unir(M[n]-A,i-A);
               }
            }
            else {
               M[n] = i;
            }               
         }
      }
      set<ll> S;
      for (int i = A; i <= B; i++) {
         //cout << i << " " << Par.iden(i-A)+A << endl;
         Par.p[i-A] = Par.iden(i-A);
         S.insert(Par.iden(i-A));
      } 
      cout << "Case #" << Nc << ": " <<  S.size() << endl;
   }
}

