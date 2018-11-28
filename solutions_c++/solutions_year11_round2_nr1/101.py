#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>

#define maxn 111

using namespace std;

int test,n;
char a[maxn][maxn];
bool c[maxn][maxn];
double wp[maxn];
double owp[maxn];
double oowp[maxn];

double cal(int i,int j){
	int u,v,t;
	u=0;
	v=0;
	for (t=1;t<=n;t++)
		if (t!=j)
			if (c[i][t]){
				v++;
				if (a[i][t]=='1') u++;
			}
	if (v==0) return 0;
	return (double)(u)/(double)(v);
}

void process(){
	int i,j,u,v;
	double w;
	string s;
	scanf("%d\n",&n);
	memset(c,false,sizeof(c));
	for (i=1;i<=n;i++){
		getline(cin,s);
		u=0;
		v=0;
		for (j=0;j<n;j++){
			a[i][j+1]=s[j];
			if (s[j]=='.') continue;
			c[i][j+1]=true;
			v++;
			if (s[j]=='1') u++;
		}
		if (v==0) wp[i]=0; else
			wp[i]=(double)(u)/(double)(v);
	}
	for (i=1;i<=n;i++){
		v=0;
		owp[i]=0;
		for (j=1;j<=n;j++)
			if (c[i][j]){
				v++;
				owp[i]=owp[i]+cal(j,i);
			}
		owp[i]=owp[i]/(double)(v);
	}
	for (i=1;i<=n;i++){
		v=0;
		oowp[i]=0;
		for (j=1;j<=n;j++)
			if (c[i][j]){
				v++;
				oowp[i]=oowp[i]+owp[j];
			}
		oowp[i]=oowp[i]/(double)(v);
	}
	for (i=1;i<=n;i++){
		w=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
		printf("%0.7lf\n",w);
	}
}

int main(){
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	scanf("%d",&test);
	int i;
	for (i=1;i<=test;i++){
		cout<<"Case #"<<i<<":\n";
		process();
	}
}
