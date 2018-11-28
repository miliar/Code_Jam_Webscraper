#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
using namespace std ;
#define MAXN 1002
int n,R,K,in[MAXN],id[MAXN],next[MAXN] ;
long long sum[MAXN],profit[MAXN] ;

int brute()
{
 int i,j,ret = 0,current = 0 ;

 for(i=0;i<n;i++)
 {
  int sm = 0 ;
  for(j=i;;j=(j+1)%n)
  {
   sm += in[j] ;
   if(sm > K) break ;
  }
  next[i] = j ;
  profit[i] = sm - in[j] ;
 }

 long long total = 0 ;
 for(i=0;i<n;i++) total += in[i] ;
 if(total <= K) return total*R ;

 for(i=1;i<=R;i++)
 {
  int nxt = next[current] ;
  ret += profit[current] ;
  current = nxt ;
 }
 return ret ;
}

void generate()
{
 int i,j,k ;
 n = rand()%50 + 2 ;
 R = rand()%1000 + 1 ;
 K = rand()%1000 + 1 ;
 for(i=0;i<n;i++) in[i] = rand()%K + 1 ;
}


long long solve()
{
 int i,j,k ;
 long long total = 0 ;
 for(i=0;i<n;i++) total += in[i] ;
 if(total <= K) return total*R ;
 for(i=0;i<n;i++)
 {
  long long sm = 0 ;
  for(j=i;;j=(j+1)%n)
  {
   sm += in[j] ;
   if(sm > K) break ;
  }
  next[i] = j ;
  profit[i] = sm - in[j] ;
//  cout << i << " " << next[i] << " " << profit[i] << endl ;
 }
 memset(sum,0,sizeof sum) ;
 memset(id,255,sizeof id) ;
  
 id[0] = 0 ;
 long long ret = 0 ;
 int current = 0 ;
 for(i=1;i<=R;i++)
 {
  int nxt = next[current] ;
  if(id[nxt] == -1)
  {
   ret += profit[current] ;
   sum[nxt] = ret ;
   id[current = nxt] = i ;
  }
  else
  {
   ret += profit[current] ;
   int rides = R - i ;
   int cycle = i - id[nxt] ;
   ret += (ret - sum[nxt])*(rides/cycle) ;
//   cout << R << " " << i << " " << rides << " " << cycle << " " << ret << " " << sum[nxt] << " " << current << " " << nxt << endl ;
   R -= (rides/cycle)*cycle ;
   current = nxt ;
  }
 }
 return ret ;
}


void test()
{
 int i,j,runs = 1000 ;
 for(i=0;i<runs;i++)
 {
  generate() ;
  int ret2 = brute() ;
  int ret1 = solve() ;
  if(ret1 != ret2) 
  { 
   cout << "failed on case " << i << endl ; 
   cout << R << " " << K << " " << n << endl ;
   for(j=0;j<n;j++) cout << in[j] << " " ; cout << endl ;
   cout << ret1 << " " << ret2 << endl ;
   while(1) ; 
  }
 }
 cout << "done" << endl ;
}

main()
{
// test() ; return 0 ;
 int i,j,k,runs ;
 scanf("%d",&runs) ;
 for(int t=1;t<=runs;t++)
 {
  scanf("%d%d%d",&R,&K,&n) ;
  for(i=0;i<n;i++) scanf("%d",&in[i]) ;
  long long ret = solve() ;
  printf("Case #%d: %lld\n",t,ret) ;
 }
}
