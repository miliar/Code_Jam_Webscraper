#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <set>
using namespace std;

int i,j,k,l,m,n,ri,repeat,r,a[101][101],b[101][101];

int main(){
	freopen("C-small-attempt0.in","r",stdin);freopen("w.txt","w",stdout);
	scanf("%d",&repeat);
	for(ri=1;ri<=repeat;ri++){
		printf("Case #%d: ",ri);
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		scanf("%d",&r);
		for(i=1;i<=r;i++){
			int x,y,xx,yy;
			scanf("%d%d%d%d",&x,&y,&xx,&yy);
		
			for(j=x;j<=xx;j++)
				for(k=y;k<=yy;k++)
					b[j][k]=1;
		}
		int flag=1,t=0;
		while(flag){
			int ff=1;
			for(i=1;i<=100;i++){
				for(j=1;j<=100;j++)
					if(b[i][j]==1){
						ff=0;
						break;
					}
				if(ff==0)break;
			}
			if(ff==1)break;
			t++;
			for(i=1;i<=100;i++)
				for(j=1;j<=100;j++){
					a[i][j]=b[i][j];
					if(b[i][j]==0&&b[i-1][j]&&b[i][j-1])
						a[i][j]=1;
					if(b[i][j]&&!b[i-1][j]&&!b[i][j-1])
						a[i][j]=0;
				}
			memcpy(b,a,sizeof(a));
		}
		printf("%d\n",t);
			
		
	}
}
