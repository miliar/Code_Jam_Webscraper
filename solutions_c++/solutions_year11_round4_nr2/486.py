#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<cmath>
using namespace std;

#define F(i,n) for(i=0;i<n;i++)
#define FF(i,n) for(i=1;i<=n;i++)
#define LL __int64
#define min(a, b) (a<b?a:b)

int a[505][505], R, C,D;

int b[505][505], c[505][505], bb[505][505], ff[505][505], gg[505][505];

void inz(){
	int i, j;
	// sum	
	FF(i,R){
		// b[i][j] = a[i][0]+...+a[i][j]
	    b[i][0] = 0;
	    FF(j,C) b[i][j] = b[i][j-1] + a[i][j];
	}
	FF(i,C){
		// c[i][j] = a[0][j]+...+a[i][j]
	    c[0][i] = a[0][i];
	    FF(j,R) c[j][i]= c[j-1][i]+a[j][i];
	}
	//v-sum
	F(i,505)ff[0][i] = gg[i][0] = 0;
	
	FF(i,R){
		FF(j,C){
			bb[i][j] = bb[i-1][j] + b[i][j];
			ff[i][j] = ff[i-1][j] + b[i][j]*i;
			gg[i][j] = gg[i][j-1] + c[i][j]*j;
		}
	}
	
}

bool fit(int x, int y, int k){
	int i, j, ss;
	// i sum
	i = bb[x][y]-bb[x-k][y]-bb[x][y-k]+bb[x-k][y-k];
	i -= a[x][y] + a[x-k+1][y] + a[x][y-k+1] + a[x-k+1][y-k+1];
	// j v-R-sum
	j = ff[x][y]-ff[x-k][y]-ff[x][y-k]+ff[x-k][y-k];
	j -= a[x][y]*x + a[x-k+1][y]*(x-k+1) + a[x][y-k+1]*x + a[x-k+1][y-k+1]*(x-k+1);
	if( j*2!=i*(x + x-k+1) )return false; 
	// ss v-C-sum
	ss = gg[x][y]-gg[x-k][y]-gg[x][y-k]+gg[x-k][y-k];
	ss -= a[x][y]*y + a[x-k+1][y]*y + a[x][y-k+1]*(y-k+1) + a[x-k+1][y-k+1]*(y-k+1);
	if( ss*2!=i*(y+y-k+1) )return false;
	return true;
}

int main(){
     int i, j, T, TT=1, sum, ans, k;
     freopen("B-large.in","r", stdin);
     freopen("B.out", "w", stdout);
     scanf("%d",&T);
     while(T--){
          scanf("%d%d%d",&R,&C,&D);
          FF(i,R)FF(j,C){
			char str;
			scanf(" %c", &str);
			a[i][j] = str - '0';
		}
//		R++, C++;
		inz();
		ans = 2;
		for(i=3;i<=R;i++){
			for(j=3;j<=C;j++){
				for(k=min(i,j);k>ans;k--){
		//			printf("%d\n",k);
					if(fit(i,j,k)){
//						cout<<i<<' '<<j<<' '<<k<<endl;
						ans = k;
						break;
					}
				}
		//		printf("%d %d\n", i,j);
			}
		}
		if(ans>=3)printf("Case #%d: %d\n", TT++, ans);
		else printf("Case #%d: IMPOSSIBLE\n", TT++);
		
	}
     
     return 0;
}
