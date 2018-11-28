#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <list>
#include <stack>
#include <numeric>
#include <queue>
#include <cstdlib>
#include <cmath>
#include <cstdio>
using namespace std;
#define debug(a) cout << #a
#define FO(it,a) for(__typeof(a)::iterator it=a.begin();it!=a.end();++it)
#define FZ(i,n) for(int i=0;i<n;++i)
#define FL(i,s,e) for(int i=s;i<e;++i)
#define CL(s,t) memset(s,t,sizeof(s))
#define sz size()
#define pb push_back
#define B begin()
#define E end()
#define all(a) a.B,a.E 
#define GI ({int t;scanf("%d",&t);t;})
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<vector<int> > vvi;
bool gr[101][22];
int pcount(int s)
{
	int ret = 0;
	while(s) s = s & (s - 1),++ret;
	return ret;
}
int main()
{
	int tt = GI;
	FZ(t,tt)
	{
		CL(gr,0);
		int n = GI;
		int c = GI;
		FZ(i,c)
		{
			int lim = GI,x,y;
			FZ(j,lim) 
			{
				x = GI;y = GI;	
				gr[i][x - 1 + n*y] = 1;
			}
		}
	
		int best =-1, bestp ;
		FZ(s,((1<<n)))
		{
			
			int cnt = 0;
			FZ(i,c) 
			{	
				FZ(j,2*n) 
				if(gr[i][j]==1)
				if ( ((s & (1<<(j%n))) != 0) == j/n )	
					goto here ;
				continue;	
			here:  cnt ++;
			}
			if(cnt == c )
			{	
				if(best == -1 || bestp > pcount(s)) 
					best = s, bestp = pcount(s);
			}
		}	
		cout <<"Case #"<<t+1<<": ";
		if(best != -1)
			FZ(i,n) cout << ((best & (1<<i))!=0) << " ";
		else cout << "IMPOSSIBLE";
		cout << endl;

	}
	return 0;
}
