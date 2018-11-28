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

using namespace std;


class est{public:

	int m[109][109];
};
int Y,X,XX,YY;
int MAX = 109;
#define M vc[b].m
#define N vc[a].m
vector<est> vc;

bool f(){
	vc.push_back(vc.back());
	int b=1;
	int a=0;
	bool sw=false;
	
	for(int i=Y;i<=YY;i++){
		for(int j=X;j<=XX;j++){
			if(N[i][j]==1){
				sw=true;
				if(N[i-1][j]==0 and N[i][j-1]==0){
					M[i][j]=0;
				}
			}else{
				if(N[i-1][j]==1 and N[i][j-1]==1)
					M[i][j]=1;
				
			}
		}
	}



	vc.erase(vc.begin());
	return sw;
}
void resuelva(){
	int n;
	scanf("%d",&n);
	int x,xx,y,yy;
	vc.clear();

	est e;
	memset(e.m,0,sizeof(e.m));

	X=109;XX=0;Y=109;YY=0;
	for(int i=1;i<=n;i++){
		scanf("%d %d %d %d",&x,&y,&xx,&yy);
		X=min(X,x);
		Y=min(Y,y);
		XX=max(XX,xx);
		YY=max(YY,yy);
		
		for(int j=y;j<=yy;j++)
			for(int k=x;k<=xx;k++)
				e.m[j][k]=1;
	}
	/*printf("\n%d %d %d %d\n",X,Y,XX,YY);
	for(int i=Y;i<=YY;i++){
		for(int j=X;j<=XX;j++){
			printf("%d",e.m[i][j]);
		}
		printf("\n");
	}*/
	vc.push_back(e);
	int res=0;
	while(f()){
		res++;
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

