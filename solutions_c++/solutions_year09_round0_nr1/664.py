#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;
#define M 500
#define D 5000
int net[M+5][M+5];
int used[M+5];
int dp[30][20];
char sou[D+100][20];
char mid[M+100][500];
vector<int> ckj[20];
int l,d,n;
int begin;

int init(){
	memset(net,0,sizeof(net));
	int i,j,k;
	
	for(i=0;i<ckj[0].size();i++){
		net[begin][ckj[0][i]]=1;
	}

	int a,b;
	for(i=0;i<l-1;i++){
		for(j=0;j<ckj[i].size();j++){
			a=ckj[i][j];
			for(k=0;k<ckj[i+1].size();k++){
				b=ckj[i+1][k];
				net[a][b]=1;
			}
		}
	}
	return 0;
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,j,k;
	scanf("%d%d%d",&l,&d,&n);
	gets(sou[0]);
	
	for(i=0;i<d;i++)
		scanf("%s",sou[i]);

	for(i=0;i<n;i++)
		scanf("%s",mid[i]);

	begin=400;
	for(i=0;i<n;i++){
		for(j=0;j<l;j++)
			ckj[j].clear();

		j=0;
		k=0;
		while(j<l){
			if(mid[i][k]=='('){
				k++;
				for(;mid[i][k]!=')';k++){
					ckj[j].push_back(j*26+mid[i][k]-'a');
				}
			}
			else {
				ckj[j].push_back(j*26+mid[i][k]-'a');
			}
			j++;
			k++;
		}
		init();
		int res=0;
		for(j=0;j<d;j++){
			if(net[begin][sou[j][0]-'a']==0) continue;
			for(k=0;k<l-1;k++){
				int a=k*26+sou[j][k]-'a';
				int b=(k+1)*26+sou[j][k+1]-'a';
				if(!net[a][b]) break;
			}
			if(k==l-1) res++;
		}
		printf("Case #%d: %d\n",i+1,res);
	}

	return 0;
}