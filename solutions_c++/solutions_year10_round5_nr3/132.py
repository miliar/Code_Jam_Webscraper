#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#define INF (1<<30)
#define EPS 1e-8
#define LLD long long int
using namespace std;

struct dat{
	int x,y;
	dat(){}
	dat(int x,int y):x(x),y(y){}
	bool operator < (dat const &T) const{return y<T.y;}
}   t;

int n,p[4000005],c,AC;
priority_queue<dat> q;

int main(){
	scanf("%d",&c);
	for (int tc=1;tc<=c;tc++){
		scanf("%d",&n);
		memset(p,0,sizeof(p));
		while (n--){
			scanf("%d%d",&t.x,&t.y);
			t.x+=2000000;
			p[t.x]+=t.y;
			q.push(t);
		}
		AC=0;
		while (!q.empty()){
			t=q.top();
			q.pop();
			if (t.y<=1) break;
			if (p[t.x]<=1) continue;
			AC++;
			p[t.x-1]++;
			p[t.x+1]++;
			p[t.x]-=2;
			
			if (p[t.x-1]>1) q.push(dat(t.x-1,p[t.x-1]));
			if (p[t.x]>1) q.push(dat(t.x,p[t.x]));
			if (p[t.x+1]>1) q.push(dat(t.x+1,p[t.x+1]));
			
		}
		while (!q.empty()) q.pop();
		printf("Case #%d: %d\n",tc,AC);
	}
	return 0;
}
