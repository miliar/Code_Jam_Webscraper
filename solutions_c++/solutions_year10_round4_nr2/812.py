/**
* @author Gareve
* @problem
* @judge
*/
#define DEBUG
#ifndef NDEBUG	
	#define DBG(a) cout<<__LINE__<<": "<<#a<<"= "<<a<<endl;
#else
	#define DBG(a) ;
#endif
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cassert>

using namespace std;
const int MAX = 1025;

int vc[MAX],res;
int m[MAX][1029];
int q,Y;
int tree[MAX][1029];

int mn(int y,int x){
	while(y>=0){
		x*=2;
		y--;
	}
	return x;
}
int mx(int y,int x){
	while(y>=0){
		x*=2;
		x++;
		y--;
	}
	return x;
}
void comprar(int x){
	x/=2;
	int a=-1,b=-1;
	for(int y=0;y<Y;y++){
		if(tree[y][x]==0){
			a=y;b=x;
		}
		x/=2;
	}
	if(a!=-1){
		tree[a][b]=1;
		int la=mn(a,b),lb=mx(a,b);
//			printf("El %d %d: %d %d\n",a,b,la,lb);
		for(int i=la;i<=lb;i++)
			vc[i]--;
	}
}
void resuelva(){
	int n;
	scanf("%d",&Y);
	n=1<<Y;
	int k=n;

	memset(tree,0,sizeof(tree));
	for(int i=0;i<n;i++){
		scanf("%d",&vc[i]);
		vc[i]=Y-vc[i];
	}
	k>>=1;

	q=0;
	while(k>=1){
		for(int i=0;i<k;i++)
			scanf("%d",&m[q][i]);
		k>>=1;
		q++;
	}
	res=0;
//			for(int w=0;w<n or !printf("\n");w++)printf("%d ",vc[w]);
	for(int i=0;i<n;i++){
//		printf(":%d -> %d\n",i,vc[i]);
		while(vc[i]>0){
			//for(int w=0;w<n or !printf("\n");w++)printf("%d ",vc[w]);
			//			printf("Comp %d\n",i);
			comprar(i);
			res++;
		}
	}
	printf("%d\n",res);
}
int main(){
	int n;
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		printf("Case #%d: ",i);
		resuelva();
	}
}

