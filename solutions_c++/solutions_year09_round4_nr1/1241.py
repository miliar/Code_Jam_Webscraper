#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <vector>
#include <set>
#define MAX_N 100
#define INF 1000000000
using namespace std;

#define REP(i,n) for(int i=0,_n=(n);i<_n;i++)
#define FOR(i,a,b) for(int i=(a),_n=(b);i<=_n;i++)
#define _m(a,b) memset(a,b,sizeof(a))


char temp2[MAX_N];
int num[MAX_N];
map<int,int> dist;

int main()
{
	int t,n;
	scanf("%d",&t);
	REP(__,t)
	{
		int res = 0;
		dist.clear();
		_m(num,0);
		scanf("%d",&n);
		int x=0;		
		REP(i,n)
		{
			scanf("%s",temp2);
			REP(j,n) if (temp2[j]=='1') num[i] = j;
			x =  x * 10 + num[i];
		}
		
		queue<int> q;
		q.push(x);
		dist[x] = 0;
		int temp[10];
		
		bool found=true;
		REP(i,n) if (num[i] > i) found = false;
		while (!q.empty() && !found)
		{

			int node = q.front();q.pop();
			int cost = dist[node];	
			int xx = node;		
			REP(i,n) temp[i] = node%10,node/=10;
			reverse(temp,temp+n);
			REP(i,n)
			{
				if (i > 0) 
				{
					swap(temp[i],temp[i-1]);
					bool valid = true;
					int x=0;
					REP(j,n) {if (temp[j] > j) valid = false;x = x*10 + temp[j];}
					if (valid)
					{
						res = cost+1;
						found = 1;
						break;
					}
					if (dist.count(x)==0)
					{
						dist[x] = cost+1;
						q.push(x);	
					}
					swap(temp[i],temp[i-1]);
				}	
			}
		}
		
		fprintf(stderr,"Case #%d: %d\n",__+1,res);
		printf("Case #%d: %d\n",__+1,res);
	}
	return 0;	
}
