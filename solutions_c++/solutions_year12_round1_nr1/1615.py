#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <list>
using namespace std;

#define rep(i,b) for(int i=(0);i<(b);++i)
#define fo(i,a,b) for(int i=(a);i<=(b);++i)
#define ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fore(a,b) for(__typeof((b).begin()) a = (b).begin();a!=(b).end();++a)
#define vv vector
#define pb push_back
#define ll long long
#define ld long double
#define ss(a) (int)(a).size()
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi vv<int>
#define vs vv<string>
#define MAX(a,b) ((a)>(b))?((a):(b))
#define MIN(a,b) ((a)<(b))?((a):(b))
#define ABS(a) ((a)>(0))?(a):(a)


class CSolver
{
public:
	bool  virtual ReadData()
	{
		return false;
		//reading data
	};
	void  virtual Solve()
	{
		if (!ReadData())
			printf("error");
		
		printf("%f ","something");
	};
};

class AA
{
public:
	int ma;
	int mb;
	float* inse;
	int keystroked;
	 AA()
	{	
	 };
	bool  virtual ReadData()
	{
		 scanf("%d", &ma);
		  scanf("%d", &mb);
		    char endofline;
   scanf("%c", &endofline);
		  inse=new float[ma+1];
		  rep(i,ma)
			  scanf("%f", &inse[i]);

		return false;
		//reading data
	};
	void   Solve()
	{	

		
		ReadData();
		float best=mb+2;
		float compelte=mb+1;
		float runni=1;
		float tempi;
		rep(i,ma+1)
		{
			
			tempi=(ma-(i))*2+(mb-ma)+1;
			float tri=tempi*runni+(1-runni)*(compelte+tempi);
			if (tri<best)
				best=tri;
			runni=runni*inse[i];
		}
		printf("%f",best);
	};		
};


int main(int argc, char ** argv) {
   int t;
    char c;
	AA solver;
   char endofline;
   scanf("%d", &t);
   scanf("%c", &endofline);
   rep (i, t) {
       printf("Case #%d: ", i+1);
	 
	   
	    solver.Solve();
		scanf("%c", &endofline);
       printf("\n");
   }
   return 0;
}