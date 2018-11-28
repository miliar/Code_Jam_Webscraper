#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <queue>
#include <set>
using namespace std;
#define INF 1010101010

int edg[410][410];
int vpt[410];
int kaburi[410][410];
int dp[410][410];
int kab3[410][410][410]; //for small

set<int> cov[410];

main(){
	int datasuu;
	scanf("%d ",&datasuu);
	for(int casenum=1;casenum<=datasuu;casenum++){
		printf("Case #%d: ",casenum);
		
		int n,m;
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++)for(int j=0;j<n;j++)edg[i][j]=0;
		//for(int i=0;i<n;i++)for(int j=0;j<n;j++)kaburi[i][j]=0;
		//for(int i=0;i<n;i++)vpt[i]=0;
		for(int i=0;i<n;i++)for(int j=0;j<n;j++)dp[i][j]=-1;

		for(int i=0;i<m;i++){
			int a,b;
			scanf("%d,%d",&a,&b);
			edg[a][b]=edg[b][a]=1;
		}
		
		//haba
		int dist[410];
		queue<int> que;
		que.push(1);
		for(int i=0;i<n;i++)dist[i]=INF;
		dist[1]=0;
		while(!que.empty()){
			int p=que.front();
			que.pop();
			for(int q=0;q<n;q++){
				if(edg[p][q]==1){
					if(dist[q]>dist[p]+1){
						dist[q]=dist[p]+1;
						que.push(q);
					}
				}
			}
		}
		printf("%d ",dist[0]-1);
		
		for(int i=0;i<n;i++){
			vpt[i]=0;
			for(int j=0;j<n;j++){
				if(i!=1 && (i==j || edg[i][j]==1))vpt[i]++;
			}
		}
		for(int i=0;i<n;i++)for(int j=0;j<n;j++){
//			if(edg[i][j]==1){
			if(dist[j]==dist[i]-1 || dist[j]==dist[i]-2){
				kaburi[i][j]=0;
				if(i==1 || j==1)continue;
				for(int k=0;k<n;k++){
					if(i!=1 && (i==k || edg[i][k]==1)){
					if(j!=1 && (j==k || edg[j][k]==1)){
						kaburi[i][j]++;
					}
					}
				}
			}
		}
		for(int i=0;i<n;i++)for(int j=0;j<n;j++)for(int k=0;k<n;k++){
			if(dist[j]==dist[i]-1 && dist[k]==dist[j]-1 && edg[i][j]==1 && edg[j][k]==1){
				kab3[i][j][k]=0;
				if(i==1 || j==1 || k==1)continue;
				for(int l=0;l<n;l++){
					if(i!=1 && (i==l || edg[i][l]==1)){
					if(j!=1 && (j==l || edg[j][l]==1)){
					if(k!=1 && (k==l || edg[k][l]==1)){
						kab3[i][j][k]++;
					}
					}
					}
				}
			}
		}
		//for(int i=0;i<n;i++)printf("%d:d=%d vpt=%d\n",i,dist[i],vpt[i]);
		
		vector<pair<int,int> > hoge;
		for(int i=0;i<n;i++)hoge.push_back(make_pair(dist[i],i));
		sort(hoge.begin(),hoge.end());
		for(int i=0;i<hoge.size();i++){
			int p=hoge[i].second;
			if(dist[p]==INF)break;
			if(p==1)continue;
			if(dist[p]==1){
				dp[p][1]=vpt[p];
			}else{
				for(int q=0;q<n;q++){
					if(dist[q]<dist[p] && edg[p][q]==1){
						for(int r=0;r<n;r++){
							if(dist[r]<dist[q] && edg[q][r]==1){
								dp[p][q]=max(dp[p][q],dp[q][r]+vpt[p]-kaburi[p][q]-kaburi[p][r]+kab3[p][q][r]);
							}
						}
					}
				}
			}
		}
		//for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(dp[i][j]!=-1)printf(" dp[%d][%d]==%d\n",i,j,dp[i][j]);
		/*
		for(int d=1;d<=dist[0];d++){
			for(int i=0;i<n;i++){
				if(dist[i]==d){
					if(d==1)dp[i]=vpt[i];
					for(int j=0;j<n;j++){
						if(edg[i][j]==1 && dist[j]==d+1){
							dp[j]=max(dp[j],dp[i]+vpt[j]-kaburi[i][j]);
						}
					}
				}
			}
		}
		int usiro=0;
		for(int i=0;i<n;i++){
			if(dist[i]==dist[0]+1 && edg[0][i]==1)usiro++;
		}
		*/
		int ans=0;
		for(int i=0;i<n;i++)ans=max(ans,dp[0][i]);
		printf("%d\n",ans-dist[0]);
	}
}