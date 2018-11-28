

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


int main(){
     ifstream fin("A-large(1).in");
	 ofstream fout("output.out");
	 int t;
	 cout.flags(ios::fixed);
	cout.precision(6);
	 fin >> t;
	 int l = 0;
	 while(t){
		 double wp[ 101 ],g[ 101 ],oo[ 101 ],win[ 101 ],a[ 101 ][ 101 ];
		int n;
	     t--;
		 double ow[ 101 ];
		 fin >> n;
		 string s[ 101 ];
		 FOR(i , 0 , n)
			 fin >> s[ i ];
		 FOR(i , 0 , n){
			 win[ i ] = 0.;
             g[ i ] = 0.;
			 oo[ i ] = 0.;
			 ow[ i ] = 0;
			 FOR(j , 0 , s[ i ].size()){
				 if(s[ i ][ j ] == '1')
					 win[ i ]++;
				 if(s[ i ][ j ]!= '.')
					 g[ i ]++;

			 }
			
			 wp[ i ] = (double)(win[ i ] / g[ i ]); 
			
		 }
		 FOR(i , 0 , n)
			 FOR(j , 0 , n){
			    if(s[ i ][ j ]=='1')
					a[ i ][ j ] = (win[ i ] - 1) / (g[ i ] - 1);
				else if(s[ i ][ j ] == '0')
                    a[ i ][ j ] = (win[ i ]) / (g[ i ] - 1);
				else
					a[ i ][ j ] = (win[ i ]) / (g[ i ]);
		//cout << i << " % "<< j <<" "<< a[ i ][ j ] <<endl;
		 }
       
		 FOR(i , 0 , n){
			 FOR(j , 0 , n)
			  if(s[ i ][ j ] != '.')
				  ow[ i ] += a[ j ][ i ];
			 ow[ i ] = ow[ i ] / g[ i ];
		 }
		 FOR(i , 0 , n){
			   FOR(j , 0 , n)
			      if(s[ i ][ j ]!='.')
					  oo[ i ] += ow[ j ];
			   oo[ i ] = oo[ i ] / g[ i ];
		 }
		 double slv[ 101 ];
		 FOR(i , 0 , n)
			 slv[ i ] = wp[ i ] * 0.25 + 0.5 * ow[ i ] + 0.25 * oo[ i ];
		 l++;
		fout<<"Case #"<<l<<":"<<endl;
          FOR(i , 0 , n)
			  fout << slv[ i ] <<endl;
	 }

}