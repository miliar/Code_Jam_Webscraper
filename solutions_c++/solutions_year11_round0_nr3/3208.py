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

ifstream fin("C-small-attempt0.in");
ofstream fout("outputX.txt");

int main()
{
 	int test, case_cnt = 1;
 	fin>>test;
 	while(case_cnt <= test)
 	{
           int number, tmp, max_bits = (sizeof(int)*8);
   		   int me = 0, you = 0, you_sum = 0, me_sum = 0, ans = 0;
           fin>>number;
           VI array;
           FOR(i,number)
           {
       				fin>>tmp;
       				array.PB(tmp);
		   }
		   FOR(i, max_bits)
		   {
		   		  int bit_cnt = 0;
		   		  FOR(j, number)
		   		  {
				   		 if(array[j]&(1<<i))
				   		      bit_cnt++;
                  }
                  if(bit_cnt&1)
                  {
            			   fout<<"Case #"<<case_cnt<<": NO\n";
            			   goto out;
		          }
 		   }
 		   FORN(i,1,((1<<number)-1))
 		   {
		   		  me = you = me_sum = you_sum = 0;
		   		  FOR(j, number)
		   		  {
				   		 if(i&(1<<j))
				   		 {
				  			    me^=(array[j]);
				  			    me_sum+=(array[j]);
		  			     }
		  			     else
		  			     {
						  	    you^=(array[j]);
						  	    you_sum+=(array[j]);
						 }
   		          }
   		          if(you == me)
   		          {
				   		 ans = max(ans, you_sum);
				   		 ans = max(ans, me_sum);
	   		      }
  		   }
  		   fout<<"Case #"<<case_cnt<<": "<<ans<<endl;
 		   out:
		   	   case_cnt++;
    }
 	system("pause");
 	return 0;
}
