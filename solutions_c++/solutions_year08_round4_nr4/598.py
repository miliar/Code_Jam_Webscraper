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

ifstream inp("D:\\googleCodeJam\\D\\D-small-attempt0.in");
ofstream onp("D:\\googleCodeJam\\D\\small.out" , ios::out);
int nN, N;


string per( string s, vector <int> v ){
	 string res = s;
	 int i , j;
	 for ( i = 0; i < s.length() / v.size(); i ++ )
		 for ( j = 0; j < v.size(); j ++ )
			{ //cout<< v[j]<<endl;
				res[i * v.size() + j] = s[i * v.size() + v[j]];
		      }
	  return res;
}

int RLE ( string s )
{ int res = 0;
  int i ;
  for ( i = 1; i < s.length(); i ++ )
	  if ( s[i] != s[i-1] ) res ++;
  return res;
}

int main()
{

inp >> N;
int k;
string s;
int i;
 for (nN = 0; nN < N; nN++) {
	 inp >> k;
	 inp >> s;
	 vector <int> v;
	 v.clear();
	 
	 for (i=0; i< k ; i++) v.push_back(i);
				
				int minV = RLE (per( s , v));		
				//caculation first
			
			   while ( next_permutation( v.begin(), v.end() ) )
				
				{ 
					int mid = RLE (per( s , v));
					
				  minV = min( minV, mid);		
				}
	 onp<<"Case #"<< nN+1 <<": "<< minV + 1<<endl;
	// onp<<"Case #"<< nN+1 <<": "<< maxF<<" "<<minD<<" "<<minB<<endl;
		 
	 }
 onp.close();	 
 return 1;
 
}