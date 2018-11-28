
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<string>
#include<string.h>
#include<cstring>
#include<stack>
#include<queue>
#include<cassert>
#include<cmath>
using namespace std;

#define LL long long int 
#define PII pair<int,int> 
#define PB push_back
#define MP make_pair
#define INF 1000000000
int a[100][100],R,C;
int chk1(int sx,int sy,int k){
	double cx,cy,sumx=0,sumy=0;
	k--;
	cx=sx+(k-1)/2.0;
	cy=sy+(k-1)/2.0;
	int i,j;
	for(i=sx;i<=sx+k;i++){
		for(j=sy;j<=sy+k;j++){
			if((i==sx &&j==sy )||( i==sx && j==sy+k) ||(i==sx+k && j==sy+k) || (i==sx+k && j==sy))
				continue;
			sumx+=(cx-i+0.5)*(double)a[i][j];
			sumy+=(cy-j+0.5)*(double)a[i][j];
		}	
	}
	if(fabs(sumx-0)<=0.000000001 && fabs(sumy-0)<=0.000000001){
//		printf("%d %d\n",sx,sy);
		return 1;
	}
	return 0;
}
int chk(int k){
	int i,j;
	for(i=1;i<=R-k+1;i++){
		for(j=1;j<=C-k+1;j++){
			if(chk1(i,j,k)==1)
				return 1;
		}
	}
	return 0;
}
int main(){
	int test,t,i,j,k,D;
	scanf("%d",&test);
	for(t=1;t<=test;t++){
		scanf("%d %d %d ",&R,&C,&D);
		for(i=1;i<=R;i++)
			for(j=1;j<=C;j++)
				scanf(" %c",&a[i][j]);
		for(i=1;i<=R;i++)
			for(j=1;j<=C;j++)
				a[i][j]-='0';
		int ans=-1;
		for(k=3;k<=min(R,C);k++)
			if(chk(k)==1)
				ans=k;
		printf("Case #%d: ",t);
		if(ans==-1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",ans);
	}
	return 0;
}
