#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <string>
#include <sstream>
#include <queue>
using namespace std;
typedef long long llong;
const int Mod=100003;
const int Max=512;
int cb[Max][Max];
int f[Max][Max],res[Max];
int main(){
	for(int i=0;i<Max;++i){
		cb[i][0]=cb[i][i]=1;
		for(int j=1;j<i;++j){
			cb[i][j]=cb[i-1][j-1]+cb[i-1][j];
			if(cb[i][j]>=Mod) cb[i][j]-=Mod;
		}
	}
	memset(f,0,sizeof(f));
	for(int a=2;a<Max;++a){
		if(a==500){
			++a;
			--a;
		}
		f[a][1]=1;
		res[a]=1;
		for(int b=2;b<a;++b){
			for(int i=1;i<b;++i){
				f[a][b]=(f[a][b]+(llong)f[b][i]*cb[a-b-1][b-i-1])%Mod;
			}
			res[a]=(res[a]+f[a][b])%Mod;
		}
	}
//	for(int i=2;i<=500;++i){
//		printf("%d %d\n",i,res[i]);
//		if(i%40==0) system("pause");
//	}
	int TT;
	scanf("%d",&TT);
	for(int cas=1;cas<=TT;++cas){
		int n;
		scanf("%d",&n);
		printf("Case #%d: %d\n",cas,res[n]);
	}
	return 0;
}

