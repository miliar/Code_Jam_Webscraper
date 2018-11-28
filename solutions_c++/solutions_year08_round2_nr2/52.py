#include<iostream>
using namespace std ;
int parent[1000001] ;

bool sieve[10002] ;
int pr,primes[10002] ;
bool solve(int k1,int k2,int p)
{
 if(k1 > k2) swap(k1,k2) ;
 int i,j,ret = 1 ;
 for(i=0;i<pr && primes[i] <= k1;i++)  
  if(k1%primes[i] == 0)
   if(k2%primes[i] == 0)
    ret = primes[i] ;
 return ret >= p?1:0 ;  
}

int get(int k) {return k==parent[k]?k:parent[k]=get(parent[k]) ;}
main()
{
 int i,j,k,runs,a,b,p ;

 for(i=2;i<=10000;i++)
  if(!sieve[i])
  {
   primes[pr++] = i ;
   for(j=i+i;j<=10000;j+=i) sieve[j] = true ;            
  }

 freopen("a.in","r",stdin) ;
 freopen("out.txt","w",stdout) ;
  
 cin >> runs ;
 for(int t=1;t<=runs;t++)
 {
  cin >> a >> b >> p ;
  for(i=a;i<=b;i++) parent[i] = i ;
  
  for(i=a;i<=b;i++)
   for(j=i+1;j<=b;j++)
    if(solve(i,j,p))
    {
     int aa = get(i) ;
     int bb = get(j) ;
     parent[aa] = bb ;             
    }
  
  int ret = 0 ;
  for(i=a;i<=b;i++) if(parent[i] == i) ret ++ ;
  printf("Case #%d: %d\n",t,ret) ;            
 }
}
