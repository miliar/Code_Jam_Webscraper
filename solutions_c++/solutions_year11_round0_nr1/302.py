#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std ;
#define MAXN 102
int M,a[MAXN],b[MAXN] ;

int sz,q[MAXN * MAXN * MAXN * 10] ;
int best[MAXN][MAXN][MAXN * 2] ;
void push(int k1,int k2,int where,int steps)
{
 if(best[k1][k2][where] == -1)
 {
  best[k1][k2][where] = steps ;
  q[sz++] = k1 ;
  q[sz++] = k2 ;
  q[sz++] = where ;
 }
}

int main()
{
 int runs ;
 cin >> runs ;
 for(int T = 1;runs--;T++)
 {
  sz = 0 ;
  memset(best,255,sizeof best) ;

  printf("Case #%d: ",T) ;
  cin >> M ;
  for(int i = 0;i < M;i++)
  {
   string s ;
   int loc ;
   cin >> s >> loc ;
   if(s == "O") { a[i] = 0 ; b[i] = loc ; }
   else { a[i] = 1 ; b[i] = loc ; }
  }
  push(1,1,0,0) ;
  int ret = -1 ;
  for(int i = 0;i < sz;i += 3)
  {
   int k1 = q[i],k2 = q[i + 1],where = q[i + 2] ;
   int steps = best[k1][k2][where] ;
   if(where == M) { ret = steps ; break ; }
   int dx[] = {-1,0,1} ;
   for(int j = 0;j < 3;j++)
    for(int k = 0;k < 3;k++)
    {
     int k11 = k1 + dx[j],k21 = k2 + dx[k] ;
     if(k11 < 1 || k11 > 100 || k21 < 1 || k21 > 100) continue ;
     push(k11,k21,where,steps + 1) ;
    }
   if(a[where] == 0 && b[where] == k1)
   {
    for(int j = 0;j < 3;j++)
    {
     int k11 = k1,k21 = k2 + dx[j] ;
     if(k11 < 1 || k11 > 100 || k21 < 1 || k21 > 100) continue ;
     push(k11,k21,where + 1,steps + 1) ;
    }
   }
   if(a[where] == 1 && b[where] == k2)
   {
    for(int j = 0;j < 3;j++)
    {
     int k11 = k1 + dx[j],k21 = k2 ;
     if(k11 < 1 || k11 > 100 || k21 < 1 || k21 > 100) continue ;
     push(k11,k21,where + 1,steps + 1) ;
    }
   }
  }
  printf("%d\n",ret) ;
 }
 return 0 ;
}
