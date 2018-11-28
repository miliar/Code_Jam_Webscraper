#include<iostream>
#include<vector>
#include<map>
using namespace std ;
int s,n,memo[1005][1005] ;
string se[505] ;
string data[1005] ;

int dat[1005] ;
int solve()
{
 int i,j,k,cur ;
 for(i=0;i<s;i++) memo[i][n] = 0 ;
 for(k=n-1;k>=0;k--)
  for(cur=0;cur<s;cur++)
  {
   if(cur != dat[k]) memo[cur][k] = memo[cur][k+1] ;
   else
   {
    memo[cur][k] = (int)1e9 ;
    for(i=0;i<s;i++) if(i != cur)
    memo[cur][k] <?= 1 + memo[i][k+1] ;
   }
  }
 int ret = memo[0][0] ;
 for(i=1;i<s;i++) ret <?= memo[i][0] ;
 return ret ;
}

main()
{
 int i,j,k ;
 char buff[1000] ;
 freopen("a.in","r",stdin) ;
 freopen("out.txt","w",stdout) ;
 int runs ;
 cin >> runs ;
 for(int t=1;t<=runs;t++)
 {
  map<string,int> m ;
 
  cin >> s ;getchar();
  for(i=0;i<s;i++)
  {
   gets(buff); 
   se[i].assign(buff) ;
   m[se[i]] = i ;
  }
  cin >> n ; getchar();
  for(i=0;i<n;i++)
  {
   gets(buff); 
   data[i].assign(buff) ;
  }
  for(i=0;i<n;i++)
  {
   if(m.count(data[i])) dat[i] = m[data[i]] ;               
   else dat[i] = -1 ;
  }
  
  int ret = solve() ;
  printf("Case #%d: %d\n",t,ret) ;    
 } 
}
