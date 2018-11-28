#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <queue>

using namespace std;

#define EPS 1e-10
#define PI acos(-1)

long long g[2010], sum[2010], total,c,times,res,acc,r,k,n,tmp;
int t,cn,now,first;
queue<int> q;


void process() {
	scanf("%lld %lld %lld",&r,&k,&n);
	sum[0]=0;
	
	while (!q.empty()) q.pop();
	
	for (int i=0; i<n; ++i) {
		scanf("%lld",&g[i]);
		g[n+i]=g[i];
		q.push(i);
		sum[i+1]=sum[i]+g[i];
	}
	
	t=0;
	c=0;
	total=0;
	times=0;
	res=0;
	first=true;
	
	if (sum[n]<=k) {
		c=sum[n];
		printf("Case #%d: %lld\n",++cn,(c*r));
		return;
	}
	
	
	while (times<r) {
		now = q.front();
		if (now==0) {
			if (first) first=false;
			else break;
		}
		q.pop();
		q.push(now);
		acc=g[now];
		++times;
		while (acc<=k) {
			t = q.front();
			if (now==t) break;
			if (acc+g[t]<=k) {
				acc += g[t];
				q.pop();
				q.push(t);
			} else {
				break;
			}
		}
		
		c+=acc;
	}
	
	tmp = r/times;
	res = c*tmp;
	r = r%tmp;
	c=0;
	first=true;
	times=0;
	
	while (times<r) {
		now = q.front();
		if (now==0) {
			if(first) first=false;
			else break;
		}
		q.pop();
		q.push(now);
		acc=g[now];
		++times;
		while (acc<=k) {
			t = q.front();
			if (now==t) break;
			if (acc+g[t]<=k) {
				acc += g[t];
				q.pop();
				q.push(t);
			} else {
				break;
			}
		}
	
		res+=acc;
	}
	printf("Case #%d: %lld\n",++cn,res);
	
	fflush(stdout);
}

int main() {
	freopen("out","w",stdout);
	int cases;
	cn=0;
	scanf("%d",&cases);
	
	while (cases--) process();

	return 0;
}
