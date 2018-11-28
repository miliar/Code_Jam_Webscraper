
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cassert>
using namespace std;

int main(){
	int nn;scanf("%d",&nn);
	for(int npr=1;npr<=nn;npr++){
		int n;scanf("%d",&n);
		int m=2*n-1;
		int v[m][m];memset(v,-1,sizeof(v));

		int sta[m],end[m];
		for(int i=0;i<n;i++){
			sta[i]=n-1-i;
			end[i]=sta[i]+2*i;
		}
		for(int i=0;i<n-1;i++){
			sta[n+i]=i+1;
			end[n+i]=sta[n+i]+(m-1-2*i-2);
		}

		for(int i=0;i<m;i++)for(int k=sta[i];k<=end[i];k+=2)scanf("%d",v[i]+k);

		int ans=1000*1000*1000;
		for(int i=0;i<=m+1;i++)for(int k=0;k<=m+1;k++){
			int cand=0;
			int ng=0;
			for(int s=0;ng==0 && s<m;s++)for(int t=sta[s];ng==0 && t<=end[s];t+=2){
				assert(v[s][t]!=-1);
				int dx=s-i;
				int dy=t-k;

				int dist=abs(dx)+abs(dy);
				cand=max(cand,(dist+1)*(dist+1));
				if(ans<=cand){ng=1;continue;}

				const int sx[4]={1,1,-1,-1};
				const int sy[4]={1,-1,1,-1};
				for(int p=0;ng==0 && p<4;p++){
					int xx=i+dx*sx[p];
					int yy=k+dy*sy[p];
					if(0<=xx && xx<m && sta[xx]<=yy && yy<=end[xx]){
						assert(v[xx][yy]!=-1);
						if(v[s][t]!=v[xx][yy]){ng=1;continue;}
					}
				}
			}
			if(ng==0)ans=min(ans,cand);
		}

		printf("Case #%d: %d\n",npr,ans-n*n);
	}
	return 0;
}
