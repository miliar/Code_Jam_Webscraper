
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

int main(){
   int t , x = 0;
    ifstream fin("A-large.in");
	ofstream fout("output.out");
   fin >> t;
   while(t){
         t--;
		 int n,a[ 101 ],k;
		 char c;
		 fin >> n;
		 FOR(i , 0 , n){
		      fin >> c;
			  fin >> k;
			  if(c == 'O')
				  k = -k;
			  a[ i ] = k; // for o k is neg
		 }
    int time = 0 , o = 1 , b = 1 , to = 0 , tb = 0 , p , f ;
	FOR(i , 0 , n){
		if(a[ i ] < 0){
		    k = -a[ i ];
			p = abs(k - o);
			f = p - (time - to);
			if(f < 0)
				   f = 0;
			time = time + f + 1;
			o = k;
			to = time;
		}
		else{
		      k = a[ i ];
			  p = abs(k - b);
			   f = p - (time - tb);
			   if(f < 0)
				   f = 0;
              time = time + f + 1;
			  b = k;
			  tb = time;
		
		}
		
	
	}
	x++;
	fout << "Case #"<<x<<": "<<time<<endl;
   }
}