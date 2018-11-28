#include <cstdio>
#include <cmath>
#include <cstring>
#include <memory.h>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
using namespace std;
const int maxn=401;
int n,m;
int head,tail;
bool a[maxn][maxn];
int dist[maxn];
int q[maxn];
int sum[maxn][maxn];

void init(){
	scanf("%d%d",&n,&m);
	memset(a,false,sizeof(a));
	for (int i=0;i<m;i++){
		int st,en;
		scanf("%d,%d",&st,&en);
		a[st][en]=a[en][st]=true;
	}
	return;
}

void bfs(){
	head=0;
	tail=1;
	memset(dist,0xff,sizeof(dist));
	dist[0]=0;
	q[tail]=0;
	while (1){
		head++;
		if (head>tail){
			break;
		}
		int cur=q[head];
		int curdist=dist[cur]+1;
		for (int i=0;i<n;i++){
			if (!a[cur][i]){
				continue;
			}
			if (dist[i]>=0){
				continue;
			}
			dist[i]=curdist;
			tail++;
			q[tail]=i;
		}
	}
	printf("%d ",dist[1]-1);
	return;
}

int neighbour(int x,int y){
	int ans=0;
	if (y==1){
		for (int i=0;i<n;i++){
			if (i==x){
				continue;
			}
			if (i==y){
				continue;
			}
			if (dist[i]!=dist[1]){
				continue;
			}
			if (!a[x][i]){
				continue;
			}
			ans++;
		}
		return ans;
	}
	for (int i=0;i<n;i++){
		if (i==x){
			continue;
		}
		if (i==y){
			continue;
		}
		if (dist[i]!=dist[y]){
			continue;
		}
		if ((!a[x][i])&&(!a[y][i])){
			continue;
		}
		ans++;
	}
	return ans;
}

int count(int x,int y,int k){
	int ans=0;
	if (k==1){
		for (int i=0;i<n;i++){
			if (i==x){
				continue;
			}
			if (i==y){
				continue;
			}
			if (dist[i]!=dist[y]){
				continue;
			}
			if ((!a[x][i])&&(!a[y][i])){
				continue;
			}
			ans++;
		}
		return ans;
	}
	for (int i=0;i<n;i++){
		if (i==x){
			continue;
		}
		if (i==y){
			continue;
		}
		if (dist[i]!=dist[y]){
			continue;
		}
		if ((!a[x][i])&&(!a[y][i])&&(!a[k][i])){
			continue;
		}
		ans++;
	}
	return ans;
}

int process(){
	memset(sum,0xff,sizeof(sum));
	for (int i=0;i<n;i++){
		if (a[i][1]&&(dist[i]==(dist[1]-1))){
			sum[i][1]=neighbour(i,1)+1;
		}
	}
	for (int i=tail;i>=1;i--){
		int cur=q[i];
		for (int j=0;j<n;j++){
			if (dist[j]==(dist[cur]-1)){
				if (a[j][cur]){
					for (int k=0;k<n;k++){
						if (sum[cur][k]>=0){
							sum[j][cur]=max(sum[j][cur],sum[cur][k]+count(j,cur,k));
						}
					}
				}
			}
		}
	}
	int ans=0;
	for (int i=0;i<n;i++){
		if (sum[0][i]<0){
			continue;
		}
		ans=max(ans,sum[0][i]+neighbour(i,0));
	}
	return ans;
}

int main(){
	int tcase;
	scanf("%d",&tcase);
	for (int i=1;i<=tcase;i++){
		init();
		printf("Case #%d: ",i);
		bfs();
		printf("%d\n",process());
	}
	return 0;
}
