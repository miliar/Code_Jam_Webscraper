
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
int n,a[ 16 ];
int sum(int a , int b){
      return a ^ b;
}
int dp[ 1<< 16 ];
int f(int bit){
	if(dp[ bit ]!=-1)
		return dp[ bit ];
	int w = 0, q = 0, o1 = 0,o2 =0,slv = 0;
      FOR(i , 0 , n)
		  if(bit & (1<< i))
			  w = sum(w , a[ i ]),o1 += a[ i ];
		  else
              q = sum(q , a[ i ]),o2+= a[ i ];
	 
        if(w == q && bit && bit != (1<<n )-1)
			slv = max(o1 , o2);
		FOR(i , 0 , n){
			if((bit & (1<< i)) == 0)
				slv = max(slv , f(bit | (1 << i) ) );
		}
		return dp[ bit ] = slv;
}
int main(){
     int t,x = 0;
	 ifstream fin("C-small-attempt1.in");
	 ofstream fout("output.out");
	 fin >> t; 
	 while(t){
		 MEM(dp , -1);
	      t--;
          fin >> n;
		  FOR(i , 0 , n)
			  fin >> a[ i ];
		  int y = f(0);
		  x++;
		  if(!y)
			  fout << "Case #"<<x<<": "<<"NO"<<endl;
		  else
			  fout << "Case #"<<x<<": "<<y<<endl;
		  
	 }
}
