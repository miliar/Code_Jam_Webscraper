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

ifstream inp("D:\\googleCodeJam\\D\\D-small-attempt2.in");
ofstream onp("D:\\googleCodeJam\\D\\small.out" , ios::out);

int main()
{
int N;
int i,j,k;
int n, h, w, r;
int rx[1000], ry[1000];

int ways[200][200];

inp>>N;
 for ( long long nN = 0; nN < N; nN++) {
	 cout<<"Case #"<< nN+1 <<": ";
	 onp<<"Case #"<< nN+1 <<": ";
	 inp >> h >> w >> r;
	 for ( i  = 0; i < r; i ++ )
		 inp>> rx[i]>>ry[i];
	 
	 fill_ ( ways, 0);
	 for ( i  = 0; i < r; i ++ )
	  ways[rx[i]][ry[i]] = -2;
	 
	 ways[1][1] = 1;
	 for ( i = 1; i <= h; i ++ )
	 for ( j = 1; j <= w; j ++ )
		 if ( ways[i][j] > 0 ){
			 if ( ways[i + 2] [j + 1] != -2 )
				 ways[i + 2][j + 1] += ways[i][j],
				 ways[i + 2][j + 1] %= 10007;
			 
			 if ( ways[i + 1] [j + 2] != -2 )
				 ways[i + 1][j + 2] += ways[i][j],
				 ways[i + 1][j + 2] %= 10007;
			 
		 }
	 onp<<ways[h][w]<<endl;
	 
	 }
 onp.close();	 
 return 1;
 
}