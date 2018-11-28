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

ifstream fin("B-large.in");
ofstream fout("outputX.txt");

string combine_me(string s, VS combine_str)
{
 	   int ln = SZ(s);
 	   char last = s[ln - 1], last_but_one = s[ln - 2];
 	   string ret = "";
 	   FOR(i, ln-2)
 	   		  ret+=s[i];
       foreach(it, combine_str)
       {
	   			   string combine = *it;
	   			   if( (combine[0] == last) && (combine[1] == last_but_one) ||
	   			   	   (combine[0] == last_but_one) && (combine[1] == last) )
	   			   {
				   	   ret+=combine[2];
				   	   return ret;
	   			   }
       }
       return s;
}

string oppose_me(string s, VS oppose_str)
{
 	   int ln = SZ(s);
 	   foreach(it, oppose_str)
 	   {
		   string oppose = *it;
		   char one = oppose[0], two = oppose[1];
		   int one_idx = -1, two_idx = -1;
		   FOR(i, ln)
		   {
		   		  if(s[i] == one)
		   		  {
				   		  one_idx = i;
		   		  }
		   		  if(s[i] == two)
		   		  {
				   		  two_idx = i;
		   		  }
 		   }
 		   if( (one_idx != -1) && (two_idx != -1) )
                 RET "";
       }
       return s;
}

int main()
{
 	int test, case_cnt = 1;
 	fin>>test;
 	while( case_cnt <= test)
 	{
	 	   int combine_cnt, oppose_cnt, str_ln;
	 	   VS combine_str, oppose_str;
	 	   string combine, oppose, input_str, ans = "";
	 	   fin>>combine_cnt;
	 	   while(combine_cnt)
	 	   {
	             fin>>combine;
	 	   	     combine_str.PB(combine);
	 	   	     combine_cnt--;
	       }
	       fin>>oppose_cnt;
   	 	   while(oppose_cnt)
	 	   {
	             fin>>oppose;
	 	   	     oppose_str.PB(oppose);
	 	   	     oppose_cnt--;
	       }
		   fin>>str_ln;
		   fin>>input_str;
   	       string s = "" ;
		   s+= input_str[0];
		   if(str_ln >=2)
		   {
		   		   FORN(i, 1, str_ln)
		   		   {
				   		   s+=input_str[i];
						   s = combine_me(s, combine_str);
						   s = oppose_me(s, oppose_str);
				   }
		   }
		   fout<<"Case #"<<case_cnt<<": [";
		   FOR(i, SZ(s))
		   {
		   		  fout<<s[i];
		   		  if(i != (SZ(s)-1))
		   		       fout<<", ";
		   }
		   fout<<"]\n";
	 	   case_cnt++;
    }
 	system("pause");
 	return 0;
}
