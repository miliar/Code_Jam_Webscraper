#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <complex>
#include <climits>
#include <queue>
#include <ctime>

using namespace std;

#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define rep(i,x,n) for(int i = (x) ; i < (n) ; ++i)
#define repit(it,x,n) for(__typeof(x) it = (x) ; it!=(n) ;++it)

struct ST{
	int o,b,ind;
	ST(){}
	ST(int a,int b,int c)
		:o(a),b(b),ind(c){}
};

int d[][2]={{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};

int n;
int ty[105],in[105];
int vis[105][105][105];

int main()
{
	freopen("a.txt","rt",stdin);
	freopen("a.out","wt",stdout);
	int t,x,y;
	char c;
	scanf("%d",&t);
	rep(tt,0,t)
	{
		scanf("%d",&n);
		rep(i,0,n){
			scanf(" %c ",&c);
			scanf("%d",&y);
			x = (c=='B'?1:0);
			ty[i] = x;
			in[i] = y;
		}
		queue<ST>q;
		rep(i,0,102)
			rep(j,0,102)
				rep(k,0,n+1)
					vis[i][j][k]=1000000;
		vis[1][1][0]=0;
		q.push(ST(1,1,0));
		ST p;
		while(!q.empty())
		{
			p = q.front();
			q.pop();
			/*if(p.ind == n)
				break;*/
			if(in[p.ind] == p.b && ty[p.ind] == 1){
				rep(i,-1,2){
					if(p.o+i<=0||vis[p.o+i][p.b][p.ind+1]<=vis[p.o][p.b][p.ind]+1)
						continue;
					vis[p.o+i][p.b][p.ind+1]=vis[p.o][p.b][p.ind]+1;
					q.push(ST(p.o+i,p.b,p.ind+1));
				}
			}
			if(in[p.ind] == p.o && ty[p.ind] == 0){
				rep(i,-1,2){
					if(p.b+i<=0||vis[p.o][p.b+i][p.ind+1]<=vis[p.o][p.b][p.ind]+1)
						continue;
					vis[p.o][p.b+i][p.ind+1]=vis[p.o][p.b][p.ind]+1;
					q.push(ST(p.o,p.b+i,p.ind+1));
				}
			}
			rep(i,0,8)
			{
				if(p.o+d[i][0]<=0||p.b+d[i][1]<=0||vis[p.o+d[i][0]][p.b+d[i][1]][p.ind]<=vis[p.o][p.b][p.ind]+1)
					continue;
				vis[p.o+d[i][0]][p.b+d[i][1]][p.ind]=vis[p.o][p.b][p.ind]+1;
				q.push(ST(p.o+d[i][0],p.b+d[i][1],p.ind));
			}
		}
		int res = INT_MAX;
		rep(i,0,101)
			rep(j,0,101)
				res=min(res,vis[i][j][n]);
		printf("Case #%d: ",tt+1);
		printf("%d\n",res);
	}

	return 0;
}