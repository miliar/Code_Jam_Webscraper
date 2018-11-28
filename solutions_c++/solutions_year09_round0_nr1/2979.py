#include<assert.h>
#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<iostream>
#include<cstdlib>
#include<queue>
#include<sstream>
#include<queue>
#include<ctype.h>

using namespace std;

#define re return
#define co continue
#define pb push_back
#define br break
#define sz size

typedef long long INT;

#define sf scanf
#define pf printf


char words[5000+5][20];

bool occur[20][30];

int main()
{
 freopen("A_large.in","r",stdin);
 freopen("a_large.out","w",stdout);   
    
 int l,d,n;
 sf("%d %d %d",&l,&d,&n);
 int i,j;
 for(i=0;i<d;i++)
  sf("%s",words[i]);
  int kase=1;
 while ( n--)
 {
   char rule[600];
   
   
   
   for(i=0;i<20;i++)
    for(j=0;j<30;j++) occur[i][j]=false;
   // rules ready;
   sf("%s",rule);
   i = 0;
   int pos=0;
   while ( rule[i] )
   {
    if ( rule[i] =='(')
    {
      i++;
      while ( rule[i] != ')' )
       occur[pos][rule[i]-'a']=true,i++;  
    }
    else occur[pos][ rule[i]-'a' ] = true;
    i++;
    pos++;
   }
   // match word
   int cnt=0;
   for(i=0;i<d;i++) {
    for(j=0; j<l;j++)
     if ( occur[j][ words[i][j]-'a' ] == false ) break;
     if ( j == l ) cnt++;
   } 
   pf("Case #%d: %d\n",kase++,cnt);
 }
 return 0;
}
