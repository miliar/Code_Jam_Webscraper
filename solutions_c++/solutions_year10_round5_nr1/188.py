#include<iostream>
#include<set>
#include<map>
#include<string>
#include<stdio.h>
#include<sstream>
#include<algorithm>
#include<sstream>
#include<queue>
#include<cmath>
#include<cassert>
using namespace std ;
#define INF (int)1e9
typedef pair<long long,long long> P ;

pair<int,P> euclid(int a,int b)
{
 if(b == 0) return make_pair(a,P(1,0)) ;
 pair<int,P> temp = euclid(b,a%b) ;
 return make_pair(temp.first,P(temp.second.second,temp.second.first - (a/b)*temp.second.second)) ;            
}

int solve(int a,int b,int n)
{
 pair<int,P> temp = euclid(a,n) ;
 if(b%temp.first == 0)
  return (1LL*temp.second.first*(b/temp.first) + n*1000000000LL)%n ;
 return -1 ;
}


int D,K,a[20] ;
bool prime[1000002] ;
int brute(int a0,int a1,int upper)
{
 int i,j,k ;
 set<int> s ;
 for(i=2;i<=upper;i++) if(prime[i]) if(i > a1)
  for(j=0;j < upper;j++)
  {
   int b = (a1 - 1LL*j*a0 + 1000000000000LL*i)%i ;
   s.insert((1LL*j*a1 + b)%i) ;
   if(s.size() > 1) return -1 ;
  }
 if(s.size() == 0) return -2 ;
 return *s.begin();
}

main()
{
 int i,j,k,runs ;
 
 for(i=2;i<1000002;i++) prime[i] = true ;
 for(i=2;i<1000002;i++) if(prime[i])
  for(j=i+i;j<1000002;j+=i)
   prime[j] = false ;
 
 scanf("%d",&runs) ;
 for(int t=1;t<=runs;t++)
 {
  set<int> valid ;
  scanf("%d%d",&D,&K) ;
  for(i=0;i<K;i++) scanf("%d",&a[i]) ;
  
//  if(t == 9) { cout << D << " " << K << endl ; for(i=0;i<K;i++) cout << a[i] << " " ; cout << endl ; }
  
  int upper = 1 ;
  for(i=0;i<D;i++) upper *= 10 ;
  
  if(K == 1) { printf("Case #%d: I don't know.\n",t) ; continue ; }
  if(a[K-1] == a[K-2]) { printf("Case #%d: %d\n",t,a[K-1]) ; continue ; }
  if(K == 2) 
  {
   int tp = brute(a[0],a[1],upper) ;
   if(tp != -1) { printf("Case #%d: %d\n",t,tp) ; }
   else printf("Case #%d: I don't know.\n",t) ; 
   continue ; 
  }
  for(i=1;i<K;i++) assert(a[i] != a[i-1]) ;
  
  int mx = 0 ;
  for(i=0;i<K;i++) mx = max(mx,a[i]) ;
  for(i=2;i<=upper;i++) if(prime[i]) if(i > mx)
  {
   int bb = (a[2] - a[1] + 1000000000000LL*i)%i ;
   int aa = (a[1] - a[0] + 1000000000000LL*i)%i ;
   int A = solve(aa,bb,i) ;
   int B = (a[1] - 1LL*A*a[0] + 1000000000000LL*i)%i ;
   if((1LL*A*a[0] + B)%i != a[1]) continue ;
//   if(i == 11) cout << A << " " << B << endl ;
//   cout << i << " " << A << " " << B << endl ;
   
   int S = a[0] ;
   for(j=1;j<K;j++)
   {
    S = (1LL*A*S + B)%i ;
    if(S != a[j]) break ;
   }
   if(j == K) valid.insert((1LL*A*S + B)%i) ;
  }
//  for(set<int> :: iterator it = valid.begin(); it != valid.end();++it) cout << *it << " " ; cout << endl ;
  if(valid.size() == 1) printf("Case #%d: %d\n",t,*valid.begin()) ;
  else if(valid.size() > 1) printf("Case #%d: I don't know.\n",t) ;  
  else printf("Case #%d: Failed !\n",t) ;
 }
}
