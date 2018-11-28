
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


class CandySplit
{
	public:
	CandySplit()
	{
		rep(i,32)
			m_helptable[i]=pow(2.,i);
	}

		void ReadData()
		{
			m_smallest=0xffffffff;
			rep(i,32)
			{
				m_bins[i]=0;
			}
			int t,num; 
			char tab;
			scanf("%d", &t);
			scanf("%c", &tab);
			rep (m,t)
			{
				scanf("%d", &num);
				if (m_smallest>num)
					m_smallest=num;
				rep(i,32)
					if ((num&m_helptable[i])==m_helptable[i])
						m_bins[i]++;
			}
		};
		int Solve(){
			ReadData();
			long long sean=0;
			int pat=0;
			rep(i,32)
			{
				if (m_bins[i]%2!=0)
					{
						printf("NO");
						return 0;
				}
				else
				{
					sean+=m_helptable[i]*m_bins[i];
				}
			}
			sean-=m_smallest;
		
			printf("%d",sean);
			return 0;
		};
		unsigned int m_smallest;
	int m_helptable[32];
	int m_bins[32];
};
int main(int argc, char ** argv) {
   int t;
   CandySplit cnady;
   char c;
   char endofline;
   scanf("%d", &t);
   scanf("%c", &endofline);
   rep (i, t) {
       printf("Case #%d: ", i+1);
	 //  storecredit1.GetData();
	   
	    cnady.Solve();

       printf("\n");
   }
   return 0;
}