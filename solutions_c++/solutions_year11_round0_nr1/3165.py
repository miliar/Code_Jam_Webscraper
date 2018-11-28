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
 	int test, case_count = 1;
 	fin>>test;
 	while(case_count <= test)
 	{
	        int number, position, ans = 0, cur_orange_pos = 1, cur_blue_pos = 1;
			int blue_elapse_time = 0, orange_elapse_time = 0;
	        char color;
	        fin>>number;
	        FOR(i, number)
	        {
			 	   fin>>color>>position;
			 	   if(color == 'O')
			 	   {
				   			int itake_time = (abs(cur_orange_pos - position));

				   			ans += (1+ max(itake_time - orange_elapse_time, 0));
				   			blue_elapse_time += ( 1 + max(itake_time - orange_elapse_time, 0));
				   			orange_elapse_time = 0;
			 	   			cur_orange_pos = position;
		           }
 	   			   else
 	   			   {
   				   			int itake_time = (abs(cur_blue_pos - position));

				   			ans += 1+ max(itake_time - blue_elapse_time, 0);
				   			orange_elapse_time += ( 1 + max(itake_time - blue_elapse_time, 0));
				   			blue_elapse_time = 0;
			 	   			cur_blue_pos = position;
		           }
            }
            fout<<"Case #"<<case_count<<": "<<ans<<endl;
            case_count++;
    }
 	system("pause");
 	return 0;
}
