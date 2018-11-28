#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<string>
#include<set>
#include<map>
#include<vector>
#include<algorithm>
#include<sstream>
#include<stack>
#include<queue>
#include<deque>
#include<iostream>
using namespace std;
#define sz(X) (int)X.size()
#define mp(X,Y) make_pair(X,Y)
#define pb(X) push_back(X)
#define clr(X) memset(X,0,sizeof(X))
#define klr(X) memset(X,-1,sizeof(X))
#define ll long long
#define pii pair<int,int>

struct circle{
	double r;
	int idx;
} v[1010];

int n;
double W,L;
double x[1010],y[1010], r[1010];


double dist(int i, int j){
	return (x[i]-x[j])*(x[i]-x[j]) + (y[i]-y[j])*(y[i]-y[j]);
}

bool cmp(circle a, circle b){
	if(a.r != b.r)
		return a.r > b.r;
	return a.idx < b.idx;
}


int main(){
	int t;
	scanf("%d",&t);
	for(int caso=1;caso<=t;caso++){
		printf("Case #%d: ",caso);
		scanf("%d",&n);
		scanf("%lf %lf",&W,&L);
		for(int i=0;i<n;i++){
			scanf("%lf",&v[i].r);
			r[i] = v[i].r;
			v[i].idx = i;	
		}
		sort(v,v+n, cmp);
		int i;
		
		if(W>=L){
		x[v[0].idx]=0.0;
		y[v[0].idx]=0.0;
		for(i=1;i<n;i++){
			double next = x[v[i-1].idx]  + v[i-1].r + v[i].r +1e-8;
			if(next<W){
				x[v[i].idx] = next;
				y[v[i].idx] = 0.0;
			}
			else break;
		}
		x[v[i].idx] = W;
		y[v[i].idx] = L;
		i++;
		for(;i<n;i++){
			double next = x[v[i-1].idx] - v[i-1].r -v[i].r  -1e-8;
			if(next>0.0){
				x[v[i].idx] = next;
				y[v[i].idx] = L;
			}
			else break;
		}
		}
		else{
			x[v[0].idx]=0.0;
			y[v[0].idx]=0.0;
				for(i=1;i<n;i++){
				double next = y[v[i-1].idx]  + v[i-1].r + v[i].r +1e-8;
				if(next<L){
					x[v[i].idx] = 0.0;
					y[v[i].idx] = next;
				}
				else break;
			}
		x[v[i].idx] = W;
		y[v[i].idx] = L;
		i++;
		for(;i<n;i++){
			double next = y[v[i-1].idx] - v[i-1].r -v[i].r  -1e-8;
			if(next>0.0){
				x[v[i].idx] = W;
				y[v[i].idx] = next;
			}
			else break;
		}
		}
		
		if(i<n)
		random_shuffle(v+i,v+n);
		for(;i<n;i++){
			while(1){
				x[v[i].idx] = (1.0*rand()/RAND_MAX)*W;
				y[v[i].idx] = (1.0*rand()/RAND_MAX)*L;
				int j;
				for(j=0;j<i;j++){
					if(dist(v[i].idx,v[j].idx) <= (v[i].r + v[j].r)*(v[i].r+v[j].r) + 1e-8)
						break;
				}
				if(j==i)break;
			}
		}
		
		/*
		for(i=0;i<n;i++){
				if(x[i] <0.0 || x[i] > W || y[i]<0.0 || y[i]>L){
					printf("BUG\n");
					exit(1);
				}
				for(int j=0;j<i;j++){
					if(dist(i,j) <= (r[i] + r[j])*(r[i] + r[j]) + 1e-8){
							printf("BUG\n");
							exit(1);
						}
				}
		}*/
		
		for(int i=0;i<n;i++)
			printf(" %.10f %.10f",x[i],y[i]);
		printf("\n");
	}
	return 0;
}
