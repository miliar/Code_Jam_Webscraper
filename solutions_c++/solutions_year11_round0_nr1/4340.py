#include<stdio.h>
#include<queue>
#include<string.h>
#include<iostream>
#include<algorithm>
using namespace std;
#define M 105
int main(){
	int cas,i,j,n,oq,bq,r,ans,oh,bh;
	int count=1;
	char c;
	freopen("C:\\Users\\lenovo\\Desktop\\A-small-attempt3.in","r",stdin);
	freopen("C:\\Users\\lenovo\\Desktop\\stdout.txt","w",stdout);
	scanf("%d",&cas);
	while(cas--&&scanf("%d",&n)){
		oq=bq=oh=bh=1;ans=0;
		for(i=0;i<n;i++){
			scanf(" %c %d",&c,&r);
			if(c=='O'){
				while(1){
					if(oq<=r&&oh>=r) break;
					oh++;
					bh++;
					bq--;
					oq--;
					ans++;
				}
				oq=oh=r;
				bq--;bh++;
				ans++;
			}
			else if(c=='B'){
				while(1){
					if(bq<=r&&bh>=r) break;
					oh++;
					bh++;
					bq--;
					oq--;
					ans++;
				}
				bq=bh=r;
				oq--;oh++;
				ans++;
			}
		}
		printf("Case #%d: %d\n",count++,ans);
	}
	return 0;
}
