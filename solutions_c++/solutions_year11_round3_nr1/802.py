#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define RET return
#define FOR(i,n) for(int i=0;i<(int)n;++i)
#define SZ(n) ((int)n.size())

#define FORN(i,start,end) for(int i=start;i<end;++i)
#define FORD(i,n) for(int i=(int)n;i>=0;--i)
#define SET(a,n) memset(a,n,sizeof(a))
#define foreach(it,x) for(__typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define PB push_back

typedef vector<string> VS;
typedef vector<int> VI;
typedef stringstream SS;

ifstream fin("A-large.in");
ofstream fout("outputX.txt");

int main()
{
 	int test, case_num = 1;
 	fin>>test;
 	while(case_num <= test)
 	{
          int R, C;
          bool fail = 0;
          string row_str;
          VS matrix;
          fin>>R>>C;
          FOR(i, R)
          {
		   		 fin>>row_str;
		   		 matrix.PB(row_str);
	      }
	      FOR(i, R)
	      {
		   		 FOR(j, C)
		   		 {
				  		if(matrix[i][j] == '#')
				  		{
			 				  if( ((i+1)<R) && ((j+1)<C) )
			 				  {
							   	  matrix[i][j] = '/';
							   	  if(matrix[i+1][j]=='#')
				  						 matrix[i+1][j] = '\\';
	  						      else
	  						      {
								   	     fail = 1;
	  						      	     goto failed;
					      	     }
							   	  if(matrix[i][j+1] =='#')
					 				     matrix[i][j+1] = '\\';
 			 				      else
 			 				       {
								   	     fail = 1;
	  						      	     goto failed;
							       }
							   	  if(matrix[i+1][j+1] == '#')
							              matrix[i+1][j+1] = '/';
							   	  else
							   	  {
								   	     fail = 1;
	  						      	     goto failed;
							      }
							   }
							  else
							  {
							   	  fail = 1;
							  	  goto failed;
							  }
	 				    }
		         }
	      }
   	      failed:
          fout<<"Case #"<<case_num<<":\n";
		  		 if(fail)
				 		 fout<<"Impossible\n";
                 else
                 {
				  	 FOR(i, R)
				  	 {
				  	 		FOR(j, C)
				  	 		{
				  	 			   fout<<matrix[i][j];
					        }
					        fout<<endl;
		             }
				 }
          case_num++;
    }
 	system("pause");
 	return 0;
}
