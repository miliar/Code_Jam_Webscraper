#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;


void opens(){
	freopen("Csmall.in","r",stdin);
	freopen("Csmall.out","w",stdout);
}

void openb(){
	freopen("Clarge.in","r",stdin);
	freopen("Clarge.out","w",stdout);
}

int t,A1,A2,B1,B2,ans;

bool dp(int x,int y){
	for (int i=x/y;i>=1;i--){
		if (x-i*y>0){
			if (!dp(x-i*y,y)){
				return 1;
			}
		}
	}
	for (int i=y/x;i>=1;i--){
		if (y-i*x>0){
			if (!dp(x,y-i*x)){
				return 1;
			}
		}
	}
	return 0;
}

int main(){
	opens();
	//openb();
	scanf("%d",&t);
	int xx=1;
	while (t--){
		scanf("%d%d%d%d",&A1,&A2,&B1,&B2);
		ans=0;
		for (int i=A1;i<=A2;i++){
			for (int j=B1;j<=B2;j++){
				if (dp(i,j)){
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n",xx++,ans);
	}
	return 0;
}
