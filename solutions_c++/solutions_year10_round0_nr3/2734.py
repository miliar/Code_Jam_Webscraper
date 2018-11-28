#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <cstdlib>
#include <stdlib.h>
#include <stack>
#include <cstdio>
#include <map>
#include <cmath>
#include <time.h>
using namespace std;

#define MAX(a,b) ((a>=b)?a:b)
#define MIN(a,b) ((a<=b)?a:b)
#define ABS(a) ((a<0)?-(a):a)

queue<int> q;
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int T,r,k,n,a,count;
	long long res,now;
	scanf("%d",&T);
	for(int t=0;t<T;++t)
	{
		scanf("%d %d %d",&r,&k,&n);
		while(!q.empty())q.pop();
		for(int i=0;i<n;++i){scanf("%d",&a); q.push(a);}
		res=0;
		for(int i=0;i<r;++i)
		{
			now=count=0;
			while(now+q.front()<=k && count<n){++count; now+=q.front(); res+=q.front(); q.push(q.front()); q.pop();}
		}
		printf("Case #%d: ",t+1);
		cout <<res <<"\n";
	}
	return 0;
}