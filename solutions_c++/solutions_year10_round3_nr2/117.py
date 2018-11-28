#include<iostream>
#include<set>
#include<map>
#include<string>
#include<stdio.h>
#include<sstream>
#include<algorithm>
#include<sstream>
#include<queue>
#include<string.h>
using namespace std ;
#define INF 50
char tab[11][1002][1002] ;

void pre()
{
 int i,j,k,t,ii ;
 for(t=2;t<=10;t++)
 {
  for(k=1;k<=1000;k++)
   for(i=1;i+k-1<=1000;i++)
   {
    j = i + k - 1 ;
    if(i*t >= j) continue ;
    int ret = INF ;
    for(ii=i+1;ii<j;ii++) ret = min(ret,1 + max(tab[t][i][ii],tab[t][ii][j])) ;
    tab[t][i][j] = ret ;
   }
 }
}


int C,sz,a[100] ;
int memo[102][102] ;
int solve(int l,int h)
{
 if(1LL*a[l]*C >= a[h]) return 0 ;
 if(memo[l][h] != -1) return memo[l][h] ;
 int ret = INF ;
 for(int i=l+1;i<h;i++) ret = min(ret,1 + max(solve(l,i),solve(i,h))) ;
 return memo[l][h] = ret ;
}

int Solve(long long l,long long h,int t)
{
 int i,j,k ;
 sz = 0 ; C = t ;
 
 long long L = l,H = h ;
 while(L <= H) { a[sz++] = L ; L *= C ; }
 L = l,H = h ;
 while(H >= L) { a[sz++] = H ; H /= C ; }
 sort(a,a+sz) ;
 
 int Sz = 1 ;
 for(i=1;i<sz;i++) if(a[i] != a[i-1]) a[Sz++] = a[i] ;
 sz = Sz ;

 memset(memo,255,sizeof memo) ;
 int ret = solve(0,sz-1) ;
 return ret ;
}

main()
{
 int i,j,k,l,h,runs ;

/* 
 pre() ;
 cout << "done" << endl ;

 for(i=0;i<1000000;i++)
 {
  k = rand()%9 + 2 ;
  l = rand()%1000 + 1 ;
  h = l + rand()%1000 ;
  if(h > 1000 || l >= h) { i -- ; continue ; }

  int ret1 = tab[k][l][h] ;
  int ret2 = Solve(l,h,k) ;
//  cout << ret1 << " " << ret2 << endl ;
  if(ret1 != ret2) cout << k << " " << l << " " << h << endl ;
 }
 cout << "tested" << endl ;
*/

 int test = 1 ;
 cin >> runs ;
 while(1)
 {
  cin >> l >> h >> k ;
//  int ret = tab[k][l][h] ;
  int ret = Solve(l,h,k) ;
  printf("Case #%d: %d\n",test,ret) ;
  test ++ ;
  if(test > runs) break ;
 }
}
