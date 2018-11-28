#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

#define INF 1000000

int c[2001];
int malt[2][2001][2001];
int flag[2001];

int main(){
	int i,j,n,m,a,b,t,u,label=0,q,pat;
	cin>>t;
	for (u=0; u<t; u++)	{
		cin>>n>>m;
		for (i=0; i<m; i++){
			cin>>q;
			for (j=0; j<q; j++){
				cin>>a>>b;
				malt[b][a-1][i]=u+1;
			}
		}
		int minmc=INF;//1000000;
		int mc,minpat;
		for (pat=0; pat<(1<<n); pat++){
			label++;
			mc=0;
			int happy=0;
			for (i=0; i<n; i++){
				q=(pat>>i)&1;
				if (q) mc++;
				for (j=0; j<m; j++){
					if (malt[q][i][j]==u+1){
						if (flag[j]!=label){
							happy++;
							flag[j]=label;
						}
					}
				}
			}
			if (happy==m && mc<minmc){
				minmc=mc;
				minpat=pat;
			}
		}
		printf("Case #%d:",u+1);
		if (minmc==INF)
			printf(" IMPOSSIBLE\n");
		else{
			for (i=0; i<n; i++){
				q=(minpat>>i)&1;
				printf(" %d",q);
			}			
			printf("\n");
		}
	}
	return 0;
}