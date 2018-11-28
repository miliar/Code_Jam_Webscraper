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

ifstream inp("D:\\googleCodeJam\\A\\A-large.in");
ofstream onp("D:\\googleCodeJam\\A\\large.out" , ios::out);
int nN, N;
int getone[20001];
int getzero[20001];
int input[20001];
int C[20001];

int getmin ( int x, int y)
{
	if ( x== -1 ) return y;
	if ( y== -1 ) return x;
	if ( x < y ) return x;
	return y;
}

int addd ( int x, int y )
{
	if (x == -1 || y == -1 ) return -1;
	return x + y;
}
int main()
{

inp >> N;
int M,V, i;
 for (nN = 0; nN < N; nN++) {
	  inp >> M >> V;
	  for ( i = 1; i <=  ( M - 1 ) /2; i ++ )
		  inp >> input[i] >> C[i];
	  for (  i =  ( M - 1 ) /2 + 1; i <= M ;i ++ )
		  inp >> input[i];
		
	  
	  fill_ (getone, -1);
	  fill_ (getzero, -1);
	  
	  
	  for ( i = ( M - 1 ) /2 + 1 ; i <= M; i ++)
		  if ( input [i] == 0 ) getzero[i] = 0;
			  else getone[i] = 0;
	  int j;
	  for ( i = (M - 1 ) / 2; i >= 1; i -- )
	  {  int left, right;
	     left =  i * 2; right = i * 2 + 1;
	     
		
		 
		 if ( input[i] == 1 )
			 
			 { getzero[i] = getmin (getzero[i], 
			                        getmin( getzero[left], getzero[right])
									);
		       getone[i] =  getmin (getone[i], addd ( getone[right] , getone[left]) );
			   if (C[i]){
			   getzero[i] = getmin (getzero[i], 
			                        addd (addd ( getzero[left] , getzero[right]) , 1 ) );
		       getone[i] = getmin (getone[i], 
			                      addd (getmin ( getone[right] , getone[left]) , 1));
			   }
			 }
		 
		 if ( input[i] == 0 )
			 { getzero[i] = getmin (getzero[i], addd ( getzero[left], getzero[right]));
		       getone[i] = getmin (getone[i], getmin ( getone[right] , getone[left]));
			   if (C[i]){
			   getzero[i] = getmin (getzero[i], 
			              addd(getmin ( getzero[left] , getzero[right]) ,1));
		       getone[i] = getmin (getone[i],
                       addd(			   addd ( getone[right] , getone[left]) ,1)) ;
			   }
			 }
	  }
	  
		int res;
		if (V == 1 ) res = getone[1]; else res = getzero[1];
		if (res >= 0)  onp<<"Case #"<< nN+1 <<": "<<res<<endl;
		else   onp<<"Case #"<< nN+1 <<": "<<"IMPOSSIBLE"<<endl;
	// onp<<"Case #"<< nN+1 <<": "<< maxF<<" "<<minD<<" "<<minB<<endl;
		 
	 
 }
 onp.close();	 
 return 1;
 
}