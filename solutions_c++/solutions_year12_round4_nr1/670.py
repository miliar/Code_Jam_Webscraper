#include <stdio.h>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <stdio.h>
#include <sstream>
#include <string>
#include <string.h>
#include <vector>
#include <queue>
#include <math.h>
#include <map>
#define MaxLength INT_MAX
#define MaxNode 12
#define MN 10005
using namespace std;

int D,T,N,H;
int d[MN],l[MN];
int vis[MN];
bool bfs(){
	int i,j,k, len;
	queue<pair<int, int> > q;
	while(!q.empty())
		q.pop();
	q.push(make_pair(0,d[0]));
	vis[0] = d[0];

	while(!q.empty()){
		i = q.front().first;
		len = q.front().second;
		q.pop();

		if(D-d[i]<=len)
			return true;
		for(j=0; j<N; j++)
			if(j != i && (k = fabs(double(d[i]-d[j])))<=len && k>vis[j]){
				k = min(k,l[j]);
				q.push(make_pair(j,k));
				vis[j] = k;
			}
	}
	return false;
}
int main(){
	int i,j,k,tt,a,b;
	scanf("%d",&T);
	for(tt=1; tt<=T;tt++){
		memset(vis,0,sizeof(vis));

		scanf("%d",&N);
		for(i=0; i<N ;i++)
			scanf("%d %d",&d[i], &l[i]);
		scanf("%d",&D);


		if(bfs())
			printf("Case #%d: YES\n",tt);
		else
			printf("Case #%d: NO\n",tt);
	}
	return 0;
}
