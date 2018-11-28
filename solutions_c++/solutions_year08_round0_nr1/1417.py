#include <stdio.h>
#include <string>
using namespace std;
int memo[1001][101];
int n,m;
string q[1001],searchs[1001];
int rec( int pos , int s )
{
  int best=1<<30;
     if(memo[pos][s]!=-1)
        return memo[pos][s];
     if(pos==n)
       return 0;
    if( q[pos]==searchs[s] )
     {
        for(int r=0;r<m;r++)
         {
            if(r==s)
	     continue;
	    best=min( best,rec(pos+1,r)+1 );
         } 
     }
    else
     {
         best= rec(pos+1,s);
     }
    return memo[pos][s]=best;
}
char pal[1000000];
int main()
{
int N;
     gets(pal);
   sscanf(pal,"%d",&N);
 for(int h=0;h<N;h++)
{
 memset(memo,-1,sizeof(memo));
 int res=1<<30;
    gets(pal);
   sscanf(pal,"%d",&m);
    for(int r=0;r<m;r++)
      gets(pal),searchs[r]=pal;
    gets(pal);
   sscanf(pal,"%d",&n);
    for(int r=0;r<n;r++)
      gets(pal),q[r]=pal;
    for(int r=0;r<m;r++)
      res=min(res,rec(0,r));
   printf("Case #%d: %d\n",h+1,res);   
 }
return 0;
}
