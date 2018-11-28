#include <iostream>
#include <vector>
#include <cstdio>
#include <set>
#include <algorithm>
#define ST first
#define ND second
#define MP make_pair
#define PB push_back
using namespace std;
typedef long long int lld;
typedef double lf;

using namespace std;
int del,ins,M,n,t,mini[260][260],res[260][260],T[260],wyn,tt;
int main(){
	scanf("%d",&t);
	while(t--){
		scanf("%d %d %d %d",&del,&ins,&M,&n);
		for(int i=1;i<=n;i++)
			scanf("%d",&T[i]);
		for(int i=0;i<=255;i++){
			res[1][i]=ins+del;
			res[1][i]=min(res[1][i],abs(T[1]-i));
		}
		for(int a=0;a<=255;a++){
			mini[a][a]=res[1][a];
			for(int b=a+1;b<=255;b++)
				mini[a][b]=min(res[1][b],mini[a][b-1]);
		}
/*
		for(int i=0;i<=255;i++){
			wyn=min(wyn,res[1][i]);
			printf("%d %d\n",i,res[1][i]);
		}
		system("pause");
*/
		for(int j=0;j<=255;j++)
			for(int k=1;k<=255;k++)
				res[1][j]=min(res[1][j],k*ins+mini[max(0,j-M*(k+0))][min(255,j+M*(k+0))]);
//		for(int i=0;i<=255;i++){
//			wyn=min(wyn,res[n][i]);
//			printf("%d %d\n",i,res[1][i]);
//		}
//		system("pause");
		
			for(int a=0;a<=255;a++){
				mini[a][a]=res[1][a];
				for(int b=a+1;b<=255;b++)
					mini[a][b]=min(res[1][b],mini[a][b-1]);
			}
		for(int i=2;i<=n;i++){
			for(int j=0;j<=255;j++){
				res[i][j]=res[i-1][j]+del;
				res[i][j]=min(res[i][j],abs(T[i]-j)+mini[max(0,j-M)][min(255,j+M)]);
			}
			for(int a=0;a<=255;a++)
				for(int b=0;b<=255;b++)
					mini[a][b]=2000000000;
			for(int a=0;a<=255;a++){
				mini[a][a]=res[i][a];
				for(int b=a+1;b<=255;b++)
					mini[a][b]=min(res[i][b],mini[a][b-1]);
			}
//			for(int q=0;q<=255;q++){
//				wyn=min(wyn,res[i][q]);
//				printf("%d %d\n",q,res[i][q]);
//			}
//			system("pause");
			for(int j=0;j<=255;j++)
				for(int k=1;k<=255;k++)
					res[i][j]=min(res[i][j],k*ins+mini[max(0,j-M*(k+0))][min(255,j+M*(k+0))]);
			
//			for(int q=0;q<=255;q++){
//				wyn=min(wyn,res[i][q]);
//				printf("%d %d\n",q,res[i][q]);
//			}
//			system("pause");
			
			for(int a=0;a<=255;a++){
				mini[a][a]=res[i][a];
				for(int b=a+1;b<=255;b++)
					mini[a][b]=min(res[i][b],mini[a][b-1]);
			}
		}
		wyn=2000000000;
		for(int i=0;i<=255;i++){
			wyn=min(wyn,res[n][i]);
//			printf("%d %d\n",i,res[n][i]);
		}
		tt++;
		printf("Case #%d: %d\n",tt,wyn);
	}
}
