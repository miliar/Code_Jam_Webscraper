#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>

#define maxn 101

using namespace std;

int test,n,m,res;
bool a[maxn][maxn];
bool b[maxn][maxn];

void input(){
	int i,u,v,x1,y1,x2,y2;
	memset(a,false,sizeof(a));
	cin>>n;
	m=0;
	for (i=1;i<=n;i++){
		cin>>x1>>y1>>x2>>y2;
		for (u=min(x1,x2);u<=max(x1,x2);u++)
			for (v=min(y1,y2);v<=max(y1,y2);v++){
				a[u][v]=true;
				m=max(m,u);
				m=max(m,v);
			}
	}
	n=m;
}

void process(){
	int i,j,v;
	res=0;
	while (true){
		v=0;
		for (i=1;i<=n;i++)
			for (j=1;j<=n;j++){
				if (a[i][j])
					if ((!a[i-1][j])&&(!a[i][j-1])) b[i][j]=false; 
					else{
						v++;
						b[i][j]=true;
					}
				if (!a[i][j])
					if ((a[i-1][j])&&(a[i][j-1])){
						b[i][j]=true;
						v++;
					}else b[i][j]=false;
			}
		res++;
		if (v==0) break;
		for (i=1;i<=n;i++)
			for (j=1;j<=n;j++) a[i][j]=b[i][j];
	}
}

int main(){
	//freopen("C-small-attempt0.in","r",stdin);
	//freopen("output.txt","w",stdout);
	cin>>test;
	int i;
	for (i=1;i<=test;i++){
		input();
		process();
		cout<<"Case #"<<i<<": "<<res<<"\n";
	}
}
