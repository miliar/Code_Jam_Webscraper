#include <iostream>
#include <cstdio>

using namespace std;
int v[40],g[40];
int main()
{
	freopen("input1.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,i;
	int K,n;
	scanf("%d",&T);
	for(i=1;i<=T;i++){
		scanf("%d%d",&n,&K);
		if(K==0){
			printf("Case #%d: OFF\n",i);	continue;}
		if(n==1){
			if(K%2==1)printf("Case #%d: ON\n",i);
			else printf("Case #%d: OFF\n",i);continue;	}
		int k,j;
		memset(g,0,40);
		memset(v,0,40);
		v[0]=1;g[0]=1;
		for(k=1;k<=K;k++){
			for(j=1;j<=n;j++)
				if((g[j-1])||g[j])v[j]=v[j]?0:1;
			for(j=1;j<=n;j++)
				g[j]=(g[j-1]&&v[j]);
		}
		if(g[n])printf("Case #%d: ON\n",i);
			else printf("Case #%d: OFF\n",i);
	}
	return 0;
}
