#define Llong long long
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>


#define fill_(x,v) memset(x,v,sizeof(x))
#define for_(i,a,b) for (__typeof(b) i=(a); i<(b); i++)
#define min(x,y) (((x)>(y)) ? (y) :(x))
#define max(x,y) (((y)>(x)) ? (y) :(x))
#define mL 200
using namespace std;

ifstream inp("D:\\googleCodeJam\\B\\B-large.in");
ofstream outp("D:\\googleCodeJam\\B\\large.out" , ios::out);
int like[2001][2001];
int po[2001];
int put[3000];
int fc, cc;

int main()
{

int N;
inp>> N;

 for ( long long nN = 0; nN < N; nN++) {
     
	 int m , x , y;
	 int i , j;
     inp >> fc; inp >> cc;
	 fill_( like , -1 );
	 fill_( po, -1);
	 for ( i = 0; i < cc; i ++ ) {
		 inp >> m;
		 for ( j = 0; j < m; j++) {
			 inp >> x >> y;
			 like [i][x - 1] = y;
			 if ( y == 1 ) po[i] = x - 1;
		 }
	 }
	 
	 int res = fc + 1, mid;
	 
	  fill_(put, 0);
	  int changed = 1;
	  int finished  = 0;
	  while ( changed && !finished ) {
		  changed = 0;
		  for ( i = 0; i < cc && !finished; i++) {
			  int poss = 0;
			  for ( j = 0; j < fc; j ++)
				  if ( like [i] [j] == put [j] ) poss = 1;
		      if ( poss == 0 ) 
				  if ( po[i] == -1 ) {
					                   outp<<"Case #"<< nN+1 <<": IMPOSSIBLE";
									   finished = 1;
				  
				                     } else
									 { put [ po [ i ] ] = 1; 
          				                changed = 1;}
		  }
		  
	
			  
	  }
	  
	  
		 if ( !finished )
	     { outp<<"Case #"<< nN+1<<":" ;
	     for ( i = 0; i < fc; i++)
				 outp<<" "<<put[i];
		 }
			 outp<<endl;
	 
		 
	 
	 }
 outp.close();	 
 return 1;
 
}