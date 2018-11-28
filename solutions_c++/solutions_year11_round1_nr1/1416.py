#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<cmath>
using namespace std;

#define F(i,n) for(i=0;i<n;i++)
#define FF(i,n) for(i=1;i<=n;i++)
#define LL __int64

int Pd, Pg, N, D, G;

bool work(){
	int i, j, dd, dg;
	if(Pg==0&&Pd==0) return true;
	if(Pg==0&&Pd) return false;
	if(Pg==100&&Pd<100) return false;
	
	for(i=1;i<101;i++)if(i*100%Pg==0)break;
	dg = i;
	
//	if(Pd==0) return dg<=N;
	
	for(i=1;i<101;i++)if(i*Pd%100==0)break;
	dd = i;
//	cout<<dd<<endl;
	
	if(dd<=N) return true;
	return false;
	
	D = dd;
	G = Pd*D/Pg;
	if(Pd*D%Pg)G++;
	
	while(G%dg)G++;
	
	if(G<=N) return true;
	return false;
}

int main(){
     int i, j, n, T, TT=1;
     freopen("A-small-attempt1.in","r",stdin);
     freopen("A.out","w",stdout);
     scanf("%d",&T);
     while(T--){
		scanf("%d%d%d",&N,&Pd,&Pg);
		printf("Case #%d: ", TT++);
		if(work())printf("Possible\n");
		else printf("Broken\n");
	}
     return 0;
}
