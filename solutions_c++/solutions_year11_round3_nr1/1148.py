#include<cstdio>
#include <cctype>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include <deque>
#include <math.h>
#include<stdio.h>
#include<memory.h>
using namespace std;


typedef stringstream ss;
typedef vector<string> vs;
typedef vector<int> vi;
typedef long long int64;

#define PI 3.14159265
#define pb push_back
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define FORnm(i,n,m) for (int i=n; i<=(int)(m); i++)
#define forn(i,n) for (int i=0; i<(int)(n); i++)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)

int dx[]={1,1,0,-1},dy[]={0,1,1,1};
#define MAXIMO 1000

#define Small
//#define Large



int main()
{

	//	freopen("A-small-attempt0.in", "r", stdin);	freopen("respuestaS_A.out", "w+", stdout);
	freopen("A-large.in", "r", stdin);	freopen("respuestaL.out", "w+", stdout);


	int i, j, tc,m,n,b,cnt,T,R,C;
  scanf( "%d", &T);
	FORnm(tc,1,T)
	{
	    
	scanf( "%d%d", &R,&C); 
	char B[100];
  char D[100][100];
  bool next=true;
	forn(i,R)
	{
	  scanf( "%s", &B);
	  forn(j,C)
	  {
		 	D[i][j]=B[j];			 
			}				 				 
	 }
	 
	 
	 forn(i,R)
		 if(next)					 
	   forn(j,C)
	   {			
		 	 if(D[i][j]=='#')
				 {
				 	if( D[i+1][j]=='#' && D[i+1][j +1]=='#' && D[i][j+1]=='#' )
			     {
					 		D[i][j]='/';							
					 		D[i+1][j]='\\'; 
							 D[i+1][j +1]='/';
							  D[i][j+1]='\\'; 
								
							 }
			   else
			     {
					 	 printf( "Case #%d:\n Impossible\n", tc);
					 	 next=false;
					 	 break;
						 }
				 }									
			 }
			 else break;
	if(next)
	{   
	printf( "Case #%d: \n", tc);
	forn(i,R)
	{
	   forn(j,C)
			printf( "%c",  D[i][j]);
	printf( "\n");		
  }	 
}
	   
	   
} 
	return 0;
}
