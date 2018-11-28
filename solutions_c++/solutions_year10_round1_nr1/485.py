#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>



//#define INCLUDE_LP

#ifdef INCLUDE_LP
	#include "lp_lib.h"
#else
	#if defined (__GNUC__) && (__GNUC__ <= 2)
	#include <hash_map>
	#include <hash_set>
	#else
	//#include <ext/hash_map>
	//#include <ext/hash_set>
	using namespace __gnu_cxx;
	#endif
#endif



using namespace std;

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
//#include <boost/regex.hpp>



#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;

LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }

#define pi acos(-1.)
#define eps 1e-7
#define inf 1e17




char b[100][100];
char nb[100][100];
int main()
{
	int i,j,m;
	int testId, nTests;

	cin >> nTests;
	for(testId=1;testId<=nTests;testId++)
	{
		int num, k, col, r, wr, d;
		cin >> num >> k;

		//XXX  -- Read input --  XXX
		for(i=0; i<num; i++)
		{
			cin >> b[i];
			#ifdef DBG
			cout << b[i] << endl;
			#endif
		}

		//XXX  -- Process input --  XXX
		for(col=0; col<num; col++)
		for(r=num-1,j=0; r>=0; r--, j++)
		{
			nb[col][j] = b[r][col];
		}

		#ifdef DBG
		cout << "---------------------------------------" << endl;
		for(i=0; i<num; i++)
		{
			cout << nb[i] << endl;
		}
		#endif

		for(col=0; col<num; col++)
		{
			for(wr=r=num-1; r>=0; r--)
			{
				if(nb[r][col] != '.')
				{
					nb[wr][col] = nb[r][col];
					wr--;
				}
			}
			for(; wr>=0; wr--)
				nb[wr][col] = '.';
		}
		
		#ifdef DBG
		cout << "---------------------------------------" << endl;
		for(i=0; i<num; i++)
		{
			cout << nb[i] << endl;
		}
		#endif

		int R, B, Rwin, Bwin;


		Rwin=0; Bwin=0;

		//check row wise

		for(r=0; r<num; r++)
		{
		R=0; B=0;
		for(col=0; col<num; col++)
		{
			if(nb[r][col] == 'R')
			{
				R++;
				B=0;
				if(R == k)
					Rwin=1;
			}
			else if (nb[r][col] == 'B')
			{
				B++;
				R=0;
				if(B == k)
					Bwin = 1;
			}
			else
			{
				R=B=0;
			}
		}
		}

		//check column wise
		R=0; B=0;
		for(col=0; col<num; col++)
		{
		R=0; B=0;
		for(r=0; r<num; r++)
		{
			if(nb[r][col] == 'R')
			{
				R++;
				B=0;
				if(R == k)
					Rwin=1;
			}
			else if (nb[r][col] == 'B')
			{
				B++;
				R=0;
				if(B == k)
					Bwin = 1;
			}
			else
			{
				R=B=0;
			}
		}
		}

		for(d=0; d<(2*num-1); d++)
		{
			if(d<num)
			{
				r=d%num;
				col=0;
			}
			else
			{
				col=d%num;
				r=num-1;
			}
		
		
			R=0; B=0;
			while(r>=0 && col<num)
			{
				if(nb[r][col] == 'R')
				{
					R++;
					B=0;
					if(R == k)
						Rwin=1;
				}
				else if (nb[r][col] == 'B')
				{
					B++;
					R=0;
					if(B == k)
						Bwin = 1;
				}
				else
				{
					R=B=0;
				}
			
				r--;
				col++;
			}

		
		}

		for(d=0; d<(2*num-1); d++)
		{
			if(d<num)
			{
				//r=d%num;
				//col=d;
				r=0;
				col=num-1-d;
			}
			else
			{
				//col=d%num;
				//r=num-1;

				col=0;
				r=d-(num-1);
			}

			R=0; B=0;
			while(r<num && col<num)
			{
				if(nb[r][col] == 'R')
				{
					R++;
					B=0;
					if(R == k)
						Rwin=1;
				}
				else if (nb[r][col] == 'B')
				{
					B++;
					R=0;
					if(B == k)
						Bwin = 1;
				}
				else
				{
					R=B=0;
				}
			
				r++;
				col++;
			}

		}

		//XXX  -- Print output --  XXX
		printf("Case #%d: ",testId);

		//cout << "Rwin : " << Rwin << " Bwin : " << Bwin << endl;
		if(Rwin == 0 && Bwin == 0)
			printf("Neither\n");
		else if (Rwin == 1 && Bwin == 0)
			printf("Red\n");
		else if (Rwin == 0 && Bwin == 1)
			printf("Blue\n");
		else
			printf("Both\n");
	}

	return 0;
}
