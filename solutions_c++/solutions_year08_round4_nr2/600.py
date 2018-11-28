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

ifstream inp("D:\\googleCodeJam\\B\\B-small-attempt1.in");
ofstream onp("D:\\googleCodeJam\\B\\small.out" , ios::out);
int nN, N;

int main()
{

inp >> N;
int n, m , a;
 for (nN = 0; nN < N; nN++) {
	  int i1, j1, i2, j2;
	  inp >> n >> m >> a;
	  int found = 0;
	  int x1, x2, y1, y2;
	  for ( i1 = 0; i1 <= n && !found; i1 ++ )
		  for ( j1 = 0; j1 <= m && !found; j1 ++ )
			  if ( !(i1 == 0 && j1 == 0) )
			  for ( i2 = 0; i2 <= n && !found; i2 ++ )
				  for ( j2 = 0; j2 <= m && !found; j2 ++)
					  if ( !(i2 == 0 && j2 == 0))
					  if ( abs ( i1 * j2 - i2 * j1 ) == a )
					  { found = 1;
					    x1 = i1; x2 = i2; y1 = j1; y2 = j2;
					  }
		
		if (found) onp<<"Case #"<< nN+1 <<": 0 0 "<< x1 <<" "<< y1<<" "<<x2<<" "<<y2<<endl;
			else onp<<"Case #"<< nN+1 <<": IMPOSSIBLE"<<endl;
	
		 
	 }
 onp.close();	 
 return 1;
 
}