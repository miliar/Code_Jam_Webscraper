#include <stdio.h>
#include <algorithm>
using namespace std;

#define INF 999999999

int x1[2000],x2[2000],y1[2000],y2[2000];

int check[2000];

int maxx,maxy,minsum;
int n;


void saiki(int p){
	if(check[p]==1)return;
	check[p]=1;
	maxx=max(maxx,x2[p]);
	maxy=max(maxy,y2[p]);
	minsum=min(minsum,x1[p]+y1[p]);
	for(int i=0;i<n;i++){
		if(x2[i]<x1[p]-1)continue;
		if(x2[p]<x1[i]-1)continue;
		if(y2[i]<y1[p]-1)continue;
		if(y2[p]<y1[i]-1)continue;
		saiki(i);
	}
}

main(){
	int tests;
	scanf("%d",&tests);
	for(int t=1;t<=tests;t++){
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			scanf("%d%d%d%d",&x1[i],&y1[i],&x2[i],&y2[i]);
		}
		for(int i=0;i<n;i++)check[i]=0;
		int ans=0;
		for(int i=0;i<n;i++){
			if(check[i]==0){
				minsum=INF;
				maxx=-INF;
				maxy=-INF;
				saiki(i);
				ans=max(ans,(maxx+maxy)-minsum+1);
			}
		}
		printf("Case #%d: %d\n",t,ans);
	}
}