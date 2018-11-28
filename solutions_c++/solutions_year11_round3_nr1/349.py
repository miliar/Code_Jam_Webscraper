/*
This program is develpoed by Ratan Dhorawat.
*/

#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <stdio.h>
#define f(i,j,n) for(int (i)=(j);(i)<(n);(i)++)
#define fr(i,j,n)for(int (i)=(n-1);(i)>=(j);(i)--)
using namespace std;

bool valid(int i,int j,int r,int c)
{
     if(i>=0&&i<r&&j>=0&&j<c)
     return true;
     return false;
}
int main()
{
 
 int T;
 cin>>T;
 int cas=0;
 while(T--){cas++;
 string s[55];
 int r,c;
 cin>>r>>c;
 f(i,0,r)
 cin>>s[i];
 bool flag=true;
 f(i,0,r)
 {
   f(j,0,c)
   {
           if(s[i][j]=='#')
           {
                           if(valid(i+1,j+1,r,c)&&(s[i][j+1]=='#'&&s[i+1][j+1]=='#'&&s[i+1][j]=='#'))
                           {
                                               
                              s[i][j]='/';
                              s[i][j+1]='\\';
                              s[i+1][j]='\\';
                              s[i+1][j+1]='/';                  
                           }
                           else{
                           flag=false;
                           break;
                           }
           }
   }     
   if(!flag)break;   
 }
 cout<<"Case #"<<cas<<":\n";
 if(flag) 
 f(i,0,r)
 {
         f(j,0,c)
         cout<<s[i][j];
         cout<<endl;
 }
 else
 cout<<"Impossible\n";
}
 return 0;
}
