#include<iostream>
using namespace std ;
#define MAXN 5002
int L,D ;
char in[MAXN][22] ;
char inp[1000] ;
string arr[22] ;
main()
{
 int i,j,k,runs ;
 freopen("in.in","r",stdin) ;
 freopen("out.txt","w",stdout) ;
 
 cin >> L >> D >> runs ;
 for(i=0;i<D;i++) scanf("%s",in[i]) ;
 for(int t=1;t<=runs;t++)
 {
  scanf("%s",inp) ;
  int sz = 0 ;
  for(i=0;i<22;i++) arr[i].clear() ;
  for(j=0;inp[j];j++)
  {
   if(isalpha(inp[j])) arr[sz++].push_back(inp[j]) ;
   else
   {
    j ++ ;
    while(inp[j] && isalpha(inp[j])) arr[sz].push_back(inp[j++]) ;
    sz ++ ;
   }
  }
  int ret = 0 ;
  for(i=0;i<D;i++)
  { 
   for(j=0;j<L;j++)
    if(arr[j].find(in[i][j]) == -1)
     break ;
   if(j==L) ret ++ ;
  }
  printf("Case #%d: %d\n",t,ret) ;
 }
// while(1) ;     
}
