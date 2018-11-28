
                         /* »Â ‰«„ Œœ« */
                            /*in the name of GOD */ 
#include<set>
#include<map>
#include<cmath>
#include<queue>
#include<limits>
#include <list>
#include <stack>
#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<fstream>
#include<algorithm>
#include<memory.h>
using namespace std;


#define vi vector<int>
#define pb push_back
# define MEM(array,w)   memset(array,w,sizeof array)
# define FOR(i,a,b) for(int i = a ; i < b ; i++)
#define S  size()
# define SET set<int>::iterator it = s.begin(); it != s.end();it++
# define ULL unsigned long long
# define eps 1e-9
# define LL  long long 
# define IS istringstream 

# define FORI(i,a,b) for(int i = a ; i <= b ; i++)
# define MFOR(i,a,b) for(int i = a ; i > b ; i--)
# define MFORI(i,a,b) for(int i = a ; i >= b ; i--)
# define PII pair<int , int>
#define all(c) (c).begin(), (c).end() 
#define maxint 1 << 31 - 1

string slv="";
char com[ 91 ][ 91 ] , opp[ 91 ];
bool tr( char c){
	if(c!= '@')
		return true;
    return false;
}
string s;
bool f(){
  if(slv.size() > 1)
	  if(tr(com[ slv[ slv.size() -1 ] ][ slv[ slv.size() -2 ] ])){
		 // cout << slv[ slv.size() -1 ] <<" # "<<slv[ slv.size() -2] << " " <<com[ slv[ slv.size() -1 ] ][ slv[ slv.size() -2 ] ]<<endl;
			  slv = slv.substr(0 , slv.size() - 2) + com[ slv[ slv.size() -1 ] ][ slv[ slv.size() -2 ] ];
			  if(slv.find(opp[ slv[ slv.size() - 1 ] ]) < slv.size()){
				  slv = "";
			      return false;
			  }
	          return true;
	  }
	  if(slv.size() >= 1)
		  if(slv.find(opp[ slv[ slv.size() - 1 ] ]) < slv.size())
				  slv = "";
	  return false;
}
int main(){
    int t , d , x =0;
	 ifstream fin("B-small-attempt0.in");
	 ofstream fout("output.out");
	fin >>t;
	while(t){
		t--;
	      int c;
	      FOR(i , 65 , 91)
			  FOR(j , 65 , 91){
			      com[ i ][ j ] = '@';
				  opp[ i ] = '@';
		  }
		  fin >> c;
		 
		  FOR(i , 0 , c){
			  fin >> s;
			  com[ s[ 0 ] ][ s[ 1 ] ] = s[ 2 ];
			  com[ s[ 1 ] ][ s[ 0 ] ] = s[ 2 ];
		  }
		  fin >> d;
		  FOR(i , 0 , d){
		     fin >> s;
			 opp[ s[ 0 ] ] = s[ 1 ];
			 opp[ s[ 1 ] ] = s[ 0 ] ;
		 }
		  int n;
		  fin >> n;
		  fin >> s;
		  slv = "";
		  FOR(i , 0 , s.size()){
		      slv += s[ i ];
			  bool e;  
			  e = f();
			  while(e)
				   e = f();

		  }
		  x++;
		  int y = slv.size();
		  fout <<"Case #"<<x<<": ["; 
		   FOR(i , 0 , y - 1)
			  fout << slv[ i ] <<", ";
		   if(y > 0)
				fout << slv[ y - 1 ];
		  fout <<"]"<<endl;
	}
}
// 1 3 AAC FDK BKA 1 CG 5 GABFD