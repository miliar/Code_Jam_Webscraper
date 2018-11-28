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

ifstream fin("B-small-attempt1.in");
ofstream fout("outputX.txt");

int main()
{
 	int test, case_num = 1;
 	fin>>test;
 	while(case_num <= test)
 	{
     	  long long int L, t, N, C, c_tmp, ans = 0, cur_time = 0, index = 0;
    	   bool flag = 0;
		  vector<long long int> n_list, c_list;
		  fin>>L>>t>>N>>C;
		  FOR(i, C)
		  {
		   		 fin>>c_tmp;
		   		 c_list.PB(c_tmp);
 		  }
		  int n_cnt = 0;
		  while(n_cnt < N)
		  {
		       if( (cur_time+(c_list[n_cnt%C]*2)) <= t)
   			       cur_time+=((c_list[n_cnt%C]*2));
		       else
			   {
			   	   if(!flag)
			   	   {
				   		
				   		n_list.PB(c_list[n_cnt%C]-((t - cur_time)>>1));
				   		flag = 1;
				   		cur_time = t;
				   }
   		   		   else
			   	   	   n_list.PB(c_list[n_cnt%C]);	
				} 	  
		       n_cnt++;
		  }
		  sort(n_list.rbegin(), n_list.rend());
		  while(index < L)
		  {
			  cur_time+=n_list[index];
			  index++;
	      }
	      FORN(i, L, SZ(n_list))
	          cur_time+=(n_list[i]*2);
	      fout<<"Case #"<<case_num<<": "<<cur_time<<endl;
          case_num++;
    }
 	system("pause");
 	return 0;
}
