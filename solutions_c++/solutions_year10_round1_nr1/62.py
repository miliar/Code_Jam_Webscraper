#include <iostream>
#include <string>
#include <cstring>
#include <string.h>
#include <algorithm>
#include <set>
#include <map>
#include <vector>

using namespace std;

int a[60][60];
int b[60][60];
int c[60][60];
int v[60];
int n,k;
int dx[]={1,1,-1,-1,1,-1,0,0};
int dy[]={-1,1,1,-1,0,0,1,-1};

int solve(int x){
	int mx=0;
	for (int i=1; i<=n; i++)
		for (int j=1; j<=n; j++)
		if (c[i][j]==x){
			for (int l=0; l<8; l++){
				int tk=1;
				int tx=i+dx[l], ty=j+dy[l];
				while (c[tx][ty]==x){
					tk++;
					tx+=dx[l], ty+=dy[l];
				}
				mx=max(mx,tk);
			}
		}
	return mx;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	scanf("%d\n",&t);

	for (int tt=1; tt<=t; tt++){
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		memset(c,0,sizeof(c));
		memset(v,0,sizeof(v));
		scanf("%d%d\n",&n,&k);
		char q;
		for (int i=1; i<=n; i++){
			for (int j=1; j<=n; j++){
				scanf("%c",&q);
				if (q=='.') a[i][j]=0; else
					if (q=='R') a[i][j]=1; else
						a[i][j]=2;
			}
			scanf("\n");
		}

		int x=0, y=0;
		for (int i=1; i<=n; i++)
			for (int j=1; j<=n; j++)
				b[i][j]=a[n+1-j][i];	

		for (int i=1; i<=n; i++)
			for (int j=n; j>=1; j--){
				if (b[j][i]!=0){
					v[i]++;
					c[n+1-v[i]][i]=b[j][i];
				}
			}

		x=solve(1);
		y=solve(2);
			
		printf("Case #%d: ",tt);
		if (x>=k&&y>=k) printf("Both\n"); else
			if (x<k&&y<k) printf("Neither\n"); else
				if (x>=k) printf("Red\n"); else
					printf("Blue\n");
	}

	return 0;
}