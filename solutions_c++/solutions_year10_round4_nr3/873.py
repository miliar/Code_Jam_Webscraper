#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<iostream>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<list>
#include<algorithm>
#include<limits>
using namespace std;
const int N=10000,M=1000000007;
int a[120][120];

int main(){
	int T,R,i,j,k,l,tmpn,c=0,t=0,maxc=0,maxr=0,x1,x2,y1,y2;
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);
	memset(a,0,sizeof(a));
	scanf("%d",&T);
	for(i=1;i<=T;i++){
		scanf("%d",&R);
		while(R--){
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			if(x2>maxc)maxc=x2;
			if(y2>maxr)maxr=y2;
			for(j=x1;j<=x2;j++)
				for(k=y1;k<=y2;k++)
					if(a[j][k]==0){
						c++;
						a[j][k]=1;
					}
		}
		t=0;
		do{
			for(j=maxc;j>=1;j--){
				for(k=maxr;k>=1;k--){
					if(a[j][k]==1){
						if(a[j-1][k]==0 && a[j][k-1]==0){
							a[j][k]=0;
							c--;
						}
					}else{
						if(a[j-1][k]==1 && a[j][k-1]==1){
							a[j][k]=1;
							c++;
						}
					}
				}
			}
			t++;
		}while(c>0);
		printf("Case #%d: %d\n",i,t);
	}
	return 0;
}

