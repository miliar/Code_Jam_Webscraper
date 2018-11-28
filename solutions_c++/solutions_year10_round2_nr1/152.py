#include<iostream>
#include<stdio.h>
#include<vector>
#include<string.h>
#include<sstream>
using namespace std ;
#define MAXN 202
int p1,p2 ;
vector<string> have[MAXN],need[MAXN] ;

bool match1(int i1,int i2,int len)
{
 if(have[i2].size() < len) return false ;
 for(int i=0;i<len;i++)
  if(need[i1][i] != have[i2][i])
   return false ;
 return true ;
}

bool match2(int i1,int i2,int len)
{
 if(need[i2].size() < len) return false ;
 for(int i=0;i<len;i++)
  if(need[i1][i] != need[i2][i])
   return false ;
 return true ;
}

main()
{
 int i,j,k,runs ;
 cin >> runs ;
 for(int t=1;t<=runs;t++)
 {
  cin >> p1 >> p2 ;
  for(i=0;i<p1;i++)
  {
   have[i].clear() ;
   string temp ;
   cin >> temp ;
   for(j=0;j<temp.size();j++)
    if(temp[j] == '/')
     temp[j] = ' ' ;
   istringstream iss(temp) ;
   string temp2 ;
   while(iss >> temp2) have[i].push_back(temp2) ;
  }
  for(i=0;i<p2;i++)
  {
   need[i].clear() ;
   string temp ;
   cin >> temp ;
   for(j=0;j<temp.size();j++)
    if(temp[j] == '/')
     temp[j] = ' ' ;
   istringstream iss(temp) ;
   string temp2 ;
   while(iss >> temp2) need[i].push_back(temp2) ;
  }
/*  
  for(i=0;i<p1;i++,cout<<endl)
   for(j=0;j<have[i].size();j++)
    cout << have[i][j] << " " ;
  for(i=0;i<p2;i++,cout<<endl)
   for(j=0;j<need[i].size();j++)
    cout << need[i][j] << " " ;
*/  
  int ret = 0 ;
  for(i=0;i<p2;i++)
  {
   int mx = 0 ;
   for(j=0;j<p1;j++)
   {
    for(k=0;k<have[j].size() && k<need[i].size() && have[j][k] == need[i][k];k++);
    mx = max(mx,k) ;
   }
   ret += need[i].size() - mx ;
   have[p1++] = need[i] ;
  }
/*
   for(j=0;j<need[i].size();j++)
   {
    for(k=0;k<p1;k++) if(match1(i,k,j+1)) break ;
    if(k < p1) continue ;
    for(k=0;k<i;k++) if(match2(i,k,j+1)) break ;
    if(k < i) continue ;
    ret ++ ;
   }
*/
  printf("Case #%d: %d\n",t,ret) ;
 }
}
