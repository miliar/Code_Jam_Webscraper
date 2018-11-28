#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <cctype>
#include <fstream>
#include <numeric>
#include <map>
#include <iterator>
#include <cstdlib>
#include <cstdio>
using namespace std;

#define INF 99999999
#define EPS 1e-7
#define MIN(a,b) ((a)<(b))?(a):(b)
#define MAX(a,b) ((a)>(b))?(a):(b)
#define REP(i,n) for(i=0; i<(n); i++)
#define FOR(i,a,b) for(i=(a); i<=(b); i++)
#define SET(t,v) memset((t), (v), sizeof(t))
#define sz size()
#define pb push_back
#define i64 long long
#define ALL(x) x.begin(), x.end()


#define SIZE 1000+10

#define IO freopen("C-large.in","r",stdin); freopen("C-large.out","w",stdout);


i64 T,N,R,k;
i64 grp[SIZE],E[SIZE],path[SIZE];
bool visited[SIZE];


int main()
{
	IO
	i64 tc,i,j,sum,buffer,earn,cnt,gc,nn; 
	scanf("%lld",&T);
	for(tc=1;tc<=T;tc++)
	{
		scanf("%lld %lld %lld",&R,&k,&N);
		sum=0;
		for(i=0;i<N;i++)
		{
			scanf("%lld",&grp[i]);
			sum += grp[i];
		}
		j=0;		//path index
		earn=0;		//total earning
		cnt=0;		//rounds count
		memset(visited,0,sizeof(visited));
		memset(E,0,sizeof(E));
		i=0;		//curent index of groups
		nn=N;		//number of goups available
		while(cnt<R && !visited[i])		//till no cycle
		{
			E[i] = earn;			//total earnings before ith group(start)
			path[j++] = i;			//mremember the path
			//printf("i: %d ",i);	
			visited[i] = true;
			buffer=0;				//buffer for one round
			gc=0;					//group count
			while(gc<=nn && buffer <=k)		//till available groups
			{
				buffer += grp[i];
				i=(i+1)%N;
				gc++;
			}
			i = (i+N-1)%N;			//fix extra iteration
			buffer -= grp[i];		//fix buffer
			//printf("buffer: %d\n",buffer);
			earn += buffer;			
			cnt++;
			nn += gc;
		}

		if(cnt<R)		//if cycle found on ith group(start)
		{
			int t=0,z;
			for(z=0;path[z]!=i;z++)
				t++;	//number of nodes before cycle start
			R -= t;
			cnt -= t;
			earn = E[i] + (R/cnt)*(earn-E[i]);		//earnings in full cycles
			cnt = R - R%cnt;
			//printf("earn: %d, cnt: %d, i:%d\n",earn,cnt,i);
			
			memset(visited,0,sizeof(visited));
			while(cnt<R && !visited[i])		//earning in fractional cycle
			{
				visited[i] = true;
				buffer=0;
				gc=0;
				while(gc<=nn && buffer <=k)
				{
					buffer += grp[i];
					i=(i+1)%N;
				}
				i = (i+N-1)%N;
				buffer -= grp[i];
				//printf("buffer: %d\n",buffer);
				earn += buffer;
				cnt++;
				nn += gc;
			}
		}
		
		printf("Case #%lld: %lld\n",tc,earn);
	}
	return 0;
}

