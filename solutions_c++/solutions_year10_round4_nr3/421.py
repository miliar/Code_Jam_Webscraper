#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

long c,r,d[101][101];

int main(){
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	long h,i,j,k,l,m,a,b;
	scanf("%ld",&c);
	for(h=1;h<=c;h++){
		scanf("%ld",&r);
		memset(d,0,sizeof(d));
		for(i=1;i<=r;i++){
			scanf("%ld%ld%ld%ld",&j,&k,&l,&m);
			for(a=j;a<=l;a++)
				for(b=k;b<=m;b++)
					d[a][b]=1;
		}
		k=0;
		while(1){
			for(i=100;i>0;i--){
				for(j=100;j>0;j--)
					if(d[i][j]==1)break;
				if(j>0)break;
			}
			if(i<=0)break;
			k++;
			for(i=100;i>0;i--)
				for(j=100;j>0;j--){
					if(d[i-1][j]==0 && d[i][j-1]==0)d[i][j]=0;
					if(d[i-1][j]==1 && d[i][j-1]==1)d[i][j]=1;
				}
		}
		printf("Case #%ld: %ld\n",h,k);
	}
	return 0;
}