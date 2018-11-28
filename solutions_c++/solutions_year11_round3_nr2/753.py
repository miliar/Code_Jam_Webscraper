#include <functional>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <string>
#include <vector>
#include <cstdio>
#include <bitset>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;
typedef unsigned long long uint64;
typedef long long int64;
#define eps 1e-9
#define pi 3.1415926535897932384626433832795
#define MAX 1000005
struct Line
{
	int dist;
	int index;
};

int L,t,N,C;
int dist[MAX],tmp[MAX];
Line ss[MAX];
bool visit[MAX];

bool cmp(Line a,Line b)
{
	if(a.dist==b.dist)
		return a.index<b.index;
	return  a.dist<b.dist;
}

int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("C-large.in","r",stdin);
	//freopen("B-small-attempt0.in","r",stdin);
	//freopen("out.txt","w",stdout);
	int T,testcase=1;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",testcase++);
		scanf("%d%d%d%d",&L,&t,&N,&C);
		Line temp;
		for(int i=1;i<=C;i++)
		{
			scanf("%d",&tmp[i]);
			dist[i]=tmp[i];
			ss[i].dist=tmp[i],ss[i].index=i;
		}
		sort(ss+1,ss+C+1,cmp);
		for(int i=1;i<=N;i++)
		{
		    for(int k=1;k<=C && i*C+k<=N;k++)
			    dist[i*C+k]=tmp[k];
		}
		int sum=0;
		sum=t;
		int last;
		double first=0.5*(t);
		for(last=1;last<=N;last++)
		{
			if(dist[last]>first)break;
			if(dist[last]<=first)first=first-dist[last];
		}
		first=dist[last]-first;
		if(first==0)last--;
		//sum+=first/0.5;
		int num=L;
		memset(visit,0,sizeof(visit));
		bool firstuse=false;
		for(int i=C;i>=0;i--)
		{
			if(first>ss[i].dist)
			{
				sum+=first;firstuse=true;
				num--;
			}
			for(int k=0;k*C+(ss[i].index)<=N;k++)
			{
				if(num==0)break;
				if(k*C+(ss[i].index)<=last)continue;
				num--;
				sum+=dist[k*C+(ss[i].index)];
				visit[k*C+(ss[i].index)]=1;
			}
			if(num==0)break;
		}
		if(!firstuse)sum+=first/0.5;
		num=0;
		for(int i=last+1;i<=N;i++)
			if(!visit[i])num+=dist[i];
		sum+=num*2;
		printf("%d\n",sum);


	}
	return 0;
}