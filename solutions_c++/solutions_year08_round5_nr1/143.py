#include <stdio.h>
#include <string.h>
#include <math.h>
#include <string>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>

using namespace std;

const int maxn = 10000;
const double eps = 1e-10;
const double pi = 2.0*acos(0.0);
const int INF = 1000000000;

#define sqr(a) ((a)*(a))
#define nul(a) memset(a,0,sizeof(a))
#define fill(a,b) memset(a,b,sizeof(a))

int xsegmin[maxn],xsegmax[maxn],ysegmin[maxn],ysegmax[maxn];

const int dx[4] = {0,1,0,-1};
const int dy[4] = {1,0,-1,0};
int n;
int s;
int maxc = 4010;
void init(){
	s = 0;
	int i;
	for (i = 0 ; i<maxn ; i++){
		xsegmin[i] = INF;
		xsegmax[i] = -INF;
		ysegmin[i] = INF;
		ysegmax[i] = -INF;
	}/*
	fill(xsegmin,INF);
	fill(ysegmin,INF);
	fill(xsegmax,-INF);
	fill(ysegmax,-INF);*/
	scanf("%d",&n);
	
	int tekx = 3010, teky = 3010;
	int x = maxc,y = maxc;
	char teks[100];
	int num;
	int dir = 0;
	for (i = 0 ; i<n ; i++){
		scanf("%s",teks);
		scanf("%d",&num);
		int j;
		for (j = 0 ; j<num ; j++){
			int l = strlen(teks);
			int k;
			for (k = 0 ; k<l ; k++){
				if (teks[k]=='F'){
					int nx = x+dx[dir];
					int ny = y+dy[dir];
					if (x==nx){
						ysegmin[min(y,ny)] = min(ysegmin[min(y,ny)],x);
						ysegmax[min(y,ny)] = max(ysegmax[min(y,ny)],x);
					} else{
						xsegmin[min(x,nx)] = min(xsegmin[min(x,nx)],y);
						xsegmax[min(x,nx)] = max(xsegmax[min(x,nx)],y);
					}
					s+=(x*ny-y*nx);
					x = nx;
					y = ny;
				}
				if (teks[k]=='L')
					dir = (dir-1+4)%4;
				if (teks[k]=='R')
					dir = (dir+1)%4;
			}
		}
	}
	if (s<0)
		s = -s;
	s/=2;
}

void solve(){
	int i,j,res = 0;
	for (i = 0 ; i<=maxc+3010 ; i++){
		for (j = 0 ; j<=maxc+3010; j++){
			if (ysegmin[j]<=i && ysegmax[j]>=i+1 || xsegmin[i]<=j && xsegmax[i]>=j+1)
				res++;
		}
	}
	printf("%d",res-s);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	int i;
	for (i = 1 ; i<=t ; i++){
		printf("Case #%d: ",i);
		init();
		solve();
		printf("\n");
	}
	return 0;
}