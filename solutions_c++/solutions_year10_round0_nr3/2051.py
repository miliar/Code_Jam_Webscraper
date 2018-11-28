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


int find(int start[], int cur_seq, int cur_qpos)
{
	int i;
	for(i=0; i<=cur_seq; i++)
		if(start[i] == cur_qpos)
			return (i);
	
	return(-1);
}



int main()
{
	int i;
	int testId, nTests;

	cin >> nTests;
	unsigned long long int g[2000];
	for(testId=1;testId<=nTests;testId++)
	{
		int R, k, N;
		int cur_qpos, cur_n_grps;
		unsigned long long int tmp, tot, cur_tot;

		//XXX  -- Read input --  XXX
		cin >> R >> k >> N;
		for(i=0; i<N; i++)
		{
			cin >> g[i];
		}

		//XXX  -- Process input --  XXX

		int cur_seq, st;
		int start[2000];
		unsigned long long int tot_cost[2000];


		tot=0;
		cur_qpos=0;
		cur_seq=-1;
		for(i=0;i<R;i++)
		{
			if ((st=find(start, cur_seq, cur_qpos)) != -1)
			{
				break; //cycle found
			}
			cur_seq++;
			start[cur_seq]=cur_qpos;
			tot_cost[cur_seq]=tot;

			cur_tot=0;
			cur_n_grps=0;
			while(cur_tot < k)
			{
				if((cur_n_grps < N) && (g[cur_qpos] <= (k-cur_tot)) )
				{
					cur_tot += g[cur_qpos];
					cur_n_grps++;
					cur_qpos++; if(cur_qpos == N) cur_qpos=0;
				}
				else
				{
					break;
				}
			}
			tot+=cur_tot;
		}

		if(i<R)
		{
			int cycleSize = cur_seq - st + 1;
			unsigned long long int cycleCost = tot - tot_cost[st];

			//cout << "DEBUG: i " << i << " R " << R << endl;
			//cout << "DEBUG: cycleSize " << cycleSize << " st " << st << " cur_seq " << cur_seq << " cycleCost " << cycleCost << endl;
			//fflush(stdout);
			
			//total number of cycles left : (R-i)/cycleSize
			tot += cycleCost * ((R-i)/cycleSize);
			i += ((R-i)/cycleSize)*cycleSize;

			for(;i<R;i++)
			{
				cur_tot=0;
				cur_n_grps=0;
				while(cur_tot < k)
				{
					if((cur_n_grps < N) && (g[cur_qpos] <= (k-cur_tot)) )
					{
						cur_tot += g[cur_qpos];
						cur_n_grps++;
						cur_qpos++; if(cur_qpos == N) cur_qpos=0;
					}
					else
					{
						break;
					}
				}
				tot+=cur_tot;			
			}
		}

		//XXX  -- Print output --  XXX
		cout << "Case #"<<testId << ": " << tot << endl;
	}

	return 0;
}
