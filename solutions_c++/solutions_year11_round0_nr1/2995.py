#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <string>
#include <memory.h>
using namespace std;
    
#define pb push_back
#define fi first
#define sc second
#define mp make_pair
#define cs c_str
#define ALL(c) (c).begin(), (c).end()
#define RALL(c) (c).rbegin(), (c).rend()
#define RESET(c,x) memset (c, x, sizeof (c))
#define ren(a,b,c) for (int a=b;a<c;a++)
#define red(a,b,c) for (int a=b;a>=c;a--)
#define repi(it,c) for (__typeof ((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define pqd(c) priority_queue <__typeof(c)>
#define pqi(c) priority_queue < __typeof(c),vector<__typeof(c)>,greater<__typeof(c)> >

const double eps = 1e-9;

typedef long long ll;
typedef pair <int,int> pii;

//lintaor1's template

int main()
{
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	ren (N,1,T+1)
	{
		char i[9];
		int n, a, op=1, bp=1, res1=0, res2=0;
		vector <bool> gil;
		queue <int> O, B;
		
		scanf("%d",&n);
		ren (x,0,n) scanf("%s%d",i,&a), (i[0]=='O') ? (gil.pb(true),O.push(a)) : (gil.pb(false),B.push(a));
		repi(it,gil)
		{
			if (*it) //orange move
			{
				//printf("O : %d %d\n",O.front(),op);
				res1 += abs(O.front()-op) + 1;
				res1 = max( res2+1,res1 );
				op=O.front();
				O.pop();
			}
			else //blue move
			{
				//printf("B : %d %d\n",B.front(),bp);
				res2 += abs(B.front()-bp) + 1;
				res2 = max( res1+1,res2 );
				bp=B.front();
				B.pop();
			}
		}
		
		printf("Case #%d: %d\n",N,max( res1,res2 ));
	}
	return 0;
}
