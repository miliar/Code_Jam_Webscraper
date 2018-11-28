#include <iostream>
#include <fstream>
#include <sstream>

#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <list>
#include <deque>

#include <cmath>
#include <string>
#include <ctime>
#include <ctime>
#include <cstdlib>
#include <algorithm>

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,a,b) for(int i=(a);i<=(b);++i)
#define tr(v,it) for(typeof(v.begin()) it = v.begin(); it != v.end() ; ++it)
#define all(c) c.begin(),c.end()
#define SZ(c) (int)c.size()
#define SQ(x) (x)*(x)
#define OUT(a,b)FOR(i,0,b)cout << a[i] << " ";cout << endl;
#define PI 2.0*acos(0.0)
#define SET(a,b) memset(a,b,sizeof a)
#define r(T) scanf("%d",&T)

int P2[50];
bool isValid(int i, int N)
{
	++N ;
	return (N%P2[i])==0;
}
int main()
{
	P2[0] = 1;
	REP(i,1,30)P2[i] = P2[i-1]*2;
	int T,N,K;
	r(T);
	REP(i,1,T)
	{
		r(N);r(K);
		bool OK = true;
		REP(j,1,N)
		{
			if(!isValid(j,K))
			{
				OK = false;
				break;
			}
		}
		if(OK) printf("Case #%d: ON\n",i);
		else printf("Case #%d: OFF\n",i);
	}
	return 0;
}
