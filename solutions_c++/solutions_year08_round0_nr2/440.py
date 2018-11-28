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

ifstream inp ( "D:\\googleCodeJam\\Fly Swatter\\B-large.in");
ofstream onp ( "D:\\googleCodeJam\\Fly Swatter\\loutput.out" , ios::out);

struct event{
	int starttime;
	int endtime;
    int type;
	int finished;
} trips[1000], mid;
int main()
{
	int n;
	inp >> n;
	int i, j, h1, h2, m1, m2;
	char c;
	int T, NA, NB;
	for ( i = 0; i < n; i++ ) 
	{
	   inp >> T;
	   inp >> NA >> NB;
	   for ( j = 0; j < NA; j++){
		   inp >> h1; inp >> c; inp >> m1;
		   inp >> h2; inp >> c; inp >> m2;
		   trips[j].starttime = h1*60+m1; trips[j].endtime = h2*60+m2;
		   trips[j].type = 1; trips[j].finished = 0;
	   }
	   
	   for ( j = 0; j < NB; j++){
		   inp >> h1; inp >> c; inp >> m1;
		   inp >> h2; inp >> c; inp >> m2;
		   trips[j + NA].starttime = h1*60+m1; trips[j + NA].endtime = h2*60+m2;
		   trips[j + NA].type = 2; trips[j + NA].finished = 0;
	   }
		   
	   int N = NA + NB;
	   
	   for ( int j1 = 0; j1 < N; j1++ )
		for ( int j2 = j1 + 1; j2 < N; j2++ )
		   if (trips[j1].starttime > trips[j2]. starttime)
		   { mid = trips [j1]; trips[j1] = trips [j2]; trips[j2]= mid;}
		
	   int CA = 0;
	   int CB = 0;
	   for ( int p = 0; p < N; p++)
		   if ( trips[p].finished == 0) {
		   
		   trips[p].finished = 1;
		   int nextt = trips[p].endtime + T;
		   int ctype = trips[p].type;
		   
		   if ( ctype == 1 ) CA ++; else CB ++;
		   
		   for ( j = p; j < N; j ++ )
			   if ( trips[j].finished == 0 && trips[j].starttime >= nextt 
				   && trips[j].type == 3-ctype)
				   {
				     trips[j].finished = 1;
					 nextt = trips[j].endtime + T;
					 ctype = trips[j].type;
				   }
		   
		   
	   }
	   cout<< CA <<" "<<CB<<endl;
	   onp<<"Case #"<< i + 1<<": "<< CA<<" "<<CB<< endl;
	}
	
	
}