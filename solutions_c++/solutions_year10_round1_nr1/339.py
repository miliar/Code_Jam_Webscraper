#include <iostream>
#include <vector>
#include <cstdio>
#include <set>
#include <algorithm>
#define ST first
#define ND second
#define MP make_pair
#define PB push_back
#define N 55
using namespace std;
typedef long long int lld;
typedef double lf;

vector<char> V;
char T[N][N],Tw[N][N],T2[N][N],akzn;
bool res[2222];
int t,n,k,il,x,y,tt;
int skx[4]={0,1,1,1};
int sky[4]={1,1,0,-1};

int main(){
	scanf("%d",&t);
	while(t--){
		scanf("%d %d",&n,&k);
		res['R']=res['B']=false;
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++)
				Tw[i][j]='.';
		for(int i=1;i<=n;i++)
			scanf("%s",T2[i]+1);
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++)
				T[i][j]=T2[n-j+1][i];
//		for(int i=1;i<=n;i++)
//			printf("%s\n",T[i]+1);
		for(int i=1;i<=n;i++){
			V.clear();
			for(int j=n;j>0;j--){
				if(T[j][i]!='.')
					V.PB(T[j][i]);
			}
			for(int j=0;j<V.size();j++)
				Tw[n-j][i]=V[j];
		}
//		for(int i=1;i<=n;i++)
//			printf("%s\n",Tw[i]+1);
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++){
				for(int kr=0;kr<4;kr++){
					il=1;
					x=i; y=j;
					akzn=Tw[x][y];
					while(x+skx[kr]>0 && x+skx[kr]<=n && y+sky[kr]>0 && y+sky[kr]<=n && Tw[x+skx[kr]][y+sky[kr]]==akzn){
						il++;
						x+=skx[kr];
						y+=sky[kr];
					}
					if(il>=k)
						res[akzn]=true;
				}
			}
		tt++;
		if(res['R'])
			if(res['B'])
				printf("Case #%d: Both\n",tt);
			else
				printf("Case #%d: Red\n",tt);
		else
			if(res['B'])
				printf("Case #%d: Blue\n",tt);
			else
				printf("Case #%d: Neither\n",tt);
	}
}
