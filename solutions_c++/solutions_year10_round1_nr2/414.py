#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <cmath>
#include <vector>

#define maxn 1000
#define maxC 1000000000

using namespace std;

int test,n,m,cost_d,cost_i,res;
int a[maxn],b[maxn],d[maxn];
int c[maxn][maxn];
int dp[maxn][maxn];

void input(){
	int i;
	cin>>cost_d>>cost_i>>m>>n;
	for (i=1;i<=n;i++) cin>>a[i];
}

void init(){
	int i,j,v,t;
	if (m==0){
		for (i=0;i<=255;i++)
			for (j=0;j<=255;j++) 
				if (i==j) c[i][j]=0; else c[i][j]=maxC;
		return;
	}
	for (i=0;i<=255;i++)
		for (j=i;j<=255;j++){
			v=i;
			t=0;
			while (v+m<j){
				t++;
				v=v+m;
			}
			c[i][j]=t;
			c[j][i]=t;
		}
}

void dynamic_programming(){
	int i,j,u,v,t;
	res=cost_d*n;
	for (i=1;i<=n;i++)
		for (j=0;j<=255;j++){
			dp[i][j]=cost_d*(i-1)+abs(j-a[i]);
			if (i>1)
				for (u=1;u<i;u++)
					for (v=0;v<=255;v++){
						if (c[j][v]==maxC) continue;
						t=dp[u][v]+cost_d*(i-u-1)+cost_i*c[j][v]+abs(j-a[i]);
						dp[i][j]=min(dp[i][j],t);
					}	
		}
	for (i=1;i<=n;i++)
		for (j=0;j<=255;j++) res=min(res,dp[i][j]+cost_d*(n-i));
}

void update(){
	int i,j,v,t;
	v=0;
	for (i=1;i<=n;i++)
		if (d[i]==1) v++;
	t=v*cost_d;
	for (i=1;i<=n;i++)
		if (d[i]==0) t=t+abs(b[i]-a[i]);
	for (i=1;i<=n;i++)
		if (d[i]==0)
			if (i>1)
				for (j=i-1;j>=1;j--)
					if (d[j]==0){
						if (c[b[j]][b[i]]==maxC) return; else
							t=t+cost_i*c[b[j]][b[i]];
						break;
					}
	res=min(res,t);
}

void visit2(int i){
	if (d[i]==1){
		if (i<n) visit2(i+1); else update();
		return;
	}
	int j;
	for (j=0;j<=255;j++){
		b[i]=j;
		if (i<n) visit2(i+1); else update();
	}
}

void visit1(int i){
	int j;
	for (j=0;j<=1;j++){
		d[i]=j;
		if (i<n) visit1(i+1); else visit2(1);
	}
}

int main(){
	//freopen("B-small-attempt4.in","r",stdin);
	//freopen("output.txt","w",stdout);
	cin>>test;
	int i;
	for (i=1;i<=test;i++){
		input();
		init();
		//dynamic_programming();
		res=maxC;
		visit1(1);
		cout<<"Case #"<<i<<": "<<res<<"\n";
	}
}
