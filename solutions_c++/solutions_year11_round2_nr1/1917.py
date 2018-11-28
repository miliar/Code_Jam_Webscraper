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


struct 	NODE
{
 		double wwp;
 		int w_cnt, l_cnt;
 		NODE(int w, int l, double wp)
 		{
		 		 w_cnt = w;
		 		 l_cnt = l; 
		 		 wwp = wp;
        }
};
int main()
{
 	int test, case_num = 1;
 	fin>>test;
 	while(case_num <= test)
 	{
         int N;
         vector<NODE> wp;
         vector<NODE> owp;
         vector<NODE> oowp;
         vector<double> ans;
         string str;
		 fin>>N;
		 VS matrix;
		 FOR(i, N)  
		 {
		     fin>>str;
		     matrix.PB(str);
	     }
	     FOR(i, N)
	     {
		  		int w_cnt = 0, l_cnt = 0;
		  	 	FOR(j, N)
		  	 	{
				 	   if(matrix[i][j] == '1')
					   		w_cnt++;		   
  				       else if(matrix[i][j] =='0')
  				            l_cnt++; 
		 	    }
		 	    NODE add(w_cnt, l_cnt, (w_cnt*1.0)/(w_cnt+l_cnt*1.0));
		 	    wp.PB(add);
 		 }
 		 FOR(i, N)
 		 {
		  		int w_cnt = 0, l_cnt = 0, cnt = 0;
		  		double my = 0.0;
		  		FOR(j, N)
		  		{
				 	   if(i==j)
				 	       continue;
 	                   if(matrix[j][i]=='.')
                           continue;
					   NODE opp = wp[j];
					   if(matrix[j][i] == '1')
					       opp.w_cnt--;
					   else if(matrix[j][i] == '0')
					       opp.l_cnt--;        
					   w_cnt+=opp.w_cnt;
					   l_cnt+=opp.l_cnt;
					   my+=((opp.w_cnt*1.0)/(opp.w_cnt+opp.l_cnt*1.0));
					   cnt++;
	 	        }
	 	        NODE opp(w_cnt, l_cnt, (my/cnt));
	 	        owp.PB(opp);
  		 }
  		 FOR(i, N)
 		 {
		  		int w_cnt = 0, l_cnt = 0, cnt = 0;
		  		double my = 0.0;
		  		FOR(j, N)
		  		{
				 	   if(i==j)
				 	       continue;
 	                   if(matrix[j][i] == '.')
                            continue;
					   NODE opp = owp[j];
					   w_cnt+=opp.w_cnt;
					   l_cnt+=opp.l_cnt;
				   	   my+=(opp.wwp);
					   cnt++;
	 	        }
	 	        NODE opp(w_cnt, l_cnt, (my/cnt));
	 	        oowp.PB(opp);
  		 }
  		 FOR(i, N)
 		      cout<<i<<" "<<wp[i].wwp<<" "<<owp[i].wwp<<" "<<oowp[i].wwp<<endl;
  		 FOR(i, N)
  		      ans.PB((0.25 *wp[i].wwp) + (0.5 * owp[i].wwp) + (0.25 *oowp[i].wwp));
         fout<<"Case #"<<case_num<<":"<<endl;
         FOR(i, N)
         		fout<<ans[i]<<endl;
         case_num++;
    }
 	system("pause");
 	return 0;
}
