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

ifstream fin("inputX.txt");
ofstream fout("outputX.txt");

int main()
{
 	int test, case_num = 1;
 	fin>>test;
 	while(case_num <= test)
 	{
          long long int N, low, high, value, ans = -1;
          vector<long long int > music;
          bool found = 0;
          fin>>N>>low>>high;
          FOR(i, N)
          {
		   		 fin>>value;
		   		 music.PB(value);
	      }
	      FORN(i, low, high+1)
	      {
		   		  int j;
		   		  for(j=0;j<N;j++)
		   		  {
	   			        if( ((music[j]%i) == 0) || ((i%(music[j])) == 0) )
	   			             continue;
                        else
                        	break;
	   			  }
	   			  if(j==N)
	   			  {
			  		  ans = i;
			  		  break;
                  }
		  }
		  if(ans == -1)
              fout<<"Case #"<<case_num<<": NO"<<endl;
          else
          	  fout<<"Case #"<<case_num<<": "<<ans<<endl;
          case_num++;
    }
 	system("pause");
 	return 0;
}
