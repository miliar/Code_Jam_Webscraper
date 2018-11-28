#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <cmath>
#include <vector>

#define maxn 601
#define maxC 1000000000

using namespace std;

int test,n,m,k,xo,yo,xt,yt,res;
int a[maxn][maxn];
int b[maxn][maxn];

void input(){
	int i,j,u,v,t;
	memset(a,0,sizeof(a));
	cin>>n;
	u=0;
	t=n+1;
	for (v=1;v<=2*n-1;v++){
		if (v<=n){
			t--;
			u++;
		}else{
			t++;
			u--;
		}
		for (i=1;i<=u;i++){
			cin>>j;
			j++;
			a[xo+t+2*(i-1)][yo+v]=j;
		}
	}
}

bool search(){
	int i,j,u,v;
	memset(b,0,sizeof(b));
	m=100;
	for (i=xo+1;i<=xo+2*n-1;i++)
		for (j=yo+1;j<=yo+2*n-1;j++) b[i][j]=a[i][j];
	xt=xt+xo;
	yt=yt+yo;
	for (i=xo+1;i<=xo+2*n-1;i++)
		for (j=yo+1;j<=yo+2*n-1;j++)
			if (b[i][j]>0){
				if (i>xt){
					u=xt-(i-xt);
					v=j;
				}
				if (i<xt){
					u=xt+(xt-i);
					v=j;
				}
				if (i==xt){
					u=i;
					v=j;
				}
				if (b[u][v]==0)
					b[u][v]=b[i][j];
				else
					if (b[u][v]!=b[i][j]) return false;
				if (j>yt){
					v=yt-(j-yt);
					u=i;
				}
				if (j<yt){
					v=yt+(yt-j);
					u=i;
				}
				if (j==yt){
					u=i;
					v=j;
				}
				if (b[u][v]==0)
					b[u][v]=b[i][j];
				else
					if (b[u][v]!=b[i][j]) return false;
			}
	return true;
}

void process(){
	int i,j;
	res=maxC;
	for (i=1;i<=2*n-1;i++)
		for (j=1;j<=2*n-1;j++){
			xt=i;
			yt=j;
			k=n+abs(n-i)+abs(n-j);
			if (k*k-n*n<res)
				if (search()) res=min(res,k*k-n*n);
		}
}

int main(){
	//freopen("A-large.in","r",stdin);
	//freopen("output.txt","w",stdout);
	cin>>test;
	int i;
	xo=300;
	yo=300;
	for (i=1;i<=test;i++){
		input();
		process();
		cout<<"Case #"<<i<<": "<<res<<"\n";
	}
}
