#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <climits>
using namespace std;

#define REP(i,n) for (int i=0; i<(int)(n); ++i)
#define REPS(p,s) for (char * p = s; *p ; p++)
#define FOR(var,start,end) for (int var=(start); var<=(int)(end); ++var)
#define FORD(var,start,end) for (int var=(start); var>=(int)(end); --var) 
#define PB push_back
#define PF push_front
#define BP pop_back
#define FP pop_front
#define BN begin()
#define RN rbegin()
#define RD rend()
#define ED end()
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define IT(X) __typeof((X).BN)
#define RIT(X) __typeof((X).RN) 
#define REF(X) __typeof(__typeof(X)::reference) 
#define FORIT(it, X) for(IT(X) it = (X).BN; it != (X).ED; ++it)
#define FORITR(it, X) for(RIT(X) it = (X).RN; it != (X).RD; ++it) 
#define VV(X) vector < vector< X > >
#define PIB(X)  pair<IT(X),bool >  

typedef long long LL;
typedef unsigned long long ULL;
typedef istringstream ISS;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector< PII > VPII;

int main()
{
    int cases,caseNum;
    cin >> cases;
	caseNum = 1;
	cin.ignore();
    while(cases>0)
    {
		int n,s,p,i,y,ip;
		y=0;
		cin >> n >> s >> p ;
		for(i=0;i<n;i++)
		{
			int diff,max,a,b,c,diffChange;
			cin >> ip;
			diff = ip % 3;
			max = (int)(ip/3);
			a = max;
			b = max;
			c = max;
			diffChange = false;

			if(max >= p)
			{
				y++;
				continue;
			}
			
			if(diff == 0 && a == 0)
				continue;
			
			c++;
			if(diff > 0)
			{
				diff--;
				diffChange = true;
			}

			if(c >=p)
			{
				if(!diffChange)
				{
					if(s <= 0)
					{
						continue;
					}
					else
					{
						s--;
					}
				}
				y++;
				continue;
			}
			
			if(diff == 0 || s == 0)
				continue;
			
			c++;
			diff--;

			if(c >= p)
			{
				s--;
				y++;
				continue;
			}
		}
		printf("Case #%d: %d\n",caseNum,y);
        cases--;
		caseNum++;
    }
    return 0;
}
