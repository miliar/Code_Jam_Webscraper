#include <numeric>
#include <functional>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <climits>
#include <cmath>
#include <cctype>
#include <sstream>
#include <map>
#include <set>
#include <cstdio>
#include <queue>
using namespace std;
typedef long long ll;
int d;
ll mod;

ll modpow(ll a, ll b){
    if(b == 0) return 1;
    ll c = modpow(a, b / 2);
    c = (c * c) % mod;
    if(b % 2 == 1) c = (c * a) % mod;
    return c;
}

ll modinverse(ll a){
    ll res = modpow(a, mod - 2);    
    return res;
}
ll LIM = 1000000;
int pr[1000010], p[100010];
int dd[7];
ll a[10];
int cnt;
void make_criba(){
   dd[0]=1;
   cnt=0;
   for(ll i = 1; i < 7; i++) dd[i]=10*dd[i-1];
   for(ll i = 0; i < LIM; i++) pr[i]=1;
   pr[0]=pr[1]=0;
   for(ll i = 2; i < LIM; i++) if(pr[i])
   {
      p[cnt] = i; cnt++;
      for(ll j= i + i ; j <= LIM; j += i) pr[j]=0;
   }
 }

int main()
{
   make_criba();
   int tt;
   cin>>tt;
   for(int t = 1; t <= tt; t++){
      int k;
      cin>>d>>k;
      for(int i = 0; i < k; i++) cin>>a[k - 1 - i];
      
      printf("Case #%d: ", t);
      if(k == 1){
         cout<<"I don't know."<<endl;
         continue;
      }
      if(k==2){
         cout<<"I don't know."<<endl;
         continue;
      }
      
      if(a[0]==a[1]){
         printf("%lld\n",a[0]);
         continue;
      }
      
      int *it = upper_bound(p,p+cnt,*max_element(a, a+k) );
      vector<int> A;

      while(it<p+cnt){
         if(*it > dd[d]) break;
         bool sirve = true;
         for(int i = 0; i < k - 3; i++){
            if( ((a[i+2]-a[i+1])*(a[i+2]-a[i+1])-(a[i+1]-a[i])*(a[i+3]-a[i+2]) )%(*it)){
            	sirve = false;
               break;
              }
         }
         if(!sirve){it++; continue;}
         if((a[0]-a[1]) % (*it)==0) continue;
         mod = *it;
         ll auxy, y = modinverse(a[1]-a[2]); 
         auxy=y;
         auxy *= a[0]-a[1]; 
         auxy %= mod;
         auxy *= a[0]-a[1]; 
         auxy %= mod;
         auxy += a[0];
         auxy %= mod;
         if(auxy < 0) auxy += mod;
         A.push_back(auxy);
         if(A.size() >= 2) break;

         it++;
      }
      if(A.size()>1){ 
         if(A[0]!=A[1]) 
         cout<<"I don't know."<<endl;
         else printf("%d\n",A[0]);
      }
      else printf("%d\n",A[0]);
   }
}
