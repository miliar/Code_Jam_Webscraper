#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
const int MaxN=600;
const double Eps=1e-6;

using namespace std;
int Map[MaxN][MaxN],N,M,D,T,Ans;
int can(int Ans){
	for (int i=0;i+Ans-1<N;i++)
	for (int j=0;j+Ans-1<M;j++){
		double cx,cy;
		cx=i+i+Ans-1;
		cy=j+j+Ans-1;
		cx=cx*1.0/2;
		cy=cy*1.0/2;
		double X,Y,x,y;
		X=Y=0;
		for (int k=i;k<i+Ans;k++)
		for (int l=j;l<j+Ans;l++){
			if (k==i && l==j) continue;
			if (k==i && l==j+Ans-1) continue;
			if (k==i+Ans-1 && l==j) continue;
			if (k==i+Ans-1 && l==j+Ans-1) continue;
			x=k,y=l;
			x-=cx;
			y-=cy;
			x*=Map[k][l];
			y*=Map[k][l];
			X+=x;
			Y+=y;
		}
		if (fabs(X)<Eps && fabs(Y)<Eps) return 1;
	}
	return 0;
}
int main(){
freopen("B.in","r",stdin);
freopen("B.out","w",stdout);
	cin >> T;
	for (int t=1;t<=T;t++){
		printf("Case #%d: ", t);
		scanf("%d %d %d", &N, &M, &D);
		char ch;
		for (int i=0;i<N;i++)
		for (int j=0;j<M;j++){
			ch=' ';
			while (ch<'0' || ch>'9') cin >> ch;
			Map[i][j]=ch-'0';
		}
		Ans=min(N,M);
		while (Ans>2){
			if (can(Ans)) break;
			Ans--;
		}
		if (Ans<3) printf("IMPOSSIBLE\n");else
		printf("%d\n", Ans);
	}
	return 0;
}
