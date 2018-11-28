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
#include<string.h>
using namespace std ;
int a[102][102] ;
int b[102][102] ;
bool solve()
{
 int i,j,k,valid = 0 ;

 for(i=1;i<=100;i++)
  for(j=1;j<=100;j++)
   b[i][j] = a[i][j] ;
 
 for(i=1;i<=100;i++)
  for(j=1;j<=100;j++)
  {
   if(a[i][j] && !a[i-1][j] && !a[i][j-1])
   { valid = 1 ; b[i][j] = 0 ; }
   else if(!a[i][j] && a[i-1][j] && a[i][j-1])
   { valid = 1 ; b[i][j] = 1 ; }
  }
 for(i=1;i<=100;i++)
  for(j=1;j<=100;j++)
   a[i][j] = b[i][j] ;
 return valid ;
}

main()
{
 int i,j,k,runs ;
 cin >> runs ;
 for(int t=1;t<=runs;t++)
 {
  int r,x0,y0,x1,y1 ;
  
  memset(a,0,sizeof a) ;
  cin >> r ;
  while(r--)
  {
   cin >> y0 >> x0 >> y1 >> x1 ;
   for(i=x0;i<=x1;i++)
    for(j=y0;j<=y1;j++)
     a[i][j] = 1 ;
  }
//  for(i=1;i<=7;i++,cout<<endl)
//   for(j=1;j<=7;j++)
//    cout << a[i][j];
  int ret = 0 ;
  while(solve()) ret ++ ;
  printf("Case #%d: %d\n",t,ret) ;
 }
}
