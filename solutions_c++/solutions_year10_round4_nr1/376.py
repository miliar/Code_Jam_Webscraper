#include<iostream>
#include<cstdio>
#include<memory.h>
#include<algorithm>
#include<cstring>
#include<queue>
#include<cmath>
using namespace std;
#define N 200
#define INF 0x7fffffff

int t,k,res=0;
char d[N][N],c;
bool f(int i){
	for(int j=0;j<2*k-1;j++){
		for(int u=0;;u++){
			int v=2*(k-1+i)-u;
			if(v<=u)break;
			if(v>=strlen(d[j]))continue;
			if(d[j][u]==' ' || d[j][v]==' ')continue;
			if(d[j][u]!= d[j][v])return false;
		}
	}
	return true;
}
bool f2(int i){
	for(int j=0;j<2*k-1;j++){
		for(int u=0;;u++){
			int v=2*(k-1+i)-u;
			if(v<=u)break;
			if(v>=2*k-1)continue;
			if(j>=strlen(d[u]))continue;
			if(j>=strlen(d[v]))continue;
			if(d[u][j]==' ' || d[v][j]==' ')continue;
			if(d[u][j]!= d[v][j])return false;
		}
	}
	return true;
}
int main(){
//	freopen("D:\\in.txt","r",stdin);		//////
//	freopen("D:\\A-small-attempt0.in","r",stdin);	//////
//	freopen("D:\\A-small-attempt0.out","w",stdout);	//////
//	freopen("D:\\A-small-attempt1.in","r",stdin);	//////
//	freopen("D:\\A-small-attempt1.out","w",stdout);	//////
	freopen("D:\\A-large.in","r",stdin);	//////
	freopen("D:\\A-large.out","w",stdout);	//////
	int m1,m2;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		scanf("%d",&k);
		while((c=getchar())!='\n');
		for(int j=0;j<2*k-1;j++){
			gets(d[j]);
		}
		int j;
		for(j=0;j<k;j++){
			if(f(j))break;
			if(f(-j))break;
		}
		m1=j;
		for(j=0;j<k;j++){
			if(f2(j))break;
			if(f2(-j))break;
		}
		m2=j;
//		printf("%d,%d\n",m1,m2);
		res=abs(m1+m2+k)*abs(m1+m2+k)-k*k;
		printf("Case #%d: %d\n",i,res);
	}
	return 0;
}