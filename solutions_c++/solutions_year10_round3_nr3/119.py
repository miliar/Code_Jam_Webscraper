#include<iostream>
#include<set>
#include<cassert>
#include<map>
#include<string>
#include<stdio.h>
#include<sstream>
#include<algorithm>
#include<sstream>
#include<queue>
#include<string.h>
using namespace std ;
int n,m,g[32][32] ;

bool over()
{
 for(int i=0;i<n;i++)
  for(int j=0;j<m;j++)
   if(g[i][j] != -1)
    return false ;
 return true ;
}

int ct[50] ;
bool proper[50][50][50] ;
int row[50][50],col[50][50] ;
bool solve()
{
 int i,j,k,ii,jj ;
 if(over()) return false ;
 
 memset(row,0,sizeof row) ;
 memset(col,0,sizeof col) ;
 for(i=0;i<n;i++)
  for(j=0;j<m;j++) if(g[i][j] != -1)
  {
   for(k=i+1;k<n;k++) if(g[k][j] == -1 || g[k][j] != 1 - g[k-1][j]) break ;
   row[i][j] = k - i ;
   for(k=j+1;k<m;k++) if(g[i][k] == -1 || g[i][k] != 1 - g[i][k-1]) break ;
   col[i][j] = k - j ;   
  }
 
 memset(proper,false,sizeof proper) ;
 for(i=0;i<n;i++)
  for(j=0;j<m;j++) if(g[i][j] != -1)
   proper[1][i][j] = 1 ;
 for(k=2;k<=n;k++)
  for(i=0;i+k<=n;i++)
   for(j=0;j+k<=m;j++) if(g[i][j] != -1)
   {
    if(g[i][j] == g[i+1][j+1] && proper[k-1][i+1][j+1])
     if(row[i][j] >= k && col[i][j] >= k)
      proper[k][i][j] = true ;
   }
  
 int best_sz = 0,bx = 0,by = 0 ;
 for(i=0;i<n;i++)
  for(j=0;j<m;j++) if(g[i][j] != -1)
  {
   for(k=1;proper[k][i][j];k++);
   k -- ;
   if(best_sz < k) best_sz = k,bx = i,by = j ;
  }
 assert(best_sz > 0) ;
 ct[best_sz] ++ ;
 for(i=bx;i<bx+best_sz;i++)
  for(j=by;j<by+best_sz;j++)
   g[i][j] = -1 ;
 return true ; 
}

main()
{
 int i,j,k,runs ;
 
 cin >> runs ;
 int test = 1 ;
 while(1)
 {
  cin >> n >> m ;
  for(i=0;i<n;i++)
  {
   char temp[40] ;
   cin >> temp ;
   for(j=0;j<m/4;j++)
   {
    int id = 0 ;
    if(temp[j] >= '0' && temp[j] <= '9') id = temp[j] - '0' ;
    else id = temp[j] - 'A' + 10 ;
    g[i][j*4+0] = (id>>3)&1 ;
    g[i][j*4+1] = (id>>2)&1 ;
    g[i][j*4+2] = (id>>1)&1 ;
    g[i][j*4+3] = (id>>0)&1 ;
   }
  }
/* 
  for(i=0;i<n;i++,cout << endl)
   for(j=0;j<m;j++)
    cout << g[i][j] << " " ;
*/  
  memset(ct,0,sizeof ct) ;
  int ret = 0 ;
  while(solve()) ret ++ ;
//  cout << ret << endl ;
  
  int unq = 0 ;
  for(i=1;i<=n;i++) if(ct[i]) unq ++ ;
  printf("Case #%d: %d\n",test,unq) ;
  for(i=n;i>=1;i--) if(ct[i])
   printf("%d %d\n",i,ct[i]) ;
   
  test ++ ;
  if(test > runs) break ;
 }
}
